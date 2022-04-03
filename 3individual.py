from datetime import datetime, timedelta


TIME_FORMAT = '%H:%M:%S'


def get_prime_time(visits_time):
    times = {}
    for i in range(len(visits_time)):
        counter0 = 0
        counter1 = 0
        for j in range(len(visits_time)):
            if i == j:
                continue
            if visits_time[i] < visits_time[j] < visits_time[i] + timedelta(hours=1):
                counter0 += 1
            elif visits_time[i] > visits_time[j] > visits_time[i] - timedelta(hours=1):
                counter1 += 1
        if counter0 > counter1:
            times[f'''{visits_time[i].strftime(TIME_FORMAT)} - {(visits_time[i] + 
            timedelta(hours=1)).strftime(TIME_FORMAT)}'''] = counter0
        else:
            times[f'''{(visits_time[i] - 
                        timedelta(hours=1)).strftime(TIME_FORMAT)} - {visits_time[i].strftime(TIME_FORMAT)}'''] = counter1
    return max(times, key=times.get)


def main():
    with open('3inp.txt', 'r') as file:
        fdata = [x[:-1].split() for x in file]
    visits_time = [datetime.strptime(x[1], TIME_FORMAT) for x in fdata]
    data = {}
    for row in fdata:
        if data.get(row[0]):
            data[row[0]]['visits'] += 1
            data[row[0]]['time'].append(datetime.strptime(row[1], TIME_FORMAT))
            data[row[0]]['days'].append(row[2])
        else:
            data[row[0]] = {
                'visits': 1,
                'time': [datetime.strptime(row[1], TIME_FORMAT)],
                'days': [row[2]]
            }
    fdata = []
    for key in data:
        fdata.append(f'''ip: {key}, visits: {data[key]["visits"]}, most popular day: {max(data[key]["days"], 
                     key=data[key]["days"].count)}, most popular time: {get_prime_time(data[key]['time'])}\n''')
    fdata.append(f'most popular time: {get_prime_time(visits_time)}')
    with open('3ans.txt', 'w') as file:
        file.writelines(fdata, )


if __name__ == '__main__':
    main()
