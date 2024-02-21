from aiogram import Bot
from datetime import datetime
import sqlite3

async def send_message(bot : Bot, id : str):
    conn = sqlite3.connect("src/database/db.db")
    cur = conn.cursor()
    result = cur.execute(f"SELECT tg_id, name FROM date WHERE julianday(date) - julianday('now') <= 1")
    
    for id, name in cur.fetchall():
        await bot.send_message(chat_id=id, text=f"Дорогой пользователь, завтра у вашего друга {name} день рождения. Не забудьте поздравить!")
        
    cur.execute(f"DELETE FROM date WHERE julianday(date) - julianday('now') <= 1")
    conn.commit()