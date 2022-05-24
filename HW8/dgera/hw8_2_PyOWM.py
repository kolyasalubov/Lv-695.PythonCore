from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

# owm = OWM('7e79a512f516c6f26c7d8a6473dcb146')
owm = OWM('ef2206ff5da67de63306d0b143e20872')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
city = input('Please enter a city name for weather data: ')
observation = mgr.weather_at_place(city)
w = observation.weather

print()
print(f'===== Weather data in {city.capitalize()} =====')
print(f'Current weather status: {w.status} ({w.detailed_status})')
print(f'Cloudiness: {w.clouds} %')

print(f'Humidity: {w.humidity} %')

temp_celsius = w.temperature('celsius')
print(f'Current temperature: {temp_celsius["temp"]} degrees')
print(f'Minimum temperature: {temp_celsius["temp_min"]} degrees')
print(f'Maximum temperature: {temp_celsius["temp_max"]} degrees')
print(f'Feels like: {temp_celsius["feels_like"]} degrees')

print(f'Wind speed: {w.wnd["speed"]} meters per second')
print(f'Wind direction: {w.wnd["deg"]} degrees')

print(f'Pressure: {w.pressure["press"]} hPa')
print(f'Visibility distance: {w.visibility()} meters')

print(f'Sunrise time: {w.sunrise_time(timeformat = "iso")}')
print(f'Sunset time: {w.sunset_time(timeformat = "iso")}')
