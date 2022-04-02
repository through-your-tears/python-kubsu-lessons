from datetime import datetime, timedelta


weeks_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
data = {}
with open('3inp.txt', 'r') as file:
    for line in file:
        row = line.split()
        if data.get(row[0]):

        else:
            data[line[0]] = {
                'visits': 1,
                ''
            }
