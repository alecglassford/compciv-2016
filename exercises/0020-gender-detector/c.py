from os import path
from glob import glob
from collections import defaultdict

DATA_DIR = 'tempdata'
desired_filenames = ['yob19[56789]*.txt', 'yob2*.txt']

unique_names = defaultdict(set)
for filename in desired_filenames:
    for full_filename in glob(path.join(DATA_DIR, filename)):
        with open(full_filename, 'r') as year_file:
            for line in year_file:
                name, gender, count = line.split(',')
                unique_names[gender].add(name)

# Supports any number of genders/all genders
result = ' '.join(['{}: {}'.format(gender,
                                   str(len(unique_names[gender])).rjust(6))
                    for gender in sorted(unique_names.keys())])
print(result)

# This part is just F/M though
f_to_m_ratio = round(100 * len(unique_names['F']) / len(unique_names['M']))
print('F/M baby ratio:', f_to_m_ratio)
