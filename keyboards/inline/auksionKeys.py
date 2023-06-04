from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

auksionKey = InlineKeyboardMarkup(inline_keyboard=[
  [
    InlineKeyboardButton(text="Умумий савдо платформасини силкаси", url="https://e-auksion.uz/home"),
  ],
  [
    InlineKeyboardButton(text="Давлат мулкини ижарага бериш", url="https://e-auksion.uz/lots?group=11&index=1&page=1&lt=0&at=0&order=0&region=7&q=&area=99"),
  ],
  [
    InlineKeyboardButton(text="Деҳқон хўжалиги ерлар ижараси", url="https://e-auksion.uz/lots?group=24&index=1&page=1&lt=0&at=0&order=0&region=7&area=99&q=")
  ],
  [
    InlineKeyboardButton(text="Давлат активлари", url="https://e-auksion.uz/lots?group=5&index=1&page=1&lt=0&at=0&order=0&region=7&area=99"),
    InlineKeyboardButton(text="Кўчмас мулк", url="https://e-auksion.uz/lots?group=1&index=1&page=1&lt=0&at=0&order=0&region=7&area=99"),
  ],
  [
    InlineKeyboardButton(text="Ер участкалари", url="https://e-auksion.uz/lots?group=6&index=1&page=1&lt=0&at=0&order=0&region=7&area=99&q="),
    InlineKeyboardButton(text="Кўчма савдо жойлари", url="https://e-auksion.uz/lots?group=23&category=86&index=1&page=1&lt=0&at=0&order=0&q=&region=7&area=99")
  ],
  [
      InlineKeyboardButton(text="Auksion video", url="https://t.me/auksionvideo"),
      InlineKeyboardButton(text="OnlineAuksionUz", url="https://t.me/onlineauksionuz")
  ]
])