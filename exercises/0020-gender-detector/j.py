from os import path
from collections import defaultdict, Counter
import csv

START_YEAR = 1950
END_YEAR = 2014
INTERVAL = 10
DATA_DIR = 'tempdata'
WRANGLED_HEADERS = ['name', 'gender', 'ratio', 'females', 'males', 'total']
wrangled_filename = path.join(DATA_DIR, 'wrangledbabynames.csv')

name_counts = defaultdict(Counter)
for year in list(range(START_YEAR, END_YEAR, INTERVAL)) + [END_YEAR]:
    filename = path.join(DATA_DIR, 'yob{}.txt'.format(year))
    print('Parsing', filename)
    with open(filename, 'r') as year_file:
        for line in year_file:
            name, gender, count = line.split(',')
            name_counts[name][gender] += int(count)

wrangled_rows = []
for name, counts in name_counts.items():
    name_row= {}
    name_row['name'] = name
    name_row['females'] = counts['F']
    name_row['males'] = counts['M']
    name_row['total'] = sum(counts.values())
    if name_row['females'] >= name_row['males']:
        name_row['gender'] = 'F'
        name_row['ratio'] = round(100 * name_row['females'] / name_row['total'])
    else:
        name_row['gender'] = 'M'
        name_row['ratio'] = round(100 * name_row['males'] / name_row['total'])
    wrangled_rows.append(name_row)
wrangled_rows.sort(key=lambda r: (-r['total'], r['name']))

with open(wrangled_filename, 'w') as write_file:
    csv_out = csv.DictWriter(write_file, fieldnames=WRANGLED_HEADERS)
    csv_out.writeheader()
    csv_out.writerows(wrangled_rows)

with open(wrangled_filename, 'r') as final_file:
    for i in range(5):
        print(final_file.readline().strip())
