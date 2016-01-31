import requests

URL = 'http://locations.in-n-out.com/api/finder/search'
locations = requests.get(URL).json()
print(len(locations))
for location in locations:
    print('{} {}, {} {}'.format(location['StreetAddress'], location['City'], location['State'], location['ZipCode']))
