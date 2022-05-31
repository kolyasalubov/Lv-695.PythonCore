from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mark1 = KeyboardButton('Точка збору')
mark2 = KeyboardButton('Дрінк & Фуд')
mark3 = KeyboardButton('Моктейлі')
mark4 = KeyboardButton('Лимонади')
mark5 = KeyboardButton('Страви')
mark6 = KeyboardButton('Назад')
mark7 = KeyboardButton('Кава')
mark8 = KeyboardButton('Акції')

client_kb = ReplyKeyboardMarkup(resize_keyboard=True)
client_kb.add(mark2).insert(mark1)
client_kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
client_kb_menu.add(mark3).insert(mark4).add(mark7).insert(mark5).add(mark8).insert(mark6)
