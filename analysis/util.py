import numpy as np

def pick_pixels(image, points):
    res = []
    for p in points:
        res.append(image[int(p[0]), int(p[1]), :])
    return res

def sample_pixels(images, n=1000000):
    pixels = to_pixels(images)
    sample = pixels[np.random.randint(0, pixels.shape[0], n), :]
    return sample

def to_pixels(images):
    n_channels = images[0].shape[-1]
    # Flatten the pixels.
    n_pix = 1
    for dim in images[0].shape[:-1]:
        n_pix *= dim
    pixels = np.stack(images).reshape((n_pix*len(images), n_channels))
    return pixels
