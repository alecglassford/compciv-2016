from collections import Counter, defaultdict
import csv
from math import ceil
from os import path

try:
    import matplotlib.pyplot as plt
    can_plot = True
except ImportError:
    can_plot = False

from settings import CLASSIFIED_DIR, MAGAZINE_SECTIONS

MAX_X_TICKS = 20

############## Helpers

# Adapted from http://stackoverflow.com/a/9873935
def takespread(sequence, num):
    length = float(len(sequence))
    if num > length: return sequence
    return [sequence[int(ceil(i * length / num))] for i in range(num)]

def percent_format(num):
    return '({}%)'.format(round(100 * num))

##############

############## Choices for date granularity

def get_five_years(row):
    year = int(row['year'])
    start = year - year % 5
    return '{}-{}'.format(start, start + 5)

def get_year(row):
    return row['year']

def get_month(row):
    return '{}-{}'.format(row['year'], row['month'])

def get_day(row):
    return '{}-{}-{}'.format(row['year'], row['month'], row['day'])

##############

def get_counts(sections=MAGAZINE_SECTIONS, start_year=1900, get_date=get_year):
    counts = defaultdict(Counter)
    for section in sections:
        print('Counting genders in ', section, '...')
        load_filename = path.join(CLASSIFIED_DIR, section)
        with open(load_filename, 'r') as load_file:
            reader = csv.DictReader(load_file)
            for row in reader:
                if int(row['year']) >= start_year:
                    date = get_date(row)
                    counts[date][row['gender']] += 1
    return counts

def display(counts, sections):
    dates = sorted(counts.keys())
    total = [sum(counts[date].values()) for date in dates]
    female = [counts[date]['F'] for date in dates]
    male = [counts[date]['M'] for date in dates]
    unclassified = [counts[date]['U'] for date in dates]
    f_frac = [f/float(t) for f, t in zip(female, total)]
    m_frac = [m/float(t) for m, t in zip(male, total)]
    u_frac = [u/float(t) for u, t in zip(unclassified, total)]

    title = 'Fraction of New Yorker bylines from {} to {}\n(for {})'.format(
                                                dates[0], dates[-1], sections)
    print(title)
    print('{:<15}{:<8}{:<8}{:<8}{}'.format(
            'Date', 'Female', 'Male', 'Unclass.', 'Total'))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for i in range(len(dates)):
        print('{:<15}{:<8}{:<8}{:<8}{}\n{:<15}{:<8}{:<8}{:<8}\n'.format(
                dates[i], female[i], male[i], unclassified[i], total[i],
                '', percent_format(f_frac[i]), percent_format(m_frac[i]),
                percent_format(u_frac[i]), total[i]))

    if can_plot:
        plot(dates, f_frac, m_frac, title)

def plot(dates, f_frac, m_frac, title):
    x_spacing = [i for i in range(len(dates))]
    plt.stackplot(x_spacing, f_frac, m_frac, labels=('Female', 'Male'),
                  colors=('r','b'))
    plt.xlabel('Date')
    plt.ylabel('Fraction of New Yorker bylines')
    plt.title(title)
    plt.xticks(takespread(x_spacing, MAX_X_TICKS),
               takespread(dates, MAX_X_TICKS), rotation=45)
    plt.yticks([i/10.0 for i in range(10)])
    plt.legend(('Female', 'Male'))
    plt.show()

############## For users to choose options
def choose_sections():
    for i, section in enumerate(MAGAZINE_SECTIONS):
        print(i, ':', section)
    choice = input('''
What section would you like to see data on?
Enter the number from the listing above,
or just hit enter for all sections.
''')
    try:
        return [MAGAZINE_SECTIONS[int(choice)]]
    except Exception:
        return MAGAZINE_SECTIONS

def choose_start_year():
    choice = input('''
How far back should we go? (Enter a year from 1900 to 2016)
Note: Only fiction and poetry have really consistent data before 2007
''')
    try:
        year = int(choice)
        if year > 2016: return 2016
        return year
    except Exception:
        return 1900

def choose_granularity():
    choice = input('''
How granular should we be with our analysis?

Grouped by five year intervals? [type 'five']
Year by year? [type 'year'] (this is the default)
Month by month? [type 'month']
Day by day? [type 'day'] (really by week, since the magazine comes out weekly)
''')
    if choice == 'five':
        return get_five_years
    if choice == 'month':
        return get_month
    if choice == 'day':
        return get_day
    return get_year

##############

def main():
    sections = choose_sections()
    print('Will analyze', sections)
    start_year = choose_start_year()
    print('Will analyze starting from', start_year)
    date_getter = choose_granularity()
    counts = get_counts(sections, start_year, date_getter)
    display(counts, sections)

if __name__ == '__main__':
    main()
