from loader import dp, bot, db, checkUser
from keyboards.inline.contactAdminKey import contactAdmin
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.contactState import contact
from states.replyState import replyToUser
from keyboards.default.phoneShare import shareNumber
from keyboards.default.cancelContact import cancelContactKey
from keyboards.default.menuKeys import menuKeyboard, menuKeyboard2
from data.config import ADMINS


mergedkeys = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
btn1 =  types.KeyboardButton(text="❌ Бекор қилиш")
btn2 =  types.KeyboardButton(text="📞 Телефон рақамини юбориш:", request_contact=True)
mergedkeys.add(btn2, btn1)

@dp.message_handler(text="❌ Бекор қилиш", state=contact)
async def cancelHandler(message: types.Message, state: FSMContext):
  await state.finish()
  if str(message.from_user.id) in ADMINS:
    await message.reply("Мурожаат юбориш бекор қилинди", reply_markup=menuKeyboard2)
  else:
    await message.reply("Мурожаат юбориш бекор қилинди", reply_markup=menuKeyboard)


@dp.callback_query_handler(lambda query: query.data=="$contactAdmin")
async def handleContactInfo(query: types.CallbackQuery, state: FSMContext):
  await query.message.delete()
  await query.message.answer("Мурожаатингизни йўлланг:", reply_markup=cancelContactKey)
  await contact.message.set()

@dp.message_handler(state=contact.message)
async def messageHandler(message: types.Message, state: FSMContext):
  UserID = message.from_user.id
  await state.update_data({"message": message.text})
  if str(UserID) in ADMINS:
    await message.reply("✅ Мурожаатингиз админстраторга юборилди!", reply_markup=menuKeyboard2)
  else:
    await message.reply("✅ Мурожаатингиз админстраторга юборилди!", reply_markup=menuKeyboard)
  data = await state.get_data()

  message_text = data.get('message')
  answerKey = types.InlineKeyboardMarkup()
  key1 = types.InlineKeyboardButton(text="Хабар юбориш", callback_data=f"#{UserID}")
  answerKey.add(key1)

  targetUser = await db.get_user(db, UserID)
  template = f"#Янги мурожаат \n\nИсми: {targetUser['fullname']} \nТелефон рақами: {targetUser['phone']} \nХабар: {message_text}"
  await state.finish()
  for admin in ADMINS:
    await bot.send_message(chat_id=admin, text=template, reply_markup=answerKey)