import requests

resp = requests.get('https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-%E2%80%93-prepared-delivery-state-union-address')
print resp.status_code
print len(resp.text)
print resp.url
