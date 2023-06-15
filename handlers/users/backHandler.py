from aiogram import types
from data.config import ADMINS
from keyboards.default.menuKeys import menuKeyboard, menuKeyboard2
from loader import dp, db, checkUser, sendRegText

@dp.message_handler(text="🔙 Орқага")
async def backHandler(message: types.Message):
  inDB = await checkUser(db, message)

  if str(message.from_user.id) in ADMINS:
    await message.reply("Сиз асосий менюдасиз. \nБотдан фойдаланиш учун қуйидаги тугмалардан фойдаланишингиз мумкин: ", reply_markup=menuKeyboard2)
  else:
    if inDB:
      await message.reply("Сиз асосий менюдасиз. \nБотдан фойдаланиш учун қуйидаги тугмалардан фойдаланишингиз мумкин: ", reply_markup=menuKeyboard)
    else:
      await sendRegText(message)