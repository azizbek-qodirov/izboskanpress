from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.inline.registrationKey import regKey

from data import config
from utils.db_api.database import DatabaseManager
db = DatabaseManager

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def checkUser(db, messageORquery):
  inDB = await db.check_user_exists(db, messageORquery.from_user.id)
  return inDB

async def sendRegText(message):
  await message.answer("Сиз рўйхатдан ўтмагансиз. \nБотдан фойдаланиш учун қуйидаги тугма орқали аввал рўйхатдан ўтинг ва старт тугмасини босинг:", reply_markup=regKey)
