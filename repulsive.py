from calc_utils import *
from get_vectors import *
import cv2
import draw
from copy import copy
import numpy as np


def repulsive(origin, v_x, v_y):
    s_x, s_y = origin
    delta_x, delta_y = delta(s_x, s_y, v_x, v_y)
    th = theta(delta_x, delta_y)
    nh = Nh(th)

    return nh


if __name__ == '__main__':
    w, h = 675, 585
    step = 10

    field = np.zeros((h, w, 3))
    vectors = getVectors(w, h, step, repulsive)
    vectorField = draw.drawVectorField(copy(field), vectors, w, h, step)
    cv2.imshow('repulsive', vectorField)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
