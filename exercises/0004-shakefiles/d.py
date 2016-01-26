import os

file_name = os.path.join('tempdata', 'tragedies', 'hamlet')

with open(file_name, 'r') as hamlet_file:
    for i in range(5):
        print(hamlet_file.readline().strip())
