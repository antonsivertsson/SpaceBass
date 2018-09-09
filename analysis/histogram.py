import numpy as np

def count_values(img, values):
    unique, counts = np.unique(img[:], return_counts=True)
    d = dict(zip(unique, counts))
    return [d[v] if v in d else 0 for v in values]
