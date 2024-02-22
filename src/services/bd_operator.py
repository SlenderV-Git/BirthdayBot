import sqlite3
from aiogram.fsm.context import FSMContext
from datetime import datetime, date, timedelta
from lexicon.lexicon import FSMPRESETS

def date_diff(date : str):
    return (datetime.strptime(date, '%Y-%m-%d').date() - datetime.now().date()).days

async def data_converter(state : FSMContext):
    data = await state.get_data()
    month, day = data.values()
    return {"date" : str(date(year=datetime.now().year, month=int(month), day=int(day)))}

def set_user_data(data):
    conn = sqlite3.connect("src/database/db.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS date (date DATE, name TEXT, tg_id TEXT);")
    cur.execute(f"INSERT INTO date (date, name, tg_id) VALUES (?, ?, ?)", list(data.values()))
    conn.commit()

def get_date_list(tg_id : str):
    cur = sqlite3.connect("src/database/db.db").cursor()
    cur.execute(f"SELECT date, name FROM date WHERE tg_id = {tg_id} ORDER BY date ASC")
    return '\n'.join([FSMPRESETS["see_base"].format(index + 1, row[1], row[0], date_diff(row[0])) for index, row in enumerate(cur.fetchall())])


#return '\n'.join([f"{date_diff(row[0])} дней " + ' '.join(row) for index, row in enumerate(cur.fetchall())])

    


