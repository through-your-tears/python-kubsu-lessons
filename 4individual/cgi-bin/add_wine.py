import cgi
import cgitb
import html

from db import get_all_countries, get_all_sweetness, get_all_wine_grades, add_wine

cgitb.enable()

form = cgi.FieldStorage()
print("Content-type: text/html")
print(f'''
            <!DOCTYPE html>
            <html lang="ru">
                <head>
                    <title>Добавить вино</title>
                    <meta charset="UTF-8">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                </head>
                <body>
''')
if form:
    num = form.getvalue('number')
    sweetness = form.getvalue('sweetness')
    grade = form.getvalue('grade')
    descr = html.escape(form.getvalue('descr'))
    country = form.getvalue('country')

    add_wine(
        extract=num,
        sweetness_id=sweetness,
        wine_grade_id=grade,
        country_id=country,
        description=descr
    )
    print('''<h1>Вино добавлено </h1>''')

print('''
                <h1> Добавить вино </h1>
                <form>
                    <label> Выдержка в годах
                    <input type="number" name="number"> 
                    </label><br>
                    <label> Выбрать сладость 
                    <select name="sweetness">
                            ''')
for row in get_all_sweetness():
    print(f'<option value="{row[0]}">{row[1]}</option>')
print('''
                    </select>
                    </label><br>
                    <label> Выбрать сорт
                    <select name="grade">
                            ''')
for row in get_all_wine_grades():
    print(f'<option value="{row[0]}">{row[1]}</option>')
print('''
                    </select>
                    </label><br>
                    <label> Выбрать страну 
                    <select name="country">
                            ''')
for row in get_all_countries():
    print(f'<option value="{row[0]}">{row[1]}</option>')
print('''
                    </select>
                    </label><br>
                    <label> Описание
                    <textarea name="descr"></textarea>
                    </label><br>
                    <input class="btn btn-success" type="submit">
                    </form>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
                </body>
            </html>
            ''')

