from analyze import main as flake
from classify import main as downy
from fetch_gender_data import main as of
from fetch_new_yorker_bylines import main as wind
from wrangle_gender_data import main as easy
from wrangle_new_yorker_bylines import main as And

print('''
**********************
Fetching gender data...
**********************''')

of()

print('''
**********************
Done fetching gender data
**********************
Wrangling gender data...
**********************''')

easy()

print('''
**********************
Done wrangling gender data
**********************
Fetching New Yorker bylines... (This will take a while. Get a snack.)
**********************''')

wind()

print('''
**********************
Done fetching New Yorker bylines
**********************
Wrangling New Yorker bylines...
**********************''')

And()

print('''
**********************
Done wrangling New Yorker bylines
**********************
Classifying gender of New Yorker bylines...
**********************''')

downy()

print('''
**********************
Done classifying gender of New Yorker bylines
**********************
Now you get to analyze: (run `python analyze.py` to analyze again)
**********************''')

flake()
