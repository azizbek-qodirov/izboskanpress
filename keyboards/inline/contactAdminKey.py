from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

contactAdmin = InlineKeyboardMarkup(inline_keyboard=[
  [
    InlineKeyboardButton(text="Aдмин билан боғланиш", callback_data="$contactAdmin")   
  ]
])