from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sectorKeys = ReplyKeyboardMarkup(keyboard=[
  [
    KeyboardButton(text="Сектор I"),
    KeyboardButton(text="Сектор II")
  ],
  [
    KeyboardButton(text="Сектор III"),
    KeyboardButton(text="Сектор IV")
  ],
  [
    KeyboardButton(text="🤖 Онлайн маҳалла бот")
  ],
  [
    KeyboardButton(text="🔙 Орқага")
  ]
], resize_keyboard=True)