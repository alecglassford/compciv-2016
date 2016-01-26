import os

file_name = os.path.join('tempdata', 'tragedies', 'hamlet')

num_lines = 0
with open(file_name, 'r') as hamlet_file:
    for line in hamlet_file:
        num_lines += 1
print(file_name, 'has', num_lines, 'lines')
