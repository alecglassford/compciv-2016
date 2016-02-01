import os, string
from collections import Counter
from string import ascii_lowercase

data_path = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')

last_letter_counts = Counter()
with open(data_path, 'r') as data_file:
    for line in data_file:
        name, sex, count = line.strip().split(',')
        last_letter = name[-1].lower()
        last_letter_counts[last_letter] += int(count)
for letter in ascii_lowercase:
    print('{}: {}'.format(letter, last_letter_counts[letter]))
