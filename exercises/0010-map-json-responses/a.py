import os

import requests

resources = [
                {
                    'name': 'googlemaps',
                    'url': 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
                },
                {
                    'name': 'mapzen',
                    'url': 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'
                }
            ]

for resource in resources:
    save_path = os.path.join('tempdata', resource['name'], 'stanford.json')
    os.makedirs(os.path.dirname(save_path), exist_ok=True) # Make each directory as we go
    print('---\nDownloading from:', resource['url'])
    data = requests.get(resource['url']).text
    print('Writing to:', save_path)
    with open(save_path, 'w') as save_file:
        save_file.write(data)
    print('Wrote {} lines and {} characters'.format(len(data.splitlines()), len(data)))
