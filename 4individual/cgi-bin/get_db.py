import cgitb

from db import get_all_wines, get_all_countries, get_all_sweetness, get_all_wine_grades

cgitb.enable()

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
                <h1> Список стран </h1>
                <ul>
                        ''')
try:
    for row in get_all_countries():
        print(f'<li>{row}</li>')
    print('''
                    </ul>
                    <h1> Список по сладости </h1>
                    <ul>''')
    for row in get_all_sweetness():
        print(f'<li>{row}</li>')
    print('''
                    </ul>
                    <h1> Список сортов </h1>
                    <ul>''')
    for row in get_all_wine_grades():
        print(f'<li>{row}</li>')
    print('''
                    </ul>
                    <h1> Список вина </h1>
                    <ul>''')
    for row in get_all_wines():
        print(f'<li>{row}</li>')
except Exception:
    pass
    print('''

                    </ul>
                <form action="../cgi-bin/sql_to_xml.py">
                    <input type="submit" class="btn btn-success" value="Сгенерировать отчёт по вину в xml">
                </form>
                <form action="../cgi-bin/xml_to_sql.py">
                    <input type="submit" class="btn btn-success" value="Создать БД из xml">
                </form>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
            </body>
        </html>
        ''')

