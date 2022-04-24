import sqlite3

from adapter import export_to_file
from db import sqlite_connection

PATH = 'wines.xml'


@sqlite_connection
def sql_to_xml(con: sqlite3.Connection):
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from wines;")
    rows = [dict(row) for row in cur.fetchall()]
    export_to_file(rows, PATH)


sql_to_xml()
