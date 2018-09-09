
def segment(pixel_model, image):
    (nr, nc, n_channels) = image.shape
    pixels = image.reshape((nr*nc, n_channels))
    labels = pixel_model.predict(pixels)
    return labels.reshape((nr, nc))
