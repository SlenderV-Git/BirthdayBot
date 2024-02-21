from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from calendar import monthrange
import datetime

def month_kb():
    build = InlineKeyboardBuilder()
    for month in range(1, 13):
        build.add(InlineKeyboardButton(text= str(month), callback_data=f"{month}_month"))
    return build.adjust(4).as_markup()

def day_kb(month : str):
    build = InlineKeyboardBuilder()
    for day in range(1, monthrange(datetime.datetime.now().hour, int(month))[1]+1):
        build.add(InlineKeyboardButton(text = str(day), callback_data = f"{day}_day"))
    return build.adjust(7).as_markup()