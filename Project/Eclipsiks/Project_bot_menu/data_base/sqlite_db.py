import sqlite3 as sq
from create_bot import dp, bot

def sql_start():
    global base, cur
    base = sq.connect('moco_menu.db')
    cur = base.cursor()
    if base:
        print("Data base connected OK!")
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS lemomenu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS dishmenu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS kofemenu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_add_command1(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO lemomenu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_add_command2(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO dishmenu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()
    
async def sql_add_command3(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO kofemenu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\nОпис: \n{ret[2]}\n\nЦіна: {ret[-1]}uah')

async def sql_read1(message):
    for ret in cur.execute('SELECT * FROM lemomenu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\nОпис: \n{ret[2]}\n\nЦіна: {ret[-1]}uah')

async def sql_read2(message):
    for ret in cur.execute('SELECT * FROM dishmenu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\nОпис: \n{ret[2]}\n\nЦіна: {ret[-1]}uah')

async def sql_read3(message):
    for ret in cur.execute('SELECT * FROM kofemenu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n\nОпис: \n{ret[2]}\n\nЦіна: {ret[-1]}uah')

# async def sql_read00():
#     return cur.execute('SELECT * FROM menu').fetchall()

# async def sql_delete_command(data):
#     cur.execute('DELETE FROM menu WHERE name == ?', (data,))
#     base.commit()

# async def sql_read01():
#     return cur.execute('SELECT * FROM lemomenu').fetchall()

# async def sql_delete_command1(data):
#     cur.execute('DELETE FROM lemomenu WHERE name == ?', (data,))
#     base.commit()

# async def sql_read02():
#     return cur.execute('SELECT * FROM dishmenu').fetchall()

# async def sql_delete_command2(data):
#     cur.execute('DELETE FROM dishmenu WHERE name == ?', (data,))
#     base.commit()
