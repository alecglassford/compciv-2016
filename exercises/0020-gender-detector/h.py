from os import path
import csv

YEAR = 2014
DATA_DIR = 'tempdata'
filename = path.join(DATA_DIR, 'wrangled{}.csv'.format(YEAR))

print('Most popular names with <= 60% gender skew:')
printed = 0
with open(filename, 'r') as csv_file:
    rows = csv.DictReader(csv_file)
    for row in rows:
        if int(row['ratio']) <= 60:
            print('{} {} {} {}'.format(row['name'].ljust(10),
                                       row['gender'],
                                       row['ratio'],
                                       row['total']))
            printed +=1
            if printed >=5:
                break
