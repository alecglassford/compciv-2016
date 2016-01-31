import os, json

json_path = os.path.join('tempdata', 'mapzen', 'stanford.json')

with open(json_path, 'r') as json_file:
    raw_data = json_file.read()
data = json.loads(raw_data)

for feature in data['features']:
    if feature['type'] != 'Feature' or feature['geometry']['type'] != 'Point':
        continue # Shouldn't happen, but just in case
    print ('{};{};{};{}'.format(feature['properties']['label'],
                                feature['properties']['confidence'],
                                feature['geometry']['coordinates'][0],
                                feature['geometry']['coordinates'][1]))


# A recursive finder if we don't know where "Feature"s live. Overkill, but a fun exercise.
# def findFeatures(parent):
#     if isinstance(parent, list):
#         for child in parent:
#             findFeatures(child)
#     elif isinstance(parent, dict):
#         if parent.get('type') == 'Feature':
#             print ('{};{};{};{}'.format(feature['properties']['label'],
#                                         feature['properties']['confidence'],
#                                         feature['geometry']['coordinates'][0],
#                                         feature['geometry']['coordinates'][1]))
#         for key in parent:
#             findFeatures(parent[key])
# findFeatures(data)
