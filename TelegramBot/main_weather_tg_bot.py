import requests
import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

open_weather_token = 'ef2206ff5da67de63306d0b143e20872'
tg_bot_token = '5534199428:AAGLKToaRbijeGU5Catr4FkIy78jPHYE1LE'

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привіт!\nНапиши назву міста і я надішлю тобі інформацію про погоду.')

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        
        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        lenght_of_the_day = sunset_timestamp - sunrise_timestamp

        await message.reply(f'*** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} ***\n'
              f'Погода в місті: {city}\nТемпература: {cur_weather} C\nВологість: {humidity} %\n'
              f'Атмосферний тиск: {pressure} мм.рт.ст.\nШвидкість вітру: {wind} м\с\n'
              f'Світанок: {sunrise_timestamp}\nЗахід сонця: {sunset_timestamp}\n'
              f'Тривалість дня: {lenght_of_the_day}\n*** Гарного дня! ***')

    except:
        await message.reply('Перевірте назву міста.')

if __name__ == '__main__':
    executor.start_polling(dp)