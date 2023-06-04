from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainKey = ReplyKeyboardMarkup(keyboard=[
  [
    KeyboardButton(text="Сектор раҳбарлари")
  ],
  [
    KeyboardButton(text="Туман ҳокимининг ўринбосарлари")
  ],
  [
    KeyboardButton(text="🔙 Орқага")
  ]
], resize_keyboard=True)