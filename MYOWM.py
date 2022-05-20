from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


owm = OWM('ef2206ff5da67de63306d0b143e20872')
mgr = owm.weather_manager()

town = input('In which city do you want to know the weather?\n')

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(town)
w = observation.weather

print(f'Today in {town} is {w.detailed_status}')         # 'clouds'
speed_wind = w.wind()
print(f"Speed of the wind is {speed_wind['speed']} km/h")                 # {'speed': 4.6, 'deg': 330}
print(f'Humidity is {w.humidity} %')                # 87
temp = w.temperature('celsius')
print(f"Temperature is {temp['temp']} ℃\n"
      f"Maximal temperature today rises to {temp['temp_max']} ℃\n"
      f"Minimum temperature drop to {temp['temp_min']} ℃")  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(f'It was forecast for {town}')
