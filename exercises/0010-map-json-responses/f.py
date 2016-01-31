import os, json

json_path = os.path.join('tempdata', 'mapzen', 'stanford.json')

with open(json_path, 'r') as json_file:
    raw_data = json_file.read()
data = json.loads(raw_data)
print('type:', data['type'])
print('text:', data['geocoding']['query']['text'])
print('size:', data['geocoding']['query']['size'])
print('boundary.country:', data['geocoding']['query']['boundary.country'])
