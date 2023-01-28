import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bott.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(id TEXT PRIMARY KEY, "
               "name TEXT ,"
               "age INTEGER,"
               "groups INTEGER,"
               "dir TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES "
                       "(?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()

async def sql_command_random():
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    random_user = random.choice(result)
    return random_user


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()