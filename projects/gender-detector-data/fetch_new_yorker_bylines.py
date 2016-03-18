from os import path

import requests
from bs4 import BeautifulSoup # Just for finding num_pages here

from settings import RAW_DIR, MAGAZINE_SECTIONS

SECTION_URL_BASE = 'http://www.newyorker.com/magazine/{}'

def download(section):
    section_url = SECTION_URL_BASE.format(section)
    sources = [requests.get(section_url).text]
    first_page_soup = BeautifulSoup(sources[0], 'html.parser')
    num_pages = int(first_page_soup.select_one('#maxPages').get_text())
    print('Downloading {} pages from the {} section'.format(num_pages, section))
    page_url_base = section_url + '/page/{}'
    for page_num in range(2, num_pages + 1):
        print('Downloading page {} of {}'.format(page_num, section))
        page_url = page_url_base.format(page_num)
        sources.append(requests.get(page_url).text)
    return sources

def save(section, sources):
    save_filename = path.join(RAW_DIR, section)
    with open(save_filename, 'w') as save_file:
        save_file.writelines(sources)
    print('Wrote file {}'.format(save_filename))

def main():
    for section in MAGAZINE_SECTIONS:
        sources = download(section)
        save(section, sources)

if __name__ == '__main__':
    main()
