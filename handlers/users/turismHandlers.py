from aiogram import types
from loader import dp, bot, db, checkUser
from keyboards.inline.turismKeys import turism1, turism2, turism3, turism4
from tourismInfos import tourismData
from keyboards.inline.backTurismKeys import *
from data.config import DEVID


@dp.callback_query_handler(lambda query: query.data=="turism1")
async def turismHandler(query: types.CallbackQuery):
  await checkUser(db, query)
  await query.message.delete()
  await query.message.answer(text="Избоскан туманида 6 та Диққатга сазовор жойлар мавжуд бўлиб, қуйидаги тугмаларни босиш орқали мана шу жойлар тўғрисида маълумотга эга бўлишингиз мумкин.", reply_markup=turism1)

@dp.callback_query_handler(lambda query: query.data=="turism2")
async def turismHandler(query: types.CallbackQuery):
  await checkUser(db, query)
  await query.message.delete()
  await query.message.answer(text="Избоскан туманида 16 та археология ёдгорликлари мавжуд бўлиб, қуйидаги тугмаларни босиш орқали мана шу жойлар тўғрисида маълумотга эга бўлишингиз мумкин.", reply_markup=turism2)

@dp.callback_query_handler(lambda query: query.data=="turism3")
async def turismHandler(query: types.CallbackQuery):
  await checkUser(db, query)
  await query.message.delete()
  query.from_user
  await query.message.answer(text="Избоскан туманида 2 та архитектура ёдгорликлари мавжуд бўлиб, қуйидаги тугмаларни босиш орқали мана шу жойлар тўғрисида маълумотга эга бўлишингиз мумкин.", reply_markup=turism3)

@dp.callback_query_handler(lambda query: query.data=="turism4")
async def turismHandler(query: types.CallbackQuery):
  await checkUser(db, query)
  await query.message.delete()
  await query.message.answer(text="Избоскан туманида 3 монументал санъат ёдгорликлари мавжуд бўлиб, қуйидаги тугмаларни босиш орқали мана шу жойлар тўғрисида маълумотга эга бўлишингиз мумкин.", reply_markup=turism4)

@dp.callback_query_handler(lambda query: query.data.startswith('!'))
async def sec1Handle(query: types.CallbackQuery):
    await checkUser(db, query)
    mfyid = query.data.split("!")[1]
    mfydata = tourismData[mfyid]

    mfyidforKeys = mfyid.split(".")[0]
    keyboard = None
    
    if mfyid in tourismData:
      if mfyidforKeys == str(1):
        keyboard = backTurism1
      elif mfyidforKeys == str(2):
          keyboard = backTurism2
      elif mfyidforKeys == str(3):
        keyboard = backTurism3
      elif mfyidforKeys == str(4):
        keyboard = backTurism4
      await query.message.delete()
      await query.message.answer_photo(photo=f"{mfydata['photo']}", caption=f"{mfydata['caption']}",  reply_markup=keyboard)

    else:
      await bot.send_message(chat_id=DEVID, text=f"The bot has an error in dictionary sightseeing places {mfyid}")
