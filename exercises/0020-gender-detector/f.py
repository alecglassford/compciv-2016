from os import path
from collections import defaultdict, Counter

START_YEAR = 1950
END_YEAR = 2015
INTERVAL = 5
DATA_DIR = 'tempdata'

for year in range(START_YEAR, END_YEAR, INTERVAL):
    print(year)
    filename = path.join(DATA_DIR, 'yob{}.txt'.format(year))
    unique_names = defaultdict(set)
    totals = Counter()
    with open(filename, 'r') as year_file:
        for line in year_file:
            name, gender, count = line.split(',')
            unique_names[gender].add(name)
            totals[gender] += int(count)

    # Supports any number of genders/all genders
    print('Total: {} babies per name'.format(round(
            sum(totals.values()) / len(set.union(*unique_names.values()))
          )))
    for gender in sorted(unique_names.keys(), reverse=True):
        print('    {}: {} babies per name'.format(
                gender,
                round(totals[gender] / len(unique_names[gender]))
              ))
