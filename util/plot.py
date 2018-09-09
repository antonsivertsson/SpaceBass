from skimage import exposure
import numpy as np

def optimize_raw_for_display(raw, channels=None):
    if len(raw.shape) == 2 or raw.shape[2] == 1:
        return exposure.equalize_adapthist(raw, clip_limit=0.03)
    else:
        (nr, nc, d) = raw.shape
        if channels is None:
            channels = range(d)
        return np.dstack([optimize_raw_for_display(raw[:, :, ch]) for ch in channels])

def raws_to_rgbs(raws):
    return [optimize_raw_for_display(raw, [3, 2, 1]) for raw in raws]

def show(image):
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    imgplot = plt.imshow(image)
    plt.show()

def show_all(images):
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    for i in range(len(images)):
        plt.subplot((len(images) + 3) // 4, min(4, len(images)), i+1)
        imgplot = plt.imshow(images[i])
    plt.show()
