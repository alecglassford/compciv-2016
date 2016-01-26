import os, glob

tragic_path = os.path.join('tempdata', 'tragedies', '*')
tragic_file_names = glob.glob(tragic_path)

for file_name in tragic_file_names:
    with open(file_name, 'r') as tragic_file:
        lines = list(enumerate(tragic_file)) # A list where each entry is (line_number, line_text)
    print(file_name, 'has', len(lines), 'lines')
    for line_num, line in lines[-5:]: # Prints last 5 lines of the list
        print('{}{}'.format(line_num + 1, ':'), line.strip())
