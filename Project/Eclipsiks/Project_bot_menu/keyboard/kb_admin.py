from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


mark_admin1 = KeyboardButton('/Додати')
# mark_admin2 = KeyboardButton('/Удалить')
mark_admin3 = KeyboardButton('/Відміна')
mark_admin4 = KeyboardButton('/Моктейль')
mark_admin5 = KeyboardButton('/Лимонад')
mark_admin6 = KeyboardButton('/Страва')
mark_admin10 = KeyboardButton('/Кофе')
# mark_admin7 = KeyboardButton('/Удалить_моктейль')
# mark_admin8 = KeyboardButton('/Удалить_лимонад')
# mark_admin9 = KeyboardButton('/Удалить_блюдо')
mark_admin0 = KeyboardButton('/Головне_меню')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(mark_admin1).insert(mark_admin3).add(mark_admin0)
button_add_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(mark_admin4).insert(mark_admin5).add(mark_admin6).insert(mark_admin3).add(mark_admin10)
# button_remove_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(mark_admin7).insert(mark_admin8).insert(mark_admin9)