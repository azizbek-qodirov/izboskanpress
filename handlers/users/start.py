from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeys import menuKeyboard
from loader import dp, bot
from data.config import DEVID

allStarts = 0
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
  global allStarts
  allStarts = allStarts + 1
  await bot.send_message(chat_id=DEVID, text=f"All starts count: {allStarts}")
  await message.answer(f"Aссалому алайкум {message.chat.first_name} Избоскан инфо ботига хуш келибсиз! \nБотдан фойдаланиш учун қуйидаги тугмалардан фойдаланишингиз мумкин: ", reply_markup=menuKeyboard)
