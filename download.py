import json
from client import sentinel2
from util import data
from config import *

dates = [
    '2017-07-01',
    '2017-08-01',
    '2017-09-01',
    '2017-10-01',
    '2017-11-01',
    '2017-12-01',
    '2018-01-01',
    '2018-02-01',
    '2018-03-01',
    '2018-04-01',
    '2018-05-01',
    '2018-06-01',
]

if __name__ == "__main__":
    with open(PLACES_FILE, "r") as f:
        places = json.load(f)
    client = sentinel2.Client(api_key=API_KEY)
    data.download_places(DOWNLOAD_PATH, client, places, dates)
