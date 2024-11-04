import requests_cache
import openmeteo_requests
from retry_requests import retry
from Business.Constants import Constants

class WeatherForecaster:
    def __init__(self) -> None:
        self.cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        self.retry_session = retry(self.cache_session, retries = 5, backoff_factor = 0.2)
        self.openmeteo = openmeteo_requests.Client(session = self.retry_session)
    
    def get_weather_data(self, latitude: float, longitude: float, hourly_variables: list[str], daily_variables: list[str], timezone: str):
        params = {
            "latitude": latitude,
            "longitude": longitude
        }
        if hourly_variables:
            params["hourly"] = hourly_variables
        if daily_variables:
            params["daily"] = daily_variables
        if timezone:
            params["timezone"] = timezone
        response = self.openmeteo.weather_api(
            url = Constants.WEATHER_API_URL,
            params = params
        )
        return response

