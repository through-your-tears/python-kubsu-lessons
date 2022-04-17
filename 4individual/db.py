import sqlite3


# con = sqlite3.connect('db.db')
# with con.cursor() as cursor:
#     cursor.execute('''
#         create table if not exists 'name' (
#             `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
#         )
#     ''')

def sqlite_connection(func):
    def wrapper(*args, **kwargs):
        with sqlite3.connect('db.db') as con:
            kwargs['con'] = con
            res = func(*args, **kwargs)
            return res

    return wrapper

