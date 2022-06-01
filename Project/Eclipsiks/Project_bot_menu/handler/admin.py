from aiogram.dispatcher import FSMContext 
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, types
from create_bot import dp, bot
from data_base import sqlite_db
from keyboard import kb_admin, kb_client
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ID = None

class FSMDishes(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Оберіть дію', reply_markup=kb_admin.button_case_admin)
    await message.delete()
    


async def cm_starter(message : types.Message):
    if message.from_user.id == ID:        
        await FSMDishes.photo.set()
        await message.reply('Додайте фотографію товару.')

async def go_home(message : types.Message):
    if message.from_user.id == ID:
        await message.answer('Головне меню.', reply_markup=kb_client.client_kb)

async def first_wind(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.answer('Головне меню.', reply_markup=kb_client.client_kb)

async def cencel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Зміни не внесені.')

async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMDishes.next()
        await message.reply('Введіть назву товару')

async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMDishes.next()
        await message.reply('Введіть опис товару')

async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMDishes.next()
        await message.reply('Введіть ціну за одну одиницю')

async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = (message.text)
        await FSMDishes.next()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("Моктейль", "Лимонад")
        markup.add("Страва", "Кофе")
        markup.add("/Відміна")
        await message.reply('Куди додати позицію?', reply_markup=markup)

async def choose_where(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        await sqlite_db.sql_add_command(state)  
        await state.finish()
        await message.answer('Зміни внесені.', reply_markup=kb_admin.button_case_admin)

async def choose_where1(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        await sqlite_db.sql_add_command1(state)  
        await state.finish()
        await message.answer('Зміни внесені.', reply_markup=kb_admin.button_case_admin)

async def choose_where2(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        await sqlite_db.sql_add_command2(state)  
        await state.finish()
        await message.answer('Зміни внесені.', reply_markup=kb_admin.button_case_admin)

async def choose_where3(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        await sqlite_db.sql_add_command3(state)  
        await state.finish()
        await message.answer('Зміни внесені.', reply_markup=kb_admin.button_case_admin)


# async def del_sour(message: types.Message):
#     if message.from_user.id == ID:
#         await message.answer('Что нужно удалить?', reply_markup=kb_admin.button_remove_admin)

# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
# async def del_callback_run(callback_query: types.CallbackQuery):
#     await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
#     await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удален.', show_alert=True)

# async def delete_item(message: types.Message):
#     if message.from_user.id == ID:
#         read = await sqlite_db.sql_read00()
#         for ret in read:
#             await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescriptoin: {ret[2]}\nPrice: {ret[-1]}')
#             await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
# async def del_callback_run1(callback_query: types.CallbackQuery):
#     await sqlite_db.sql_delete_command1(callback_query.data.replace('del ', ''))
#     await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удален.', show_alert=True)

# async def delete_item1(message: types.Message):
#     if message.from_user.id == ID:
#         read = await sqlite_db.sql_read01()
#         for ret in read:
#             await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescriptoin: {ret[2]}\nPrice: {ret[-1]}')
#             await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
# async def del_callback_run2(callback_query: types.CallbackQuery):
#     await sqlite_db.sql_delete_command2(callback_query.data.replace('del ', ''))
#     await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удален.', show_alert=True)

# async def delete_item2(message: types.Message):
#     if message.from_user.id == ID:
#         read = await sqlite_db.sql_read02()
#         for ret in read:
#             await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescriptoin: {ret[2]}\nPrice: {ret[-1]}')
#             await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))




def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cencel_handler, state="*", commands='Відміна')
    dp.register_message_handler(cencel_handler, Text(equals='Відміна', ignore_case=True), state="*")
    dp.register_message_handler(cm_starter, commands=["Додати"], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMDishes.photo)
    dp.register_message_handler(load_name, state=FSMDishes.name)
    dp.register_message_handler(load_description, state=FSMDishes.description)
    dp.register_message_handler(load_price, state=FSMDishes.price)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(choose_where, lambda message: 'Моктейль' in message.text)
    dp.register_message_handler(choose_where1, lambda message: 'Лимонад' in message.text)
    dp.register_message_handler(choose_where2, lambda message: 'Страва' in message.text)
    dp.register_message_handler(choose_where3, lambda message: 'Кофе' in message.text)
    dp.register_message_handler(first_wind, state="*", commands='Головне_меню')
    dp.register_message_handler(first_wind, Text(equals='Головне_меню', ignore_case=True), state="*")
    dp.register_message_handler(go_home, commands='Головне_меню')
    # dp.register_message_handler(first_wind, lambda message: 'Главное' in message.text)
    # dp.register_message_handler(del_sour, commands='Удалить')
    # dp.register_message_handler(delete_item, commands='Удалить_моктейль')
    # dp.register_message_handler(delete_item1, commands='Удалить_лимонад')
    # dp.register_message_handler(delete_item2, commands='Удалить_блюдо')