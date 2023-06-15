from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton

adminKeyboard = ReplyKeyboardMarkup(keyboard=[
  [
    KeyboardButton(text="📊 Статистика"),
    KeyboardButton(text="📃 Маълумотлар"),
  ],
  [
    KeyboardButton(text="🌐 Умумий хабар"),
  ],
  [
    KeyboardButton(text="🔙 Орқага"),
  ]
], resize_keyboard=True)