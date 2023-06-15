from aiogram import types
from loader import dp
from keyboards.inline.mfys import *


@dp.callback_query_handler(lambda query: query.data == "$backSec1")
async def back(query: types.CallbackQuery):
    await query.message.edit_text(text="Қуйидаги МФЙлардан бирини танланг: ", reply_markup=sector1)

@dp.callback_query_handler(lambda query: query.data == "$backSec2")
async def back(query: types.CallbackQuery):
    await query.message.edit_text(text="Қуйидаги МФЙлардан бирини танланг: ", reply_markup=sector2)

@dp.callback_query_handler(lambda query: query.data == "$backSec3")
async def back(query: types.CallbackQuery):
    await query.message.edit_text(text="Қуйидаги МФЙлардан бирини танланг: ", reply_markup=sector3)

@dp.callback_query_handler(lambda query: query.data == "$backSec4")
async def back(query: types.CallbackQuery):
    await query.message.edit_text(text="Қуйидаги МФЙлардан бирини танланг: ", reply_markup=sector4)
