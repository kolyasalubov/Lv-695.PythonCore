# import sys
# sys.path.append("pyowm")

# from pyowm import OWM
# from pyowm.utils import config, timestamps

# # ---------- FREE API KEY examples ---------------------

# owm = OWM('ef2206ff5da67de63306d0b143e20872')
# mgr = owm.weather_manager()


# # Search for current weather in London (Great Britain) and get details
# observation = mgr.weather_at_place('Lviv')
# w = observation.weather

# print(w.detailed_status)         # 'clouds'
# speed_wind = w.wind() 
# print(speed_wind['speed'])                 # {'speed': 4.6, 'deg': 330}
# print(w.humidity)                # 87
# print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# w.rain                    # {}
# w.heat_index              # None
# w.clouds                  # 75
