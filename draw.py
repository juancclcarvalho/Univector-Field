import cv2
import numpy as np
from matrix_coordinates_adjust import *
from constants import Const
from cm_pixels_conversions import *


def drawVector(field, origin, end):
    cv2.arrowedLine(field, origin, end, (0, 0, 255), 1)


def drawVectorField(field, vectors, w, h, step):
    length = 10
    k = 0
    #cv2.circle(field, toggleY(convertToPixel(Const.spiral_center_x),convertToPixel(Const.spiral_center_y),h), 5, (0, 255, 255), -1)
    for x in range(0, w, step):
        for y in range(0, h, step):
            origin = toggleY(convertToPixel(x), convertToPixel(y), convertToPixel(h))
            v = [vectors[k][0], vectors[k][1]]
            v[1] = -v[1]
            end = np.array(list(origin)) + length * np.array(v)
            end = (int(end[0]), int(end[1]))
            drawVector(field, origin, end)
            k += 1
            if k >= len(vectors) : return field
    return field
