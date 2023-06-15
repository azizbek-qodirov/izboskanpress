from aiogram import types
import datetime
from data.config import ADMINS
from states.registration import register
from aiogram.dispatcher import FSMContext
from loader import dp, db, bot
from keyboards.default.phoneShare import shareNumber
from keyboards.default.menuKeys import menuKeyboard,  menuKeyboard2

@dp.message_handler(state=register.fullName)
async def handleName(message: types.Message, state: FSMContext):
    checkName =  message.text.split()
    replacedName = message.text.replace(" ", '')

    if len(checkName) == 2 and replacedName.isalpha():
        await state.update_data({"name": message.text})
        await message.answer("Қуйидаги тугма орқали телефон рақамингизни юборинг:", reply_markup=shareNumber)
        await register.next()
    else:
        await message.reply("Илтимос исм ва фамилянгизни тўғри форматда юборинг:")

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=register.phoneNumber)
async def phoneHandler(message: types.Message):
    await message.reply("Қуйидаги тугма орқали телефон рақамингизни юборинг:")

@dp.message_handler(content_types=types.ContentTypes.CONTACT ,state=register.phoneNumber)
async def phoneHandler(message: types.Message, state: FSMContext):
    userID = message.from_user.id    
    await state.update_data({"phone": message.contact.phone_number})
    usersCount = await db.count_users(db)

    data = await state.get_data()
    name = data.get('name')
    phone = data.get('phone')
    current_date = datetime.date.today()

    await db.add_user(db, userID, name, phone, current_date)
    if str(message.from_user.id) in ADMINS:
        await message.answer(f"Aссалому алайкум {name} Избоскан инфо ботига хуш келибсиз! \nБотдан фойдаланиш учун қуйидаги тугмалардан фойдаланишингиз мумкин: ", reply_markup=menuKeyboard2)
    else:
        await message.answer(f"Aссалому алайкум {name} Избоскан инфо ботига хуш келибсиз! \nБотдан фойдаланиш учун қуйидаги тугмалардан фойдаланишингиз мумкин: ", reply_markup=menuKeyboard)
    await state.finish()
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text=f"Янги фойдаланувчи қўшилди!!! \nБарча фойдаланувчилар сони : {usersCount} та")