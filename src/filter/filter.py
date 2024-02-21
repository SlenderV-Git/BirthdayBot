from aiogram.types import Message
from aiogram.filters import BaseFilter
from config.config import load_config

class AdminOnly(BaseFilter):
    async def __call__(self, message : Message):
        admins = load_config().admin_id.split()
        return str(message.from_user.id) in admins