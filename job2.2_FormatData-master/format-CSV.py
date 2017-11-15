# Определить 3 наиболее частых преступления за 2015год
import csv
a = {}  # 'тип': количество
with open('Crimes.csv') as f:
    table = csv.DictReader(f)
    for row in table:
        if '/2015' in row['Date']:
            a[row['Primary Type']] = a.get(row['Primary Type'], 0) + 1
print ('{}, {}, {}'.format(*sorted(a.items(), key=lambda x: x[1], reverse=True)))
