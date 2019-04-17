from calc_utils import *
from get_vectors import *
import cv2
import draw
from copy import copy
from constants import Const
from cm_pixels_conversions import *

def moveToGoal(origin, v_x, v_y):
    s_x, s_y = origin
    delta_x, delta_y = delta(s_x, s_y, v_x, v_y)
    th = theta(delta_x, delta_y)

    phi_tuf = phiTuf(th, delta_x, delta_y)
    return phi_tuf

   

if __name__ == '__main__':
    w, h = arena_w, arena_h
    px_w, px_h = setArenaSize()
    step = Const.step 


    field = np.zeros((px_h, px_w, 3))
    vectors = getVectors(w, h, step, moveToGoal)
    vectorField = draw.drawVectorField(copy(field), vectors, w, h, step)
    cv2.imshow('move to goal', vectorField)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
