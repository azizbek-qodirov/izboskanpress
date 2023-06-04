from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shareNumber = ReplyKeyboardMarkup(keyboard=[
  [
    KeyboardButton(text="📞 Телефон рақамини юбориш:", request_contact=True)
  ]
], resize_keyboard=True)