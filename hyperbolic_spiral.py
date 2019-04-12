from calc_utils import *
from get_vectors import *
import cv2
import draw
from copy import copy
from cm_pixels_conversions import *
from constants import Const

def hyperbolicSpiral(origin, v_x, v_y):
    s_x, s_y = origin
    delta_x, delta_y = delta(s_x, s_y, v_x, v_y)
    th = theta(delta_x, delta_y) 
    p = ro(delta_x, delta_y)
    phi_h = phiH(p, th)
    nh = Nh(phi_h)

    return nh


if __name__ == '__main__':
    w, h = arena_w, arena_h
    px_w, px_h = setArenaSize()
    step = Const.step


    field = np.zeros((px_h, px_w, 3))
    vectors = getVectors(w, h, step, hyperbolicSpiral)
    vectorField = draw.drawVectorField(copy(field), vectors, w, h, step)
    cv2.imshow('hyperbolic', vectorField)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    
