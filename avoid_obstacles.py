from calc_utils import *
from constants import Const
import numpy as np
import math
from copy import copy
from cm_pixels_conversions import *
import draw
import cv2
from get_vectors import *



origin = (75, 65)

def avoid_obstacles(origin, r_x, r_y):
    field_center_x, field_center_y = origin
    d_x, d_y = delta(r_x, r_y, field_center_x, field_center_y)
    
    phi_auf = phiAuf(origin, r_x, r_y, d_x, d_y)

    return phi_auf


if __name__ == '__main__':
    w, h = arena_w, arena_h
    px_w, px_h = setArenaSize()
    step = Const.step

    field = np.zeros((px_h, px_w, 3))
    vectors = getVectors(w, h, step, avoid_obstacles)
    vectorsField = draw.drawVectorField(copy(field), vectors, w, h, step)
    cv2.imshow('Avoid Obstacles', vectorsField)
    cv2.waitKey(0)
    cv2.destroyAllWindows()