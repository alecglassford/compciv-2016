import csv
from os import path
import re

from bs4 import BeautifulSoup

from settings import RAW_DIR, WRANGLED_DIR, MAGAZINE_SECTIONS, CSV_FIELD_NAMES

date_pattern = re.compile(r'magazine/(\d+)/(\d+)/(\d+)/')

for section in MAGAZINE_SECTIONS:
    result = []
    load_filename = path.join(RAW_DIR, section)
    with open(load_filename, 'r') as load_file:
        source = load_file.read()

    print('Parsing html of the {} section'.format(section))
    # lxml is faster, but extra dependency + doesn't handle our janky document
    soup = BeautifulSoup(source, 'html.parser')

    articles = soup.find_all('article')
    print('Wrangling {} articles from {}'.format(len(articles), section))
    for article in articles:
        author = article.find(rel='author')
        if author: # Ignore articles without author listed
            article_url = article.find('a').get('href') # Should be first url
            date = date_pattern.search(article_url)
            if date: # Ignore articles we failed to find date for
                result.append((author.get_text(), date.group(1),
                               date.group(2), date.group(3)))

    save_filename = path.join(WRANGLED_DIR, section)
    with open(save_filename, 'w') as save_file:
        writer = csv.writer(save_file)
        writer.writerow(CSV_FIELD_NAMES)
        writer.writerows(result)
    print('Wrote file {}'.format(save_filename))
