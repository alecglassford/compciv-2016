from os.path import join, basename
from os import makedirs
from glob import glob
import json

import requests

API_ENDPOINT = 'https://gateway.watsonplatform.net/visual-recognition-beta/api/v2/classify'
CREDS_FILENAME = 'creds_watson_visual.json'
PICS_DIR = 'pics'
RECOG_DIR = 'responses'
makedirs(RECOG_DIR, exist_ok=True)

# everything from here on out should be able to be used as is.
# though I've left out one key line (a missing variable assignment)

DEFAULT_PARAMS = {
    'version': '2015-12-02'
}
DEFAULT_HEADERS = {
    'Accept': 'application/json'
}

# get my creds
with open(CREDS_FILENAME, 'r') as creds_file:
	creds = json.load(creds_file)
my_username = creds['credentials']['username']
my_password = creds['credentials']['password']
myauth = (my_username, my_password)


# Make sure this works (i.e. something gets printed)
# then uncomment the lines to actually save the data
# to disk, i.e. in the responses/ folder
for fname in glob(join(PICS_DIR, '*.jpg')):
    print("Uploading", fname)

    with open(fname, 'rb') as imgdata:
        ## Talk to IBM
        ## need to send the imgdata in a dict type object
        upload_data = {}
        upload_data['images_file'] = (fname, imgdata)
        resp = requests.post(API_ENDPOINT, params=DEFAULT_PARAMS,
                        auth=myauth, headers=DEFAULT_HEADERS,
                        files=upload_data)

    # make sure things are OK, i.e. 200
    print(resp.status_code)

    if resp.status_code == 200:
        oname = join(RECOG_DIR, basename(fname + '.json'))
        print("Writing to:", oname)

        with open(oname, 'w') as o:
            o.write(resp.text)

    else:
        print("Error code was", resp.status_code, " -- not: 200")
