from aiogram.types import CallbackQuery
import re

def get_callback_body(callback : CallbackQuery):
    return re.findall(r'\d+', callback.data)[0]