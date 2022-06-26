from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('ef2206ff5da67de63306d0b143e20872')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
city = input("Please print the city:\n")
observation = mgr.weather_at_place(city)
w = observation.weather

print(f"In {city.title()} is {w.detailed_status}")         # 'clouds'
speed_wind = w.wind()
print(f" The speed in {city.title()} is {speed_wind['speed']}")    # {'speed': 4.6, 'deg': 330}
print(f"Humidity in {city.title()} is {w.humidity}")                # 87
print(f"Temperature in {city.title()} is {w.temperature('celsius')}")  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75
