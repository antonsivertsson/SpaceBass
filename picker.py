from tools import label
from util import data
import json

labels = [
    "cloud",
    "city",
    "ruins",
    "agriculture",
    "plains",
    "desert",
    "vegetation",
    "moutains",
    "charred",
    "snow",
    "water",
]

if __name__ == "__main__":
    imgs, names = data.load_image_set("data/samples")
    rgbs = [img[:, :, 1:4] for img in imgs]
    for i in range(2):
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
