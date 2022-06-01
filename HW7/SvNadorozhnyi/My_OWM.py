from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('48d138eddece31bb7c8228eb1328a70f')
mgr = owm.weather_manager()

weather_place = input("Enter a city in which you need to know the weather: ")
observation = mgr.weather_at_place(weather_place)
w = observation.weather

clouds = w.detailed_status
speed_wind = w.wind()['speed']
humidity = w.humidity
temperature = w.temperature('celsius')['temp']
print(f"In {weather_place} the wind speed is {speed_wind} km/hours")
print(f"In {weather_place} the humidity of the air is {humidity}")
print(f"In {weather_place} the temperature of the air is {temperature}")
