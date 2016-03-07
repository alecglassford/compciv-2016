from os import path
from collections import defaultdict, Counter

YEAR = 2014
DATA_DIR = 'tempdata'
filename = path.join(DATA_DIR, 'yob{}.txt'.format(YEAR))

unique_names = defaultdict(set)
totals = Counter()
with open(filename, 'r') as year_file:
    for line in year_file:
        name, gender, count = line.split(',')
        unique_names[gender].add(name)
        totals[gender] += int(count)

# Supports any number of genders/all genders
print('Total: {} unique names for {} babies'.format(
        len(set.union(*unique_names.values())),
        sum(totals.values())
      ))
for gender in sorted(unique_names.keys(), reverse=True):
    print('    {}: {} unique names for {} babies'.format(
            gender,
            len(unique_names[gender]),
            totals[gender]
          ))
