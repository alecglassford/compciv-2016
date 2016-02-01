import os

import requests

URL = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'

os.makedirs('tempdata', exist_ok=True)
save_path = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
data = requests.get(URL).text
with open(save_path, 'w') as save_file:
    save_file.write(data)
print('There are', len(data.splitlines()), 'in', save_path)
