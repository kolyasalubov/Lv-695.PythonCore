from pyowm import OWM

owm = OWM('09f55d3948dde6b940267613ad7d781f')
mgr = owm.weather_manager()


def get_city_weather():
    city = input('To find out the weather forecast, please enter the city name: ')
    observation = mgr.weather_at_place(city)
    w = observation.weather
    print(f"Today in {city}, the temperature is {w.temperature('celsius')['temp']}°C, and {w.detailed_status}.\n"
          f"The wind speed: {w.wind()['speed']} km/h\n"
          f"The humidity of the air: {w.humidity}%")


get_city_weather()
