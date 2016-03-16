from collections import Counter, defaultdict
import csv
from os import path

from settings import CLASSIFIED_DIR, MAGAZINE_SECTIONS

for section in MAGAZINE_SECTIONS:
    result = []
    load_filename = path.join(CLASSIFIED_DIR, section)
    with open(load_filename, 'r') as load_file:
        rows = list(csv.DictReader(load_file))
    rows.sort(key=lambda row: (row['year'], row['month'], row['day']))
    counts = defaultdict(Counter)
    for row in rows:
        year_month = '{}-{}'.format(row['year'], row['month'])
        counts[year_month][row['gender']] += 1
    print('Gender counts for {}:'.format(section))
    for year in sorted(counts.keys()):
        print('{},{},{},{}'.format(year, counts[year]['F'], counts[year]['M'], counts[year]['U']))
