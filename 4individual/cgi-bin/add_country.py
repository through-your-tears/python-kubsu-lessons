import cgi
import cgitb
import codecs
import html
import sys

from db import add_country

cgitb.enable()

form = cgi.FieldStorage()

country_name = html.escape(form.getvalue('field-countryname'))

add_country(name=country_name)

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
                <h1> Страна {country_name} успешно добавлена </h1>
            </body>
        </html>
''')
