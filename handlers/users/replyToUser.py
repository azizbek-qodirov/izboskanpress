from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.replyState import replyToUser
from keyboards.default.menuKeys import menuKeyboard
from keyboards.default.cancelContact import cancelContactKey


@dp.callback_query_handler(lambda query: query.data.startswith("#"))
async def handleMessage(query: types.CallbackQuery, state: FSMContext):
  userID = query.data.split('#')[1]
  
  await state.update_data({"user": userID})
  #await query.message.delete()
  await query.message.answer("Фойдаланувчи учун хабарингизни юборинг:", reply_markup=cancelContactKey)
  await replyToUser.message.set()

@dp.message_handler(text="❌ Бекор қилиш", state=replyToUser)
async def cancelHandler(message: types.Message, state: FSMContext):
  await state.finish()
  await message.reply("Хабар юбориш бекор қилинди", reply_markup=menuKeyboard)


@dp.message_handler(state=replyToUser.message)
async def sendMessage(message: types.Message, state: FSMContext):
  data = await state.get_data("user")
  userID = data.get('user')
  await bot.send_message(chat_id=userID, text=f"Aдминстратор хабарингизга жавоб берди: \n\n{message.text}")
  await message.answer("✅ Хабарингиз фойдаланувчига юборилди",reply_markup=menuKeyboard)
  await state.finish()