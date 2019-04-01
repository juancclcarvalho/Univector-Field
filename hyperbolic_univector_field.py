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

def calcPhi(s_x, s_y, v_x, v_y, d):
    '''
    Gets the phi angle between a given vector and the x-axis
    Input:  s_x: The spiral center x-axis coordinate
            s_y: The spiral center y-axis coordinate
            v_x: The vector origin x-axis coordinate
            v_y: The vector origin y-axis coordinate
    '''

    delta_x, delta_y = calc_utils.getDelta(s_x, s_y, v_x, v_y)
    pp = calc_utils.getDistance(delta_x, delta_y)
    theta = calc_utils.getTheta(delta_x, delta_y)

    return calc_utils.getPhi(theta, pp, d, de, kr)


def getVectors(w, h, step):
    vectors = []
    for i in range(0, w, step):
        for j in range(0, h, step):
            phi = calcPhi(spiral_center_x, spiral_center_y, i, j, direction)
            vectors.append([math.cos(phi), math.sin(phi)])
    return vectors


def main():
    vectors = getVectors(h, w, step)
    vectorField = draw.drawVectorField(copy(field), vectors, h, w, step)
    cv2.imshow('field', vectorField)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    h, w = 675, 585
    # makes field background
    field = np.zeros((w, h, 3)) # colored image
    main()
