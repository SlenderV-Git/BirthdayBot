import asyncio
from aiogram import Dispatcher, Bot
from config.config import load_config
from aiogram.types import Message, BotDescription, BotName
from handlers import admin_handler, user_handler
from services.commands import set_menu_commands
from aiogram.fsm.storage.memory import MemoryStorage
from services.stiker_set import get_random_sticker
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from services.news_sendler import send_message
from datetime import datetime, timedelta


bot = Bot(token= load_config().bot_token)

async def main():
    storage = MemoryStorage()
    
    scheduler = AsyncIOScheduler(timezone ="Europe/Moscow")
    scheduler.add_job(send_message, trigger="interval", seconds = 60, kwargs={"bot" : bot, "id" : 1544965726})
    scheduler.start()
    
    dp = Dispatcher(storage=storage)
    
    dp.include_router(admin_handler.rt)
    dp.include_router(user_handler.rt)
    
    
    await set_menu_commands(bot= bot)
    
    await bot.delete_webhook()
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())