import csv
from os import path
import re

from bs4 import BeautifulSoup

from settings import RAW_DIR, WRANGLED_DIR, MAGAZINE_SECTIONS

CSV_FIELD_NAMES = ['author', 'year', 'month', 'day']
date_pattern = re.compile(r'magazine/(\d+)/(\d+)/(\d+)/')

def load(section):
    load_filename = path.join(RAW_DIR, section)
    with open(load_filename, 'r') as load_file:
        return load_file.read()

def parse_article(article):
    author = article.find(rel='author')
    if author: # Ignore articles without author listed
        article_url = article.find('a').get('href') # Should be first url
        date = date_pattern.search(article_url)
        if date: # Ignore articles we failed to find date for
            return author.get_text(), date.group(1), date.group(2), date.group(3)
    return None

def wrangle(section, source):
    result = []
    print('Parsing html of the {} section'.format(section))
    # lxml is faster, but extra dependency + doesn't handle our janky document
    soup = BeautifulSoup(source, 'html.parser')
    articles = soup.find_all('article')
    print('Wrangling {} articles from {}'.format(len(articles), section))
    for article in articles:
        row = parse_article(article)
        if row: result.append(row)
    return result

def save(section, result):
    save_filename = path.join(WRANGLED_DIR, section)
    with open(save_filename, 'w') as save_file:
        writer = csv.writer(save_file)
        writer.writerow(CSV_FIELD_NAMES)
        writer.writerows(result)
    print('Wrote file {}'.format(save_filename))

def main():
    for section in MAGAZINE_SECTIONS:
        source = load(section)
        result = wrangle(section, source)
        save(section, result)

if __name__ == '__main__':
    main()
