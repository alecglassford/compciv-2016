from bs4 import BeautifulSoup

with open('raw-list.html', 'r') as raw_doc:
    soup = BeautifulSoup(raw_doc.read(), 'html.parser')

restaurants = soup.find_all(class_='resultContent')
print(len(restaurants))
for restaurant in restaurants:
    address = restaurant.find(attrs={'data-bind': 'text: StreetAddress'}).text
    city = restaurant.find(attrs={'data-bind': 'text: City'}).text
    state = restaurant.find(attrs={'data-bind': 'text: State'}).text
    zip = restaurant.find(attrs={'data-bind': 'text: ZipCode'}).text
    print('{} {},{} {}'.format(address, city, state, zip))
