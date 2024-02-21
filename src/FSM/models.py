from aiogram.fsm.state import StatesGroup, State

class AddBirthday(StatesGroup):
    add_month = State()
    add_day = State()
    add_name = State()