from aiogram import types
import xlsxwriter
from keyboards.default.cancelContact import cancelContactKey
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext
from data.config import ADMINS 
from keyboards.default.adminKeys import adminKeyboard
from states.public_message import publicMessage




publicMessageKey = types.ReplyKeyboardMarkup(keyboard=[
    [
        types.KeyboardButton(text="✔️ Ҳа"),
        types.KeyboardButton(text="✖️ Йўқ")
    ]
], resize_keyboard=True)

@dp.message_handler(text="⚙️ Админстратор менюси")
async def adminHandler(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.reply("Сиз админстраторсиз! \nҚуйидаги буйруқлардан бирини танланг:", reply_markup=adminKeyboard)

@dp.message_handler(text="📊 Статистика")
async def statsHandler(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        all_users = await db.count_users(db)
        users_day = await db.count_today_joined_users(db)
        users_month = await db.count_this_month_joined_users(db)

        msg = f"Ботдаги барча фойдаланувчилар сони: {all_users} та \n\nБугун қўшилган: {users_day} та \nБу ой қўшилган: {users_month} та"
        await message.reply(msg)

@dp.message_handler(text="❌ Бекор қилиш", state=publicMessage)
async def cancelPublicMessage(message: types.Message, state: FSMContext):
    await message.answer("Сиз админстраторсиз! \nҚуйидаги буйруқлардан бирини танланг:", reply_markup=adminKeyboard)
    await state.finish()

@dp.message_handler(text="🌐 Умумий хабар")
async def do_func(message: types.Message):
    allIDs = await db.fetch(db, "SELECT id FROM users")
    await message.answer("Юбормоқчи бўлган оммавий хабарни киритинг:", reply_markup=cancelContactKey)
    await publicMessage.message.set()

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=publicMessage.message)
async def handlePhoto(message: types.Message, state: FSMContext):
    await state.update_data({'text': message.text})
    await message.delete()
    await message.answer(f"{message.text}")
    await message.answer("Ушбу хабарингиз юборилсинми?", reply_markup=publicMessageKey)
    await publicMessage.next()

@dp.message_handler(state=publicMessage.really)
async def reallyHandle(message: types.Message, state: FSMContext):
    if message.text == "✔️ Ҳа":
        await message.answer("Хабарингиз юборилмоқда...", reply_markup=adminKeyboard)
        userids = await db.fetch(db, "SELECT id FROM users")
        data = await state.get_data()
        publicMessageText = data.get('text')
        await state.finish()
        sent = 0
        failed = 0
        for i in range(len(userids)):
            try:
                await bot.send_message(chat_id=userids[i]['id'], text=publicMessageText)
                print(userids[i]['id'])
                sent+=1
            except:
                failed += 1
        await message.answer(f"Хабарингиз {sent} та фойдаланувчига юборилди \n{failed} тасига юборилмади")

    elif message.text == "✖️ Йўқ":
        await state.finish()
        await message.answer("Юбориш бекор қилинди", reply_markup=adminKeyboard)


@dp.message_handler(text="📃 Маълумотлар")
async def xlsxWriteHandle(message: types.Message):
    users = await db.fetch(db, "SELECT * FROM users")

    workbook = xlsxwriter.Workbook("users.xlsx")
    worksheet = workbook.add_worksheet()
    headers = ["ID", "Full Name", "Phone", "Joined Date"]
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)
    
    for row_num, user in enumerate(users, 1):
        worksheet.write(row_num, 0, user["id"])
        worksheet.write(row_num, 1, user["fullname"])
        worksheet.write(row_num, 2, user["phone"])
        worksheet.write(row_num, 3, str(user["joined_date"]))
    
    workbook.close()
    await message.reply_document(types.InputFile("users.xlsx"))