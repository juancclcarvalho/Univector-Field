import numpy as np
import math
import cv2
from copy import copy
import calc_utils
import draw
import constants

spiral_center_x = constants.Const.spiral_center_x
spiral_center_y = constants.Const.spiral_center_y
direction = constants.Const.direction
de = constants.Const.de
kr = constants.Const.kr
step = constants.Const.step
cw = 1
ccw = -1


def getPhi_TUF(s_x, s_y, v_x, v_y):

    delta_x, delta_y = calc_utils.getDelta(s_x, s_y, v_x, v_y)

    # get Y
    yl = delta_y + de
    yr = delta_y - de

    #                           /*        pl        */
    ro_l = calc_utils.getDistance(delta_x, delta_y - de)
    #                           /*        pr        */
    ro_r = calc_utils.getDistance(delta_x, delta_y + de)

    theta = calc_utils.getTheta(delta_x, delta_y)

    __, phi_cw = calc_utils.getPhi_h(theta, ro_r, cw, de, kr)
    __, phi_ccw = calc_utils.getPhi_h(theta, ro_l, -cw, de, kr)
    print(phi_cw)
    
    Nh_cw = np.array([math.cos(phi_cw), math.sin(phi_cw)])
    Nh_ccw = np.array([math.cos(phi_ccw), math.sin(phi_ccw)])

    arg = (abs(yl) * Nh_ccw + abs(yr) * Nh_cw) / (2 * de)

    if -de <= delta_y < de:
        phi_tuf = math.atan2(arg[1], arg[0])
        print(1)
        print(delta_y)
    elif delta_y < -de:
        __, phi_tuf = calc_utils.getPhi_h(theta, ro_l, cw, de, kr)
        print(2)
        print(delta_y)
    elif delta_y >= de:
        __, phi_tuf = calc_utils.getPhi_h(theta, ro_r, -cw, de, kr)
        print(3)
        print(delta_y)

    return phi_tuf


def getVectors(w, h, step):
    vectors = []
    for i in range(0, w, step):
        for j in range(0, h, step):
            phi_tuf = getPhi_TUF(spiral_center_x, spiral_center_y, i, j)
            vectors.append([math.cos(phi_tuf), math.sin(phi_tuf)])
    return vectors
    


if __name__ == '__main__':
    h, w = 675, 585
    # makes field background
    field = np.zeros((w, h, 3))  # colored image
    vectors = getVectors(h, w, step)
    vectors = getVectors(h, w, step)
    vectors = getVectors(h, w, step)
    vectorField = draw.drawVectorField(copy(field), vectors, h, w, step)
    cv2.imshow('field', vectorField)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
