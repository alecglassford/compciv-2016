import os
from collections import Counter

data_path = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')

# The data may conform to a gender binary, but since the exercise just says
# 'by gender,' I see no reason for my code to. More generalizable +
# reflective of my values, as all one creates ought to be. :)
gender_counts = Counter()
with open(data_path, 'r') as data_file:
    for line in data_file:
        name, sex, count = line.strip().split(',')
        gender_counts[sex] += int(count)
for gender in sorted(gender_counts.keys()): # sort to ensure expected F then M
    print('{}: {}'.format(gender, gender_counts[gender]))
