from aiogram import Router
from aiogram.types import Message
from filter.filter import AdminOnly

rt = Router()
rt.message.filter(AdminOnly())
rt.callback_query.filter(AdminOnly())

@rt.message()
async def se(message : Message):
    await message.answer(text = "admin")