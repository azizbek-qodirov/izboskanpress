from aiogram.dispatcher.filters.state import State, StatesGroup


class publicMessage(StatesGroup):
  message = State()
  really = State()