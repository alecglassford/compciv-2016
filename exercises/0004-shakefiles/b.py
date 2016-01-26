import os.path

import requests

url = 'http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz'
dir_name = 'tempdata'
file_name = 'matty.shakespeare.tar.gz'
full_name = os.path.join(dir_name, file_name)

print('Downloading:', url)
resp = requests.get(url)
with open(full_name, 'wb') as zip_file:
    print('Writing file:', full_name)
    zip_file.write(resp.content)
