from os import path
from glob import glob
from collections import Counter

DATA_DIR = 'tempdata'
desired_filenames = ['yob19[56789]*.txt', 'yob2*.txt']

totals = Counter()
for filename in desired_filenames:
    for full_filename in glob(path.join(DATA_DIR, filename)):
        with open(full_filename, 'r') as year_file:
            for line in year_file:
                name, gender, count = line.split(',')
                totals[gender] += int(count)

# Supports any number of genders/all genders
result = ' '.join(['{}: {}'.format(gender, str(totals[gender]).rjust(6))
                    for gender in sorted(totals.keys())])
print(result)

# This part is just F/M though
f_to_m_ratio = round(100 * totals['F'] / totals['M'])
print('F/M baby ratio:', f_to_m_ratio)
