from Business.Entity.WeatherForecaster import WeatherForecaster

class HourlyNotifier:
    def __init__(self, weather_forecaster: WeatherForecaster):
        self.weather_forecaster = weather_forecaster
    
    def temperature_2m(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, ["temperature_2m"], None, "Asia/Bangkok")
        response = responses[0]
        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
        return hourly_temperature_2m

    def relative_humidity_2m(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, ["relative_humidity_2m"], None, "Asia/Bangkok")
        response = responses[0]
        hourly = response.Hourly()
        hourly_relative_humidity_2m = hourly.Variables(0).ValuesAsNumpy()
        return hourly_relative_humidity_2m

    def dew_point_2m(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, ["dew_point_2m"], None, "Asia/Bangkok")
        response = responses[0]
        hourly = response.Hourly()
        hourly_dew_point_2m = hourly.Variables(0).ValuesAsNumpy()
        return hourly_dew_point_2m

    def apparent_temperature(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, ["apparent_temperature"], None, "Asia/Bangkok")
        response = responses[0]
        hourly = response.Hourly()
        hourly_apparent_temperature = hourly.Variables(0).ValuesAsNumpy()
        return hourly_apparent_temperature

    def precipitation_probability(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, ["precipitation_probability"], None, "Asia/Bangkok")
        response = responses[0]
        hourly = response.Hourly()
        hourly_precipitation_probability = hourly.Variables(0).ValuesAsNumpy()
        return hourly_precipitation_probability

    def precipitation(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, ["precipitation"], None, "Asia/Bangkok")
        response = responses[0]
        hourly = response.Hourly()
        hourly_precipitation = hourly.Variables(0).ValuesAsNumpy()
        return hourly_precipitation

    def rain(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, ["rain"], None, "Asia/Bangkok")
        response = responses[0]
        hourly = response.Hourly()
        hourly_rain = hourly.Variables(0).ValuesAsNumpy()
        return hourly_rain

    def showers(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, ["showers"], None, "Asia/Bangkok")
        response = responses[0]
        hourly = response.Hourly()
        hourly_showers = hourly.Variables(0).ValuesAsNumpy()
        return hourly_showers

    def snowfall(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, ["snowfall"], None, "Asia/Bangkok")
        response = responses[0]
        hourly = response.Hourly()
        hourly_snowfall = hourly.Variables(0).ValuesAsNumpy()
        return hourly_snowfall

    def snow_depth(self, latitude: float, longitude: float):
        responses = self.weather_forecaster.get_weather_data(latitude, longitude, ["snow_depth"], None, "Asia/Bangkok")
        response = responses[0]
        hourly = response.Hourly()
        hourly_snow_depth = hourly.Variables(0).ValuesAsNumpy()
        return hourly_snow_depth