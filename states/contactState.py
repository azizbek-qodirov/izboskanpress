from aiogram.dispatcher.filters.state import State, StatesGroup

class contact(StatesGroup):
  fullName = State()
  location = State()
  phoneNumber = State()
  message = State()