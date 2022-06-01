from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


owm = OWM('afa86948e465dba800e0d259077f48e1')
mgr = owm.weather_manager()

city = input("Enter a city in which you need to know the weather: ")
observation = mgr.weather_at_place(city)
w = observation.weather

humidity = w.humidity
clouds = w.detailed_status
wind_speed = w.wind()['speed']
temp = w.temperature('celsius')['temp']
print(f"In {city} the wind speed is {wind_speed} km/hours")
print(f"In {city} the humidity of the air is {humidity}%")
print(f"In {city} the temperature of the air is {temp}°C")
