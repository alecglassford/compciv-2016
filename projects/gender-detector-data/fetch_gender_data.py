from glob import glob
from os import makedirs, path
from shutil import unpack_archive

import requests

from settings import GENDER_DIR

SOURCE_URL = 'https://www.ssa.gov/oact/babynames/names.zip'
DATA_ZIP_PATH = path.join(GENDER_DIR, 'names.zip')

def main():
    print('Downloading', SOURCE_URL)
    resp = requests.get(SOURCE_URL)
    with open(DATA_ZIP_PATH, 'wb') as zip_file:
        zip_file.write(resp.content)
    unpack_archive(DATA_ZIP_PATH, extract_dir=GENDER_DIR)
    baby_filenames = glob(path.join(GENDER_DIR, '*.txt'))
    print('There are {} txt files'.format(len(baby_filenames)))

if __name__ == '__main__':
    main()
