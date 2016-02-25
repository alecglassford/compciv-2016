import json
import requests

def read_mapzen_credentials():
	creds_filename = "creds_mapzen.txt"
	with open(creds_filename, 'r') as creds_file:
		return creds_file.read().strip() # e.g. "search-blahblah"

def fetch_mapzen_response(location):
	"""
	`location` is the string to be processed by Mapzen Search API
	returns the json-formatted response form Mapzen
	"""
	MAPZEN_ENDPOINT =  'https://search.mapzen.com/v1/search'
	request_params = {'text': location, 'api_key': read_mapzen_credentials()}
	resp = requests.get(MAPZEN_ENDPOINT, params=request_params)
	return resp.text

def parse_mapzen_response(txt):
	"""
	`txt` is JSON-formatted string (from Mapzen Search API)
	returns dictionary containing the useful key/values from the most relevant result
	"""
	gdict = {}
	data = json.loads(txt)
	if data['features']:
		feature = data['features'][0]
		props = feature['properties']
		coords = feature['geometry']['coordinates']

		gdict['status'] = 'OK'
		gdict['confidence'] = props['confidence']
		gdict['label'] = props['label']
		gdict['longitude'] = coords[0]
		gdict['latitude'] = coords[1]
	else:
		gdict['status'] = None
	return gdict

def geocode(location):
	"""
	Takes a location string and tries to geocode it with the Mapzen Search API

	Expects:
	`location` is a string that is a human description of a location.
	e.g. 'Stanford, CA'
	`CREDS_FILE` is the path of a file with a Mapzen API key.

	Does:
	Reads Mapzen API key from the file at CREDS_FILE, calls Mapzen Search API
	via an HTTP request, w/ `location` as the `text` parameter, deserializes
	response into a dictionary (using the JSON library)

	Returns:
	a dictionary with
	query_text: the inputted `location` string
	label: the string Mapzen uses to describe the location (e.g. an address)
	confidence: a float from 0 to 1 describing Mapzen's confidence in its result
	latitude: a float that's the latitude of the location
	longitude: a float that's the longitude of the location
	status: a string, "OK" (hopefully)
	"""
	api_response_text = fetch_mapzen_response(location)
	result = parse_mapzen_response(api_response_text)
	result['query_string'] = location
	return result
