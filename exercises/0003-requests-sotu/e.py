import requests

resp = requests.get('https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-%E2%80%93-prepared-delivery-state-union-address')
print(resp.text.count('Applause'))
print(resp.text.lower().count('applause'))
print(resp.text.count('<p>'))
