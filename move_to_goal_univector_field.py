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

def getOmega(s_x, s_y, v_x, v_y):

    delta_x, delta_y = calc_utils.getDelta(s_x, s_y, v_x, v_y)

    # get Y
    yl = delta_y + de
    yr = delta_y - de

    #                           /*        pl        */
    ppl = calc_utils.getDistance(delta_x, delta_y - de)
    #                           /*        pr        */
    ppr = calc_utils.getDistance(delta_x, delta_y + de)

    theta = calc_utils.getTheta(delta_x, delta_y)

    phi_cw = calc_utils.getPhi(theta, ppr, cw, de, kr)
    phi_ccw = calc_utils.getPhi(theta, ppl, ccw, de, kr)

    Nh_cw = np.array([math.cos(phi_cw), math.sin(phi_cw)])
    Nh_ccw = np.array([math.cos(phi_ccw), math.sin(phi_ccw)])

    arg = (yl * Nh_ccw + yr * Nh_cw) / (2 * de)

    if -de <= delta_y < de:
        omega = math.atan2(arg[1], arg[0])
    elif delta_y < -de:
        omega = calc_utils.getPhi(theta, ppl, cw, de, kr)
    elif delta_y >= de:
        omega = calc_utils.getPhi(theta, ppr, ccw, de, kr)

    print(v_x, v_y)


    return omega

def getVectors(w, h, step, n):
    vectors = []
    for i in range(0, w, step):
        for j in range(0, h, step):
            omega = getOmega(spiral_center_x, spiral_center_y, j, n - i)
            vectors.append([math.cos(omega), math.sin(omega)])
    return vectors

def main():
    vectors = getVectors(h, w, step, n)
    vectorField = draw.drawVectorField(copy(field), vectors, h, w, step)
    cv2.imshow('field', vectorField)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    h, w = 675, 585
    n = w
    # makes field background
    field = np.zeros((w, h, 3)) # colored image
    main()
