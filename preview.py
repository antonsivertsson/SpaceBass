import sys
import json
import numpy as np
from client import sentinel2
from util import plot
from config import *


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: %s <place> <frame-index>' % sys.argv[0])
        sys.exit(1)
    place = sys.argv[1]
    frame_index = int(sys.argv[2])
    with open(PLACES_FILE, "r") as f:
        places = json.load(f)
    if place not in places:
        print('%s is not defined in %s' % (place, PLACES_FILE))
    coords = places[place]
    client = sentinel2.Client(api_key=API_KEY)
    series = client.fetch_series(lng=coords[0], lat=coords[1])
    frame = list(series.frames())[frame_index]
    print(frame.date)
    img = frame.fetch_rgba()
    raw = frame.fetch_data()
    opt = plot.optimize_raw_for_display(raw, [3, 2, 1])
    plot.show_all([img, opt])
