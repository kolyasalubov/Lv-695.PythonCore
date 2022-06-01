from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('ef2206ff5da67de63306d0b143e20872')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('London,GB')
w = observation.weather

city=input("The weather in which city are you interested in: ")
wind=w.wind()
temp=w.temperature('celsius')
humidity=w.humidity

if wind.get('speed')<5:
    print(f"The wind in {city} is light today, {wind.get('speed')} m.p.h.")
elif  wind.get('speed')<10:
    print(f"The wind in {city} is medium today, {wind.get('speed')} m.p.h.")
elif  wind.get('speed')>10:
      print(f"The wind in {city} is strong today, {wind.get('speed')} m.p.h.")

if temp.get('temp_max')>=25:
    print(f"The weather is hot today. During the day the temperature rises to {temp.get('temp_max')} degrees C. Night temperature is {temp.get('temp_min')} degrees C.")
elif temp.get('temp_max')>=10:
    print(f"The weather is warm today. During the day the temperature rises to {temp.get('temp_max')} degrees C. Night temperature is {temp.get('temp_min')} degrees C.")
elif temp.get('temp_max')>=0:
    print(f"The weather is cool today. During the day the temperature rises to {temp.get('temp_max')} degrees C. Night temperature is {temp.get('temp_min')} degrees C.")
elif temp.get('temp_max')<0:
    print(f"It's frosty today. During the day the temperature rises to {temp.get('temp_max')} degrees C. Night temperature is {temp.get('temp_min')} degrees C.")

print(f"In {city} the humidity of the air is {humidity}%.")
