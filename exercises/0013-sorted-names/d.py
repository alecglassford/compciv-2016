import os
from collections import defaultdict, Counter

load_path = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')

counts_by_gender = defaultdict(Counter) # supports arbitrary genders
with open(load_path, 'r') as load_file:
    for line in load_file:
        name, sex, baby_count = line.strip().split(',')
        if 'x' in name.lower():
            counts_by_gender[sex][name] += int(baby_count)
female_names = sorted(counts_by_gender['F'].keys(),
                      key=lambda name: counts_by_gender['F'][name],
                      reverse=True)
male_names = sorted(counts_by_gender['M'].keys(),
                    key=lambda name: counts_by_gender['M'][name],
                    reverse=True)
print('Female')
for i in range(5):
    print('{}.'.format(i+1), female_names[i].ljust(12), str(counts_by_gender['F'][female_names[i]]).rjust(7))
print('Male')
for i in range(5):
    print('{}.'.format(i+1), male_names[i].ljust(12), str(counts_by_gender['M'][male_names[i]]).rjust(7))
