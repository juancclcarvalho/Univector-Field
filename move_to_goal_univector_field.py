import numpy as np
import math
import cv2
from copy import copy
from calc_utils import *
import draw
from matrix_coordinates_adjust import *
from cm_pixels_convertions import *
from constants import Const

spiral_center_x = Const.spiral_center_x
spiral_center_y = Const.spiral_center_y
direction = Const.direction
de = convertToPixel(Const.de)
kr = convertToPixel(Const.kr)
step = Const.step
cw = -1

def getOmega(s_x, s_y, v_x, v_y):

    delta_x, delta_y = getDelta(s_x, s_y, v_x, v_y)

    # get Y
    yl = delta_y + de
    yr = delta_y - de

    #                           /*        pl        */
    ppl = getDistance(delta_x, delta_y - de)
    #                           /*        pr        */
    ppr = getDistance(delta_x, delta_y + de)

    theta = getTheta(delta_x, delta_y)

    phi_cw = getPhi(theta, ppr, cw, de, kr)
    phi_ccw = getPhi(theta, ppl, -cw, de, kr)

    Nh_cw = np.array([math.cos(phi_cw), math.sin(phi_cw)])
    Nh_ccw = np.array([math.cos(phi_ccw), math.sin(phi_ccw)])

    arg = (abs(yl) * Nh_ccw + abs(yr) * Nh_cw) / (2 * de)

    if -de <= delta_y < de:
        omega = math.atan2(arg[1], arg[0])
    elif delta_y < -de:
        omega = getPhi(theta, ppl, cw, de, kr)
    else:
        omega = getPhi(theta, ppr, -cw, de, kr)

    print(omega)
    return omega

def getVectors(w, h, step):
    vectors = []
    for x in range(0, w, step):
        for y in range(0, h, step):
            omega = getOmega(spiral_center_x, spiral_center_y, x, y)
            vectors.append([math.cos(omega), math.sin(omega)])
    return vectors

def main():
    vectors = getVectors(w, h, step)
    vectorField = draw.drawVectorField(copy(field), vectors, w, h, step)
    cv2.imshow('field', vectorField)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    w, h = setArenaSize()
    # makes field background
    field = np.zeros((h, w, 3)) # colored image
    main()
