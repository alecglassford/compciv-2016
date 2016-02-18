import os
from collections import Counter

load_path = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')

total_baby_counts = Counter()
with open(load_path, 'r') as load_file:
    for line in load_file:
        name, sex, baby_count = line.strip().split(',')
        total_baby_counts[name] += int(baby_count)
popular_names = sorted(total_baby_counts.keys(),
                       key=lambda name: total_baby_counts[name],
                       reverse=True)
total_num_babies = sum(total_baby_counts.values())

def percent_babies(name_start_index, name_end_index):
    count = 0
    for name in popular_names[name_start_index - 1: name_end_index]:
        count += total_baby_counts[name]
    print('Names {} to {}:'.format(name_start_index, name_end_index),
          round(100 * count/total_num_babies, 1))

percent_babies(1, 10)
percent_babies(11, 100)
percent_babies(101, 1000)
percent_babies(1001, 10000)
percent_babies(10001, len(popular_names))
