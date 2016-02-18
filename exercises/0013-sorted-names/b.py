import os

load_path = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')

with open(load_path, 'r') as load_file:
    lines = load_file.readlines()
sorted_lines = sorted(lines, key=lambda line: int(line.strip().split(',')[2]), reverse=True)
for i in range(10):
    print('{}. {}'.format(i + 1, sorted_lines[i].strip()))
