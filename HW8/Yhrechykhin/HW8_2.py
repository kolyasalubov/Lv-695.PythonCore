from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('ea9c7e8af00ce88e33461980a4116d13')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
location = input("Please enter the city where you want to know the weather:\n")
observation = mgr.weather_at_place(location)
w = observation.weather

print(f"In {location.title()} {w.detailed_status}.")         # 'clouds'
speed_wind = w.wind() 
print(f"Speed of wind in {location.title()}: {speed_wind['speed']}.")                 # {'speed': 4.6, 'deg': 330}
print(f"Humidity in {location.title()}: {w.humidity}.")                # 87
temp_celsius = w.temperature('celsius')
print(f"Temperature in {location.title()}: {temp_celsius['temp']} °С.")  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75
