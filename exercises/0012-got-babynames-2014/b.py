import os

data_path = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')

sum = 0
with open(data_path, 'r') as data_file:
    for line in data_file:
        sum += int(line.split(',')[2])
print('There are', sum, 'babies whose names were recorded in 2014.')
