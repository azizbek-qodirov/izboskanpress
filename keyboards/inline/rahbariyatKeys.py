from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rahbariyatKeys = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="I", callback_data="sec1Boss"),
        InlineKeyboardButton(text="II", callback_data="sec2Boss"),
        InlineKeyboardButton(text="III", callback_data="sec3Boss"),
        InlineKeyboardButton(text="IV", callback_data="sec4Boss"),
    ]
])

# DDG = deputy district governors
DDGKeys = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="I", callback_data="ddg1"),
        InlineKeyboardButton(text="II", callback_data="ddg2"),
        InlineKeyboardButton(text="III", callback_data="ddg3"),
        InlineKeyboardButton(text="IV", callback_data="ddg4"),
        InlineKeyboardButton(text="V", callback_data="ddg5"),
        InlineKeyboardButton(text="VI", callback_data="ddg6"),
        InlineKeyboardButton(text="VII", callback_data="ddg7"),
    ]
]) 