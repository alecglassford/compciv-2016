from os import path
import csv
import json

DATA_DIR = 'tempdata'
input_filename = path.join(DATA_DIR, 'wrangledbabynames.csv')
output_filename = path.join(DATA_DIR, 'wrangledbabynames.json')

result = []
with open(input_filename, 'r') as csv_file:
    rows = csv.DictReader(csv_file)
    for row in rows:
        row['ratio'] = int(row['ratio'])
        row['females'] = int(row['females'])
        row['males'] = int(row['males'])
        row['total'] = int(row['total'])
        result.append(row)

    csv_file.seek(0)
    csv_length = len(csv_file.read())

result_string = json.dumps(result, indent=2)
json_length = len(result_string)

with open(output_filename, 'w') as json_file:
    json_file.write(result_string)

ratio = round((json_length - csv_length) / csv_length, 1)
print('CSV has {} characters'.format(csv_length))
print('JSON has {} characters'.format(json_length))
print('JSON requires {} times more text characters thatn CSV'.format(ratio))
