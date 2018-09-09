import numpy as np # linear algebra
import matplotlib.pyplot as plt # visualize satellite images
from skimage.io import imshow # visualize satellite images
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from keras.models import load_model
from scipy import misc
import image_slicer
import os
from PIL import Image
from resizeimage import resizeimage


y_train_set_fpath = '../../../sat_dataset/y_test_sat4.csv'
Y_train = pd.read_csv(y_train_set_fpath)


def slize_resize(original):
    ret = []
    filenames = []

    image_slicer.slice(original, 8)
    for sliced_image in os.listdir('test_images'):

        with open("test_images/" + sliced_image, 'r+b') as f:
            with Image.open(f) as image:
                filenames.append(f)

                cover = resizeimage.resize_cover(image, [28, 28])

                # arr_sliced = misc.imread(cover)

                arr_sliced = np.array(cover.getdata(), np.uint8).reshape(28,28,4)

                flattened = np.array([arr_sliced.flatten()])

                ret.append(flattened)

    return ret, filenames

images, filenames = slize_resize('test_images/original.png')

# load model
model = load_model('trained_model.h5')


for i, image in enumerate(images):
    prediction = model.predict(image, verbose=1)
    # result= {}

    print(filenames[i])

    ix = 0 # Type a number between 0 and 999 inclusive
    imshow(image) # Only seeing the RGB channels
    # Tells what the image is

    print ('Prediction:\n{:.1f}% probability barren land,\n{:.1f}% probability trees,\n{:.1f}% probability grassland,\n{:.1f}% probability other\n'.format(prediction[ix,0]*100,prediction[ix,1]*100,prediction[ix,2]*100,prediction[ix,3]*100))

# plt.show()#
