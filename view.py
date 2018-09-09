import sys
import numpy as np
from util import plot
from config import *


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print('Usage: %s <filename> <bands>' % sys.argv[0])
        sys.exit(1)
    fn = sys.argv[1]
    channels = [int(arg) for arg in sys.argv[2:]]
    with open(fn, "rb") as f:
        raw = np.load(f)
    opt = plot.optimize_raw_for_display(raw, channels)
    plot.show(opt)
