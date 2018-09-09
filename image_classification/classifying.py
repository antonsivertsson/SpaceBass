import numpy as np # linear algebra
import matplotlib.pyplot as plt # visualize satellite images
from skimage.io import imshow # visualize satellite images
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from keras.models import load_model
import image_slicer
import os
from PIL import Image
from resizeimage import resizeimage
import csv
import scipy as sp
from sklearn.feature_extraction import image

from util.data import find_images_for_dates
from client.sentinel2 import Client

dates = [
    '2017-07-01',
    '2017-07-15',
    '2017-08-01',
    '2017-08-15',
    '2017-09-01',
    '2017-09-15',
    '2017-10-01',
    '2017-10-15',
    '2017-11-01',
    '2017-11-15',
    '2017-12-01',
    '2017-12-15',
    '2018-01-01',
    '2018-01-15',
    '2018-02-01',
    '2018-02-15',
    '2018-03-01',
    '2018-03-15',
    '2018-04-01',
    '2018-04-15',
    '2018-05-01',
    '2018-05-15',
    '2018-06-01',
    '2018-06-15',
]

def get_time_series():
    C = Client('biscayabukten')
    return find_images_for_dates(C,"22.673761", "-19.2139972", dates)


def slize_resize(original):
    ret = []
    slices = image.extract_patches_2d(original, max_patches=8)

    for sliced in slices:
        # with open(sliced, 'r+b') as f:
        #     with Image.open(f) as image:
        cover = sp.misc.imresize(sliced, [28, 28])
        print(cover)

        arr_sliced = np.array(cover.getdata(), np.uint8).reshape(28,28,4)
        flattened = np.array([arr_sliced.flatten()])
        ret.append(flattened)

    return ret

# load model
model = load_model('trained_model.h5')

time_series = get_time_series()
# data_series = time_series.fetch_data()

print(time_series)
# not actually used
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

# mapping to correct classification index
mapping = [4, 5, 5, 0]

res = np.zeros((len(time_series),len(labels)))

for order, frame in enumerate(time_series):
    data = frame.fetch_data()

    slices = slize_resize(data)
    for slic in slices:
        prediction = model.predict(slic, verbose=1)
        max_index = np.argmax(prediction)
        res[order][mapping[max_index]] += 1 / 9

np.savetxt("foo.csv", res, delimiter=",")
