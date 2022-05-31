from aiogram import Dispatcher, types
from create_bot import bot, dp
from keyboard import client_kb
from keyboard import client_kb_menu
from data_base import sqlite_db

async def commands_start(message : types.Message):
    await message.answer("Прямуй за напоєм та за настроєм до нас!", reply_markup=client_kb)

async def commands_starts(message : types.Message):
    await message.answer("Головне меню", reply_markup=client_kb)

async def commands_info(message : types.Message):
    await message.answer(""" ● м.Академ містечко
    проспект Паладіна 24/7
    YMB
    8:00 - 20:00

● ПП Борщагівка
    вул Соборна 2а
    YMB
    8:00 - 20:00
    Ту гоу формат

tel: +380954491343
""")

async def moco_menu_command(message : types.Message):
    await message.answer('Ми рекомендуємо - Моктейль, а обирати тобі:', reply_markup=client_kb_menu)

async def mockteil(message : types.Message):
    await sqlite_db.sql_read(message)

async def lemonad(message : types.Message):
    await sqlite_db.sql_read1(message)

async def dishes(message : types.Message):
    await sqlite_db.sql_read2(message)
    
async def kofe(message : types.Message):
    await sqlite_db.sql_read3(message)

async def aktsii(message : types.Message):
    await message.answer("""● Пн-Пт до 11:00
    -25%

● Пн-Сб з 15:00 до 18:00
   1 + 1

● В Нд - 50%
   Бо Бог тебе ❤

● НВ (7 днів до | 7 днів потому) 
   -25%    """)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(commands_starts, lambda message: 'Назад' in message.text)
    dp.register_message_handler(commands_info, lambda message: 'Точка' in message.text)
    dp.register_message_handler(moco_menu_command, lambda message: 'Дрінк' in message.text)
    dp.register_message_handler(mockteil, lambda message: 'Моктейлі' in message.text)
    dp.register_message_handler(lemonad, lambda message: 'Лимонади' in message.text)
    dp.register_message_handler(dishes, lambda message: 'Страви' in message.text)
    dp.register_message_handler(kofe, lambda message: 'Кава' in message.text)
    dp.register_message_handler(aktsii, lambda message: 'Акції' in message.text)