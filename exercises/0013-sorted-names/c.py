import os
from collections import Counter

load_path = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')

total_baby_counts = Counter()
with open(load_path, 'r') as load_file:
    for line in load_file:
        name, sex, baby_count = line.strip().split(',')
        total_baby_counts[name] += int(baby_count)
popular_babies = {k:v for k,v in total_baby_counts.items() if v >= 2000}
popular_names = sorted(popular_babies.keys(),
                       key=lambda name: (len(name), popular_babies[name]),
                       reverse=True)
for name in popular_names[:10]:
    print(name.ljust(11), str(popular_babies[name]).rjust(12))
