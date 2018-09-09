import numpy as np
from analysis import segmentation
from analysis import util
from util import data

class PixelClassifier:

    def __init__(self, model, classes):
        self.model = model
        self.classes = classes
    
    def train_from_dir(self, path):
        imgs, _, labels = data.load_image_set(path, with_labels=True)
        return self.train(imgs, labels)

    def train(self, images, labels):
        examples = {}
        for c in self.classes:
            examples[c] = []
        for (img, labs) in zip(images, labels):
            if labs is None:
                continue
            for c in self.classes:
                if c in labs:
                    pixels = util.pick_pixels(img, labs[c])
                    examples[c] += pixels
        x = []
        y = []
        for i_class in range(len(self.classes)):
            for e in examples[self.classes[i_class]]:
                x.append(e)
                y.append(i_class)
        print(x, y)
        self.model.fit(np.array(x), y)
        # TODO: label spreading for semi-supervised learning
    
    def save(self, fn):
        pass

    def load(self, fn):
        pass

    def segment(self, image):
        return segmentation.segment(self.model, image)
