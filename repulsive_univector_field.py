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

def getVectors(w, h, step):
    vectors = []
    for i in range(0, w, step):
        for j in range(0, h, step):
            delta_x, delta_y = calc_utils.getDelta(spiral_center_x, spiral_center_y, i, j)
            theta = calc_utils.getTheta(delta_x, delta_y)
            vectors.append([math.cos(theta), math.sin(theta)])
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
