import numpy as np
import image_slicer
from PIL import Image
a = np.array([[0, 1, 5, 0]])

res = np.full((10,10), 3)

print("before")
print(res)

res = np.split(res, 6)

print("after")

print(res)

import scipy as sp
imresize(arr,(28, 28))


# mapping = [4, 5, 5, 0]
#
# res[0][mapping[a.argmax()]] = 1
#
# print(res)
#
#
# im = image_slicer.slice('image_classification/test_images/original.png', 8)
#
# for i in im:
#     print(i)
#     with Image.open(i) as image:
#         print('hej')