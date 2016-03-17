import csv
from os import path

from gender import analyze_name
from settings import WRANGLED_DIR, CLASSIFIED_DIR, MAGAZINE_SECTIONS

CLASSIFIED_CSV_FIELDS = ['author', 'year', 'month', 'day', 'usable_name',
                         'gender', 'ratio']

def extract_usable_name(namestr):
    nameparts = namestr.split()
    for part in nameparts:
        if '.' not in part and len(part) > 1:
            return part
    return namestr

def classify(section):
    result = []
    load_filename = path.join(WRANGLED_DIR, section)
    print('Classifying genders for the {} section'.format(section))
    with open(load_filename, 'r') as load_file:
        reader = csv.DictReader(load_file)
        for row in reader:
            row['usable_name'] = extract_usable_name(row['author'])
            row['gender'], row['ratio'] = analyze_name(row['usable_name'])
            print('Classfied {} as {}'.format(row['author'], row['gender']))
            result.append(row)
    return result

def save(result, section):
    save_filename = path.join(CLASSIFIED_DIR, section)
    with open(save_filename, 'w') as save_file:
        writer = csv.DictWriter(save_file, fieldnames=CLASSIFIED_CSV_FIELDS)
        writer.writeheader()
        writer.writerows(result)
    print('Wrote file {}'.format(save_filename))

def main():
    for section in MAGAZINE_SECTIONS:
        result = classify(section)
        save(result, section)

if __name__ == '__main__':
    main()
