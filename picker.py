import sys
from tools import label
from util import data
import json
from config import *

labels = [
    "cloud",
    "city",
    "ruins",
    "agriculture",
    "barren",
    "vegetation",
    "moutains",
    "charred",
    "snow",
    "water",
]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = DOWNLOAD_PATH
    imgs, names = data.load_image_set(path)
    rgbs = [img[:, :, 1:4] for img in imgs]
    print('Found %d images' % len(rgbs))
    for i in range(len(rgbs)):
        rgb = rgbs[i]
        name = names[i]
        print('Labeling image...')
        picks = {}
        try:
            with open(name + ".labels", "r") as f:
                picks = json.load(f)
        except FileNotFoundError:
            pass
        for l in labels:
            existing = picks[l] if l in picks else []
            points = label.pick_regions(rgb/8000, l, existing)
            print('File: %s' % name)
            print('Points picked: %s' % (points, ))
            picks[l] = points
        with open(name + ".labels", "w") as f:
            json.dump(picks, f)
    print('Done.')
