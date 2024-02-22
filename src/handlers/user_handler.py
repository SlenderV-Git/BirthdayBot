from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from services.stiker_set import get_random_sticker
from services.callback_operator import get_callback_body
from services.bd_operator import set_user_data, get_date_list, data_converter
from keyboard.inline_kb import month_kb, day_kb
from FSM.models import AddBirthday
from lexicon.lexicon import FSMPRESETS
from main import bot


rt = Router()

@rt.message(CommandStart())
async def start_process(message : Message):
    await message.reply_sticker(sticker = await get_random_sticker(bot= bot))
    await message.answer(text= FSMPRESETS["start"])
    
@rt.message(Command("add"), StateFilter(None))
async def starting_add(message : Message, state : FSMContext):
    await message.answer(text= FSMPRESETS["add"],
                         reply_markup= month_kb())
    await state.set_state(AddBirthday.add_month)

@rt.callback_query(AddBirthday.add_month)
async def add_month_process(callback : CallbackQuery, state : FSMContext):
    await callback.message.edit_text(text=FSMPRESETS["add_day"],
                                     reply_markup= day_kb(month= get_callback_body(callback=callback)))
    await state.update_data(data = {"month" : get_callback_body(callback=callback)})
    await state.set_state(AddBirthday.add_day)
    
@rt.callback_query(AddBirthday.add_day)
async def add_day_process(callback : CallbackQuery, state : FSMContext):
    await callback.message.edit_text(text= FSMPRESETS["add_name"],
                                     reply_markup= None)
    await state.update_data(data = {"day" : get_callback_body(callback=callback)})
    await state.set_state(AddBirthday.add_name)
    
@rt.message(AddBirthday.add_name)
async def add_name_process(message : Message, state : FSMContext):
    date = await data_converter(state=state)
    
    await message.answer(text= FSMPRESETS["finish_add"].format(message.text, date["date"]),
                                     reply_markup= None)
    
    await state.set_data(date)
    
    await state.update_data(data = {"name" : message.text})
    await state.update_data(data = {"tg_id" : message.from_user.id})
    
    set_user_data(await state.get_data())
    
    await state.clear()
    
@rt.message(Command("see"))
async def see_date_list(message : Message):
    await message.answer(text= str(get_date_list(message.from_user.id)))
    
