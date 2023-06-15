from aiogram.dispatcher.filters.state import State, StatesGroup

class register(StatesGroup):
  fullName = State()
  phoneNumber = State()