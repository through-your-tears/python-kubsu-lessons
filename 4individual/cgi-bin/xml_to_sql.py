import cgitb
import sqlite3

from adapter import import_from_file
from db import init_db, sqlite_connection

PATH = 'wines.xml'

cgitb.enable()
init_db()


@sqlite_connection
def xml_to_sql(con: sqlite3.Connection):
    rows = import_from_file(PATH)
    ins = []
    for row in rows:
        a = []
        for value in row.values():
            try:
                a.append(int(value))
            except ValueError:
                a.append(value)
        ins.append(a)
    print("Content-type: text/html")
    print(f'''
            <!DOCTYPE html>
            <html lang="ru">
                <head>
                    <title>БД</title>
                    <meta charset="UTF-8">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                </head>
                <body>
                    <ul>''')
    for row in ins:
        print(f'<li>{row}</li>')
    print('''
        </ul>
        </body>
        </html>
    
    ''')
    # con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.executemany("""
        INSERT INTO WINES (WINE_ID, WINE_EXTRACT, SWEETNESS_ID, WINE_GRADE_ID, COUNTRY_ID, DESCRIPTION) VALUES (?, ?, ?, ?, ?, ?);
    """, ins)


xml_to_sql()
