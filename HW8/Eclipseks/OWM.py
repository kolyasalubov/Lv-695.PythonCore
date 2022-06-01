from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('ef2206ff5da67de63306d0b143e20872')
mgr = owm.weather_manager()
city = input("Write city: ")
observation = mgr.weather_at_place(city)
w = observation.weather

print(f"In {city}: {w.detailed_status}")
speed_wind = w.wind()
print(f"Wind speed in {city}: {speed_wind['speed']}km/h")
print(f"Humidity in {city}: {w.humidity}% \n")
temp = w.temperature('celsius')
print("Temperature:")
print(f"""Now temp in {city}: {temp['temp']}℃
Feels like: {temp['feels_like']}
Max temp today in {city}: {temp['temp_max']}℃
Min temp today in {city}: {temp['temp_min']}℃""")
w.rain
w.heat_index
w.clouds