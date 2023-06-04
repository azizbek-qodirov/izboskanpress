from aiogram import types
from keyboards.default.menuKeys import menuKeyboard
from loader import dp

@dp.message_handler(text="🔙 Орқага")
async def backHandler(message: types.Message):
  await message.reply("Сиз асосий менюдасиз. \nБотдан фойдаланиш учун қуйидаги тугмалардан фойдаланишингиз мумкин: ", reply_markup=menuKeyboard)