import sys
import json
from client import sentinel2
from config import *

def show(image):
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    imgplot = plt.imshow(image)
    plt.show()

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
    show(img)
    raw = frame.fetch_data()
    show(raw[:, :, 1:4]/7000)
