import sqlite3
from typing import Dict, List

"""Тема таблиц вина"""
# lxml строим xml из sql
# а ещё тоже самое в джанго


def sqlite_connection(func):
    def wrapper(*args, **kwargs):
        with sqlite3.connect('db.db') as con:
            kwargs['con'] = con
            res = func(*args, **kwargs)
            con.commit()
            return res
    return wrapper


@sqlite_connection
def init_db(con: sqlite3.Connection):
    """Создаём таблицу с id, цвет,  выдержкой, сортом, страной, описанием вина"""
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS WINE_GRADES (
            WINE_GRADE_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            WINE_GRADE_NAME TEXT,
            DESCRIPTION TEXT,
            COLOR TEXT
        );""")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS COUNTRIES (
            COUNTRY_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            COUNTRY_NAME TEXT
        );""")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS SWEETNESS (
            SWEETNESS_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            SWEETNESS_NAME TEXT
        );""")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS WINES (
            WINE_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            WINE_EXTRACT INTEGER,
            SWEETNESS_ID INTEGER NOT NULL,
            WINE_GRADE_ID INTEGER NOT NULL,
            COUNTRY_ID INTEGER NOT NULL,
            DESCRIPTION TEXT,
            FOREIGN KEY (SWEETNESS_ID) REFERENCES SWEETNESS(SWEETNESS_ID),
            FOREIGN KEY (WINE_GRADE_ID) REFERENCES WINE_GRADES(WINE_GRADE_ID),
            FOREIGN KEY (COUNTRY_ID) REFERENCES COUNTRIES(COUNTRY_ID)
        );""")
    cur.execute("INSERT INTO SWEETNESS (SWEETNESS_NAME) VALUES ('Сухое');")
    cur.execute("INSERT INTO SWEETNESS (SWEETNESS_NAME) VALUES ('Полусладкое');")
    cur.execute("INSERT INTO SWEETNESS (SWEETNESS_NAME) VALUES ('Сладкое');")


@sqlite_connection
def get_all_wines(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
        SELECT G.WINE_GRADE_NAME, W.WINE_EXTRACT, S.SWEETNESS_NAME, C.COUNTRY_NAME, W.DESCRIPTION FROM WINES W
        LEFT OUTER JOIN SWEETNESS S ON W.SWEETNESS_ID = S.SWEETNESS_ID
        LEFT OUTER JOIN WINE_GRADES G ON W.WINE_GRADE_ID = G.WINE_GRADE_ID
        LEFT OUTER JOIN COUNTRIES C ON C.COUNTRY_ID = W.COUNTRY_ID;
    ''')
    return cur.fetchall()


@sqlite_connection
def get_all_countries(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
            SELECT * FROM COUNTRIES;
        ''')
    return cur.fetchall()


@sqlite_connection
def get_all_sweetness(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
            SELECT * FROM SWEETNESS;
        ''')
    return cur.fetchall()


@sqlite_connection
def get_all_wine_grades(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
                SELECT * FROM WINE_GRADES;
            ''')
    return cur.fetchall()


@sqlite_connection
def add_wine_grade(con: sqlite3.Connection, name: str, descr: str, color: str):
    cur = con.cursor()
    cur.execute('''
        INSERT INTO WINE_GRADES (WINE_GRADE_NAME, DESCRIPTION, COLOR) VALUES (?, ?, ?);
    ''', (name, descr, color))


@sqlite_connection
def add_country(con: sqlite3.Connection, name: str):
    cur = con.cursor()
    cur.execute('''
        INSERT INTO COUNTRIES (COUNTRY_NAME) VALUES (?);
    ''', (name,))


def update_country(con: sqlite3.Connection, name: str, id: int):
    cur = con.cursor()
    cur.execute('''
        UPDATE COUNTRIES
        SET country_name = (?)
        WHERE COUNTRY_ID = (?)
    ''', (name, id))


def delete_country(con: sqlite3.Connection, id: int):
    cur = con.cursor()
    cur.execute('DELETE FROM COUNTRIES WHERE COUNTRY_ID = (?)', (id,))


@sqlite_connection
def add_wine(con: sqlite3.Connection, extract: int, sweetness_id: int, wine_grade_id: int, country_id: int,
             description: str):
    cur = con.cursor()
    cur.execute('''
        INSERT INTO WINES (WINE_EXTRACT, SWEETNESS_ID, WINE_GRADE_ID, COUNTRY_ID, DESCRIPTION) VALUES (?, ?, ?, ?, ?);
    ''', (extract, sweetness_id, wine_grade_id, country_id, description))


if __name__ == '__main__':
    init_db()
