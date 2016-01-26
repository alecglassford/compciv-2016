import os

file_name = os.path.join('tempdata', 'tragedies', 'romeoandjuliet')

with open(file_name, 'r') as rj_file:
    lines = list(enumerate(rj_file)) # A list where each entry is (line_number, line_text)

for line_num, line in lines[-5:]: # Prints last 5 lines of the list
    print('{}{}'.format(line_num + 1, ':'), line.strip())
