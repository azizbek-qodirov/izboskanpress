from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

aboutRegionKeys = ReplyKeyboardMarkup(keyboard=[
  [
    KeyboardButton(text="⭕️ ИЗБОСКАН ТУМАНИ ҲАҚИДА УМУМИЙ МАЪЛУМОТ")
  ],
  [
    KeyboardButton(text="📈1. АСОСИЙ КЎРСАТКИЧЛАРИ"),
  ],
  [
    KeyboardButton(text="💈2. САНОАТ"),
    KeyboardButton(text="🔑3. ХИЗМАТЛАР"),
  ],
  [
    KeyboardButton(text="🧰4. КОРХОНАЛАР ВА ТАШКИЛОТЛАР ТАВСИФИ")
  ],
  [
    KeyboardButton(text="🏗5. ИНВEСТИЦИЯЛАР ВА ҚУРИЛИШ")
  ],
  [
    KeyboardButton(text="💰6. ИСТEЪМОЛ БОЗОРИ ВА ТАШҚИ АЛОҚАЛАР")
  ],
  [
    KeyboardButton(text="🌳7. ҚИШЛОҚ, ЎРМОН ВА БАЛИҚЧИЛИК ХЎЖАЛИГИ")
  ],
  [
    KeyboardButton(text="👨‍👩‍👧‍👦8. ДEМОГРАФИК ҲОЛАТ")
  ],
  [
    KeyboardButton(text="💵9. ЎРТАЧА ОЙЛИК НОМИНАЛ ҲИСОБЛАНГАН ИШ ҲАҚИ")
  ],
  [
    KeyboardButton(text="🔙 Орқага")
  ]
], resize_keyboard=True)