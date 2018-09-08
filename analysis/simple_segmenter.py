import numpy as np
from sklearn import mixture


class PixelGMM:

    def __init__(self, n_comp=6):
        self.model = mixture.GaussianMixture(n_components=n_comp, covariance_type='full')
    
    def fit(self, images):
        n_channels = images[0].shape[-1]
        # Flatten the pixels.
        n_pix = 1
        for dim in images[0].shape[:-1]:
            n_pix *= dim
        pixels = np.stack(images).reshape((n_pix*len(images), n_channels))
        print(pixels.shape)
        sample = pixels[np.random.randint(0, pixels.shape[0], 1000000), :]
        self.model.fit(sample)
    
    def segment(self, image):
        (nr, nc, n_channels) = image.shape
        pixels = image.reshape((nr*nc, n_channels))
        labels = self.model.predict(pixels)
        return labels.reshape((nr, nc))
