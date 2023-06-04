from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

turismKeys = InlineKeyboardMarkup(inline_keyboard=[
  [
    InlineKeyboardButton(text="Диққатга сазовор жойлар", callback_data="turism1"),
  ],
  [
    InlineKeyboardButton(text="Aрхеология ёдгорликлари", callback_data="turism2"),
  ],
  [
    InlineKeyboardButton(text="Aрхитектура ёдгорликлари", callback_data="turism3"),
  ],
  [
    InlineKeyboardButton(text="Монументал санъат ёдгорликлари", callback_data="turism4"),
  ],
])

turism1Keys = [
  InlineKeyboardButton(text='ОҚ МОЗОР ОТА ЗИЁРАТГОҲИ', callback_data="!1.1"),
  InlineKeyboardButton(text='ОЙЖАМОЛ ЗИЁРАТГОХИ', callback_data="!1.2"),
  InlineKeyboardButton(text='ЯКАТУТ АЗИЗЛАРИ ЗИЁРАТГОҲИ', callback_data="!1.3"),
  InlineKeyboardButton(text='ПОЙТУГ АЗИЗ МОЗОРИ', callback_data="!1.4"),
  InlineKeyboardButton(text='ХЎЖАҚАМБАР ОТА ЗИЁРАТГОҲИ', callback_data="!1.5"),
  InlineKeyboardButton(text='ИЛАМИШ ОТА', callback_data="!1.6"),
  InlineKeyboardButton(text="🔙 Орқага", callback_data="backturism")
]

turism2Keys = [
  InlineKeyboardButton(text='МАНДАКТЕПА', callback_data="!2.1"),
  InlineKeyboardButton(text='ЭЛАТАН ШАХРИСТОНИ', callback_data="!2.2"),
  InlineKeyboardButton(text='ДАЛА ТЕПА', callback_data="!2.3"),
  InlineKeyboardButton(text='МУНКИ ТЕПА', callback_data="!2.4"),
  InlineKeyboardButton(text='КИНДИК ТЕПА', callback_data="!2.5"),
  InlineKeyboardButton(text='ЖИЙДАМОЗОР ТЕПА', callback_data="!2.6"),
  InlineKeyboardButton(text='ҚАШҚАР МОЗОР', callback_data="!2.7"),
  InlineKeyboardButton(text='СУМАЛАНГАН ТЕПАЛИГИ', callback_data="!2.8"),
  InlineKeyboardButton(text='ШАЙХ МОЗОР', callback_data="!2.9"),
  InlineKeyboardButton(text='ЯНГИЗАМОНТЕПА', callback_data="!2.10"),
  InlineKeyboardButton(text='ТЎРАХОН МАСЖИДИ', callback_data="!2.11"),
  InlineKeyboardButton(text='КИНДИКТЕПА', callback_data="!2.12"),
  InlineKeyboardButton(text='ЭСКИ МОЗОРТЕПА', callback_data="!2.13"),
  InlineKeyboardButton(text='ТЎРТКЎЛТЕПА 2', callback_data="!2.14"),
  InlineKeyboardButton(text='БОТИРОБОД ТЕПА', callback_data="!2.15"),
  InlineKeyboardButton(text='ЛЎҒУМБЕК ТЕПА', callback_data="!2.16"),
  InlineKeyboardButton(text="🔙 Орқага", callback_data="backturism")
]

turism3Keys = [
  InlineKeyboardButton(text='ЖОНОБОД МАСЖИДИ', callback_data="!3.1"),
  InlineKeyboardButton(text='ОТАЛАР ЧОЙХОНАСИ', callback_data="!3.2"),
  InlineKeyboardButton(text="🔙 Орқага", callback_data="backturism"),
]

turism4Keys = [
  InlineKeyboardButton(text='НОМАЪЛУМ ЖАНГЧИ', callback_data="!4.1"),
  InlineKeyboardButton(text='НОМАЪЛУМ ЖАНГЧИ', callback_data="!4.2"),
  InlineKeyboardButton(text='АЛЛОМАЛАР ХИЁБОНИ', callback_data="!4.3"),
  InlineKeyboardButton(text="🔙 Орқага", callback_data="backturism")
]

turism1 = InlineKeyboardMarkup(row_width=1)
turism2 = InlineKeyboardMarkup(row_width=2)
turism3 = InlineKeyboardMarkup(row_width=1)
turism4 = InlineKeyboardMarkup(row_width=1)

turism1.add(*turism1Keys)
turism2.add(*turism2Keys)
turism3.add(*turism3Keys)
turism4.add(*turism4Keys)