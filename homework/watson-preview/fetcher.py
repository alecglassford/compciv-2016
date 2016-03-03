from os import makedirs
from os.path import join
from string import ascii_lowercase

import requests

PICS_DIR = 'pics'
makedirs(PICS_DIR, exist_ok = True)
URLS = ['https://farm2.staticflickr.com/1569/24980825130_3be7264c21_o_d.jpg',
		'https://farm8.staticflickr.com/7503/15835955115_3a006057be_o.jpg',
		'https://farm3.staticflickr.com/2079/2178246047_384aca9fcb_o_d.jpg',
		'https://farm3.staticflickr.com/2266/2178246585_14139d6905_o_d.jpg',
		'https://farm6.staticflickr.com/5462/7096416329_8621d70f0c_o_d.jpg']

for i, url in enumerate(URLS):
	print('Downloading', url)
	resp = requests.get(url)
	save_name = join(PICS_DIR, ascii_lowercase[i] + '.jpg')
	print('Saving to', save_name)
	with open(save_name, 'wb') as save_file:
		save_file.write(resp.content)
