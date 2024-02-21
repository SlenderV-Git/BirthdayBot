from random import choice
from aiogram import Bot
from config.config import load_config

async def get_random_sticker(bot : Bot):
    stiker_set = await bot.get_sticker_set(load_config().name_pack)
    return choice([sticker.file_id for sticker in stiker_set.stickers])