from os import path
from collections import Counter
import csv

DATA_DIR = 'tempdata'
filename = path.join(DATA_DIR, 'wrangledbabynames.csv')
search_list = ['Michael', 'Kelly', 'Kanye', 'THOR',
               'casey', 'Arya', 'ZZZblahblah']

index = {}
with open(filename, 'r') as csv_file:
    rows = csv.DictReader(csv_file)
    for row in rows:
        lower_name = row['name'].lower()
        index[lower_name] = row

def analyze_name(name):
    lower_name = name.lower()
    if lower_name in index:
        return index[lower_name]
    return {'name': name,
            'gender': 'NA',
            'ratio': None,
            'males': None,
            'females': None,
            'total': 0}

gender_counts = Counter()
female_babies_count = 0
male_babies_count = 0
for name in search_list:
    data = analyze_name(name)
    print(name, data['gender'], data['ratio'])
    gender_counts[data['gender']] += 1
    if data['females']:
        female_babies_count += int(data['females'])
    if data['males']:
        male_babies_count += int(data['males'])
print('Total:')
print(*['{}: {}'.format(gender, gender_counts[gender])
            for gender in sorted(gender_counts.keys())
       ])
print('females: {} males: {}'.format(female_babies_count, male_babies_count))
