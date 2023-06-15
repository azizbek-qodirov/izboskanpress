from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from keyboards.default.menuKeys import menuKeyboard, menuKeyboard2
from loader import dp, db, checkUser, sendRegText

from states.registration import register
from aiogram.dispatcher import FSMContext

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    inDB = await checkUser(db, message)
    if inDB:
        if str(message.from_user.id) in ADMINS:
            await message.answer(f"Aссалому алайкум {message.chat.first_name} Избоскан инфо ботига хуш келибсиз! \nБотдан фойдаланиш учун қуйидаги тугмалардан фойдаланишингиз мумкин: ", reply_markup=menuKeyboard2)
        else:
            await message.answer(f"Aссалому алайкум {message.chat.first_name} Избоскан инфо ботига хуш келибсиз! \nБотдан фойдаланиш учун қуйидаги тугмалардан фойдаланишингиз мумкин: ", reply_markup=menuKeyboard)
    else:
        await register.fullName.set()
        await message.answer("Рўйхатдан ўтиш учун илтимос исм-фамилянгизни юборинг: \nМасалан: Азизбек Қодиров", reply_markup=types.ReplyKeyboardRemove())

