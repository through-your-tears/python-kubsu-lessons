import csv


FIRST_PATH = '16.csv'
SECOND_PATH = '6.csv'


def main():
    with open(FIRST_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data_second = list(reader)
    with open(SECOND_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data_first = list(reader)

    answers = {}

    for row in data_first:
        mark = row["Оценка/10,00"]
        mark = mark.replace(',', '.')
        if mark == '-':
            if answers.get(row["Адрес электронной почты"]):
                answers[row["Адрес электронной почты"]]['Даты повторных попыток'].append(row["Тест начат"][:-7])
        elif float(mark) < 6:
            if answers.get(row["Адрес электронной почты"]):
                answers[row["Адрес электронной почты"]]['Даты повторных попыток'].append(row["Тест начат"][:-7])
            else:
                answers[row["Адрес электронной почты"]] = {
                    'Даты повторных попыток': [row["Тест начат"][:-7]]
                }
                answers[row["Адрес электронной почты"]] |= row
                answers[row["Адрес электронной почты"]].pop("Адрес электронной почты")

    for row in data_second:
        mark = row["Оценка/100,00"]
        mark = mark.replace(',', '.')
        if mark == '-':
            if answers.get(row["Адрес электронной почты"]):
                answers[row["Адрес электронной почты"]]['Даты повторных попыток'].append(row["Тест начат"][:-7])
        elif float(mark) < 60:
            if answers.get(row["Адрес электронной почты"]):
                answers[row["Адрес электронной почты"]]['Даты повторных попыток'].append(row["Тест начат"][:-7])
            else:
                answers[row["Адрес электронной почты"]] = {
                    'Даты повторных попыток': [row["Тест начат"][:-7]]
                }
                answers[row["Адрес электронной почты"]] |= row
                answers[row["Адрес электронной почты"]].pop("Адрес электронной почты")

    print(answers)


if __name__ == '__main__':
    main()
