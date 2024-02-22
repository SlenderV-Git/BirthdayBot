import asyncio
from aiogram import Dispatcher, Bot
from config.config import load_config
from aiogram.methods import set_my_description, set_my_name, set_chat_photo
from handlers import admin_handler, user_handler
from services.commands import set_menu_commands
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from services.news_sendler import send_message
from lexicon.lexicon import BOT_SETTING


bot = Bot(token= load_config().bot_token)

async def main():
    storage = MemoryStorage()
    
    # await bot.set_my_name(BOT_SETTING["name"])
    # await bot.set_my_description(BOT_SETTING["description"])
    
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