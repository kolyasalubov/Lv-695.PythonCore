from pyowm import OWM

owm = OWM('ef2206ff5da67de63306d0b143e20872')
mgr = owm.weather_manager()

town = input('Input city where you want to know wheathere\n')

observation = mgr.weather_at_place(town)
w = observation.weather

print(f'Today in {town} is {w.detailed_status}')         
speed_wind = w.wind()

print(f"Speed of the wind is {speed_wind['speed']} km/h")                
print(f'Humidity is {w.humidity} %')      

temp = w.temperature('celsius')

print(f"Temperature is {temp['temp']} ℃\n"
      f"Maximal temperature today rises to {temp['temp_max']} ℃\n"
      f"Minimum temperature drop to {temp['temp_min']} ℃")  

print(f'It was forecast for {town}')