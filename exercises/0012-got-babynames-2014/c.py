import os, re

data_path = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')

khaleesi_pattern = re.compile(r'Khale[es]s')
khaleesi_count = 0
with open(data_path, 'r') as data_file:
    for line in data_file:
        name, sex, count = line.strip().split(',')
        if name == 'Daenerys':
            print('Daenerys:', count)
        elif khaleesi_pattern.match(name): # name starts with pattern
            khaleesi_count += int(count)
print('Khaleesi:', khaleesi_count)
