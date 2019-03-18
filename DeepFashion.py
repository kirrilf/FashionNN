

import numpy as np
import matplotlib.pyplot as plt
import cv2

im = cv2.imread("Clo1.jpg")

resized = cv2.resize(im, (28, 28), interpolation = cv2.INTER_AREA)

print(resized)