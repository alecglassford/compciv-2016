import os

data_path = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')

with open(data_path, 'r') as data_file:
    # list of (name, sex, count), all strings
    baby_list = [line.strip().split(',') for line in data_file]
# sort by count descending
baby_list = sorted(baby_list, key=lambda baby: int(baby[2]), reverse=True)

girls = []
boys = []
for baby in baby_list:
    if len(girls) >=5 and len(boys) >=5:
        break
    if baby[1] == 'F':
        girls.append(baby)
    else: # baby[1] == 'M'
        boys.append(baby)

print('Top baby girl names')
for i in range(5):
    print(i+1, '.', girls[i][0], girls[i][2])
print('Top baby boy names')
for i in range(5):
    print(i+1, '.', boys[i][0], boys[i][2])
