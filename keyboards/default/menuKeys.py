from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton


menuKeyboard = ReplyKeyboardMarkup(keyboard=[
  [
    KeyboardButton(text="🌏 Туман ҳақида"),
    KeyboardButton(text="🏛 Раҳбарият"),
    KeyboardButton(text="🏘 МФЙлар ҳақида"),
  ],
  [
    KeyboardButton(text="🗒 Бўш иш ўринлари"),
    KeyboardButton(text='📝 "E-auksion"'),
    KeyboardButton(text="🛩 Туман туризми"),
  ],
  [
    KeyboardButton(text="☎️ Биз билан боғланиш"),
  ]
], resize_keyboard=True)

menuKeyboard2 = ReplyKeyboardMarkup([
  [
    KeyboardButton(text="🌏 Туман ҳақида"),
    KeyboardButton(text="🏛 Раҳбарият"),
    KeyboardButton(text="🏘 МФЙлар ҳақида"),
  ],
  [
    KeyboardButton(text="🗒 Бўш иш ўринлари"),
    KeyboardButton(text='📝 "E-auksion"'),
    KeyboardButton(text="🛩 Туман туризми"),
  ],
  [
    KeyboardButton(text="☎️ Биз билан боғланиш"),
  ],
  [
    KeyboardButton(text="⚙️ Админстратор менюси")
  ]
], resize_keyboard=True)