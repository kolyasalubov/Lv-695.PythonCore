from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot
from aiogram.dispatcher import Dispatcher

bot = Bot(token='') 
dp = Dispatcher(bot, storage=MemoryStorage())