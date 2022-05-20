from turtle import speed
import My_owm1

city=input("The weather in which city are you interested in: ")
wind=My_owm1.w.wind()
temp=My_owm1.w.temperature('celsius')

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