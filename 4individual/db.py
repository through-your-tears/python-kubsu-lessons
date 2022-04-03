import sqlite3


con = sqlite3.connect('db.db')
with con.cursor() as cursor:
    cursor.execute('''
        create table if not exists 'name' (
            `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
        )
    ''')
