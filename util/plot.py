from skimage import exposure

def optimize_raw_for_display(raw):
    return exposure.equalize_adapthist(raw, clip_limit=0.03)
