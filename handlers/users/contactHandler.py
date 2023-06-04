from loader import dp, bot
from keyboards.inline.contactAdminKey import contactAdmin
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.contactState import contact
from states.replyState import replyToUser
from keyboards.default.phoneShare import shareNumber
from keyboards.default.cancelContact import cancelContactKey
from keyboards.default.menuKeys import menuKeyboard
from data.config import ADMINS


mergedkeys = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
btn1 =  types.KeyboardButton(text="❌ Бекор қилиш")
btn2 =  types.KeyboardButton(text="📞 Телефон рақамини юбориш:", request_contact=True)
mergedkeys.add(btn2, btn1)

@dp.message_handler(text="❌ Бекор қилиш", state=contact)
async def cancelHandler(message: types.Message, state: FSMContext):
  await state.finish()
  await message.reply("Мурожаат юбориш бекор қилинди", reply_markup=menuKeyboard)

@dp.callback_query_handler(lambda query: query.data=="$contactAdmin")
async def handleContactInfo(query: types.CallbackQuery, state: FSMContext):
  await query.message.delete()
  await query.message.answer("Ўзингизни таништиринг. \nИсм фамилянгизни юборинг:", reply_markup=cancelContactKey)
  await contact.fullName.set()

@dp.message_handler(state=contact.fullName)
async def fullNameHandle(message: types.Message, state: FSMContext):
  checkName =  message.text.split()
  replacedName = message.text.replace(" ", '')

  if len(checkName) == 2 and replacedName.isalpha():
    await state.update_data({"name": message.text})
    await contact.next()
    await message.reply("Манзилингизни юборинг:", reply_markup=cancelContactKey)
  else:
    await message.reply("Илтимос исм ва фамилянгизни тўғри форматда юборинг:", reply_markup=cancelContactKey)

@dp.message_handler(state=contact.location)
async def locationHandler(message: types.Message, state: FSMContext):
  await state.update_data({"location": message.text})
  await contact.next()
  await message.reply("Қуйидаги тугма орқали телефон рақамингизни юборинг:", reply_markup=mergedkeys)

@dp.message_handler(content_types=types.ContentTypes.CONTACT ,state=contact.phoneNumber)
async def phoneHandler(message: types.Message, state: FSMContext):
  await state.update_data({"phone": message.contact.phone_number})
  await state.update_data({"id": message.contact.user_id})
  await contact.next()
  await message.reply("Мурожаатингизни йўлланг:", reply_markup=cancelContactKey)

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=contact.phoneNumber)
async def phoneHandler(message: types.Message, state: FSMContext):
  await message.reply("Қуйидаги тугма орқали телефон рақамингизни юборинг:", reply_markup=mergedkeys)

@dp.message_handler(state=contact.message)
async def messageHandler(message: types.Message, state: FSMContext):
  await state.update_data({"message": message.text})
  await message.reply("✅ Мурожаатингиз админстраторга юборилди!", reply_markup=menuKeyboard)
  data = await state.get_data()
  print(data)

  name = data.get('name')
  location = data.get('location')
  phone = data.get('phone')
  message = data.get('message')
  user_id = data.get('id')
  answerKey = types.InlineKeyboardMarkup()
  key1 = types.InlineKeyboardButton(text="Хабар юбориш", callback_data=f"#{user_id}")
  answerKey.add(key1)

  template = f"#Янги мурожаат \n\nИсми: {name} \nМанзили: {location} \nТелефон рақами: {phone} \nХабар: {message}"
  await state.finish()
  for admin in ADMINS:
    await bot.send_message(chat_id=admin, text=template, reply_markup=answerKey)