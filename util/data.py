import numpy as np
import random

def random_coords():
    # Ideally we should randomize a point in 3-space and calculate long-lat
    # from that, to avoid oversampling near the poles, but this works.
    return (random.uniform(-180, 180), random.uniform(-90, 90))

def find_images_for_dates(client, lng, lat, dates):
    series = client.fetch_series(lng, lat)
    i = 0
    frames = list(series.frames())
    found = []
    for date in dates:
        while i < len(frames) and date > frames[i].date:
            i = i + 1
        if i == len(frames):
            raise Exception('Date not found: %s (last date in dataset is %s)' % (date, frames[i].date))
        found.append(frames[i])
    return found

def download_places(path, client, places, dates):
    for name in places:
        coords = places[name]
        dir = "%s/%s" % (path, name)
        frames = find_images_for_dates(client, coords[0], coords[1], dates)
        for frame in frames:
            import os
            fn = "%s/%s.npy" % (dir, frame.date)
            if os.path.isfile(fn):
                print('%s skipped (already downloaded)' % fn)
                continue # Already downloaded.
            os.makedirs(dir, exist_ok=True)
            img = frame.fetch_data()
            with open(fn, "wb") as f:
                np.save(f, img)
                print('%s downloaded' % fn)

def store_image_set(path, imgs, names=None):
    for i in range(len(imgs)):
        if names is None:
            dst = "%s/img_%03d.npy" % (path, i)
        else:
            dst = "%s/%s.npy" % (path, names[i])
        with open(dst, "wb") as f:
            np.save(f, imgs[i])

def load_image_set(path, with_labels=False):
    import glob
    import json
    imgs = []
    names = []
    labels = []
    for fn in sorted(glob.glob("%s/img_*.npy" % path)):
        with open(fn, "rb") as f:
            imgs.append(np.load(f))
            names.append(fn)
        if with_labels:
            try:
                with open(fn + ".labels", "r") as f:
                    labels.append(json.load(f))
            except FileNotFoundError:
                labels.append(None)
    if with_labels:
        return imgs, names, labels
    else:
        return imgs, names
