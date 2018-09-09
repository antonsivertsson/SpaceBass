import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Markers:
    def __init__(self, points):
        self.points = points
        self.xs = list(points.get_xdata())
        self.ys = list(points.get_ydata())
        self.cid = points.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        print('click', event)
        if event.inaxes != self.points.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.points.set_data(self.xs, self.ys)
        self.points.figure.canvas.draw()


def pick_regions(img, label, existing_points=[]):
    fig, ax = plt.subplots()
    ax.imshow(img)
    fig.suptitle(label)

    points, = ax.plot([p[1] for p in existing_points], [p[0] for p in existing_points], "o")
    markers = Markers(points)

    plt.show()
    return list(zip(markers.ys, markers.xs))
