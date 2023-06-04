from aiogram import types
from loader import dp
from keyboards.inline.turismKeys import turismKeys

@dp.callback_query_handler(lambda query: query.data=="backturism")
async def backTurism(query: types.CallbackQuery):
  await query.message.edit_text("Избосканинг туризм салоҳиятидан бохабармисиз? \n\nХабарингиз бўлмаса, ушбу маълумотлар айнан Сизлар учун!", reply_markup=turismKeys)