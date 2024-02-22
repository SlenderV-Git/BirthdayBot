from aiogram import Router
from aiogram.types import Message
from filter.filter import AdminOnly

rt = Router()
rt.message.filter(AdminOnly())
rt.callback_query.filter(AdminOnly())

