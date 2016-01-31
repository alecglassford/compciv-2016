import os, json

json_path = os.path.join('tempdata', 'googlemaps', 'stanford.json')

with open(json_path, 'r') as json_file:
    raw_data = json_file.read()
data = json.loads(raw_data)
for result in data['results']:
    print('{};{};{}'.format(result['formatted_address'],
                            result['geometry']['location']['lng'],
                            result['geometry']['location']['lat']))
