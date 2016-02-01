import os, string
from collections import defaultdict, Counter
from string import ascii_lowercase

COL_WIDTH = 8
data_path = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')

last_letter_counts = defaultdict(Counter)
with open(data_path, 'r') as data_file:
    for line in data_file:
        name, sex, count = line.strip().split(',')
        last_letter = name[-1].lower()
        last_letter_counts[sex][last_letter] += int(count)

# The data may conform to a gender binary, but since the exercise just says
# 'by gender,' I see no reason for my code to. More generalizable +
# reflective of my values, as all one creates ought to be. :)
genders = sorted(last_letter_counts.keys())

# Print header
header = ['letter'.ljust(COL_WIDTH)]
for gender in genders:
    header.append(gender.rjust(COL_WIDTH))
print(''.join(header))

# Print spacer
print('-' * COL_WIDTH * (1 + len(genders)))

# Print a row for each letter
for letter in ascii_lowercase:
    row = [letter.ljust(COL_WIDTH)]
    for gender in genders:
        row.append(str(last_letter_counts[gender][letter]).rjust(COL_WIDTH))
    print(''.join(row))
