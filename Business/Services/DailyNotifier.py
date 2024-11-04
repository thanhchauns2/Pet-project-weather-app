from Business.Entity.WeatherForecaster import WeatherForecaster

class DailyNotifier:
    def __init__(self, weather_forecaster: WeatherForecaster):
        self.weather_forecaster = weather_forecaster
    
    def temperature_2m_max(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["temperature_2m_max"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
        return daily_temperature_2m_max

    def temperature_2m_min(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["temperature_2m_min"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_temperature_2m_min = daily.Variables(0).ValuesAsNumpy()
        return daily_temperature_2m_min

    def apparent_temperature_max(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["apparent_temperature_max"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_apparent_temperature_max = daily.Variables(0).ValuesAsNumpy()
        return daily_apparent_temperature_max

    def apparent_temperature_min(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["apparent_temperature_min"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_apparent_temperature_min = daily.Variables(0).ValuesAsNumpy()
        return daily_apparent_temperature_min

    def sunrise(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["sunrise"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_sunrise = daily.Variables(0).ValuesAsNumpy()
        return daily_sunrise

    def sunset(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["sunset"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_sunset = daily.Variables(0).ValuesAsNumpy()
        return daily_sunset

    def daylight_duration(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["daylight_duration"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_daylight_duration = daily.Variables(0).ValuesAsNumpy()
        return daily_daylight_duration

    def sunshine_duration(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["sunshine_duration"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_sunshine_duration = daily.Variables(0).ValuesAsNumpy()
        return daily_sunshine_duration

    def uv_index_max(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["uv_index_max"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_uv_index_max = daily.Variables(0).ValuesAsNumpy()
        return daily_uv_index_max

    def uv_index_clear_sky_max(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["uv_index_clear_sky_max"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_uv_index_clear_sky_max = daily.Variables(0).ValuesAsNumpy()
        return daily_uv_index_clear_sky_max

    def rain_sum(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["rain_sum"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_rain_sum = daily.Variables(0).ValuesAsNumpy()
        return daily_rain_sum

    def snowfall_sum(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["snowfall_sum"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_snowfall_sum = daily.Variables(0).ValuesAsNumpy()
        return daily_snowfall_sum

    def wind_speed_10m_max(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["wind_speed_10m_max"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_wind_speed_10m_max = daily.Variables(0).ValuesAsNumpy()
        return daily_wind_speed_10m_max

    def wind_gusts_10m_max(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, None, ["wind_gusts_10m_max"], "Asia/Bangkok")
        response = responses[0]
        daily = response.Daily()
        daily_wind_gusts_10m_max = daily.Variables(0).ValuesAsNumpy()
        return daily_wind_gusts_10m_max
