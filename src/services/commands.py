from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.lexicon import command_menu

async def set_menu_commands(bot : Bot):
    await bot.set_my_commands([BotCommand(command=item[0], description=item[1]) for item in command_menu.items()])