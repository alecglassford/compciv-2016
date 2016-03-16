from os import makedirs, path

DATA_DIR = 'tempdata'
RAW_DIR = path.join(DATA_DIR, 'sections')
makedirs(RAW_DIR, exist_ok=True)
WRANGLED_DIR = path.join(DATA_DIR, 'wrangled_sections')
makedirs(WRANGLED_DIR, exist_ok=True)

MAGAZINE_SECTIONS = ['reporting', 'talk-of-the-town', 'shouts-murmurs',
                     'critics', 'fiction', 'poems']

CSV_FIELD_NAMES = ['author', 'year', 'month', 'day']
