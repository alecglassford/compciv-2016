from os import path
import csv

YEAR = 2014
DATA_DIR = 'tempdata'
filename = path.join(DATA_DIR, 'wrangled{}.csv'.format(YEAR))
thresholds = [60, 70, 80, 90, 99]

print('Popular names in 2014 with gender ratio less than or equal to:')

with open(filename, 'r') as csv_file:
    rows = csv.DictReader(csv_file)
    ratios = [int(row['ratio']) for row in rows if int(row['total']) >= 100]

for threshold in thresholds:
    print ('  {}%: {}/{}'.format(
            threshold,
            sum([1 for ratio in ratios if ratio <= threshold]),
            len(ratios)
          ))
