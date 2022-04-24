import sqlite3

"""Тема таблиц вина"""
# con = sqlite3.connect('db.db')
# with con.cursor() as cursor:
#     cursor.execute('''
#         create table if not exists 'name' (
#             `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
#         )
#     ''')
# lxml строим xml из sql
# а ещё тоже самое в джанго


def sqlite_connection(func):
    def wrapper(*args, **kwargs):
        with sqlite3.connect('../db.db') as con:
            kwargs['con'] = con
            res = func(*args, **kwargs)
            con.commit()
            return res

    return wrapper


@sqlite_connection
def init_db(con: sqlite3.Connection):
    """Создаём таблицу с id, цвет,  выдержкой, сортом, винодельней, описанием вина"""
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS GRADE (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            
            DESCRIPTION TEXT,
        );
        CREATE TABLE IF NOT EXISTS Wine (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            WINE_EXTRACT INTEGER,
            SWEETNESS FOREIGN KEY ,
            COLOR FOREIGN KEY,
            GRADE FOREIGN KEY ,
            WINERY FOREIGN KEY ,
            DESCRIPTION TEXT,
        );
    """)


@sqlite_connection
def add_wine_bottle(con: sqlite3.Connection, )
