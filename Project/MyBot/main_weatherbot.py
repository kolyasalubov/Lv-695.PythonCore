import requests
import datetime
from config import telegram_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=telegram_bot_token)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=["start"])
async def start_comand(message: types.Message):
    await message.reply("Привіт! Буду радий допомогти тобі дізнатися погоду")


@dispatcher.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Хмарно \U00002601",
        "Rain": "Дощ \U00002614 варто взяти парасолю",
        "Drizzle": "Дощ \U00002614",
        "Thunderstorm": "Гроза \U000026A1 краще сиди дома",
        "Snow": "Сніг \U0001F328 вдягайся тепліше",
        "Mist": "Туман \U0001F32B"
    }

    try:
        get_requests = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = get_requests.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Подивися у вікно, не зрозумію, що там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_times = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_times = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_times - sunrise_times

        await message.reply(f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}\n"
                            f"Погода в місті {city}:\n{wd}\nТемпература: {cur_weather}°C\n"
                            f"Вологість: {humidity}% \U0001F4A6\nТиск: {pressure} мм.рт.ст\n"
                            f"Швидкість вітру: {wind} м/c \U0001F4A8\n"
                            f"Схід сонця {sunrise_times.strftime('%d-%m-%Y %H:%M')} \U0001F305\n"
                            f"Захід сонця {sunset_times.strftime('%d-%m-%Y %H:%M')} \U0001F307\n"
                            f"Тривалість дня {length_of_the_day} \U0001F566\n"
                            f"Гарного дня і успіхів!"
                            )
    except Exception:
        await message.reply("\U00002620 Перевірте назву міста \U00002620")


if __name__ == "__main__":
    executor.start_polling(dispatcher)
