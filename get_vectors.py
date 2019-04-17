from constants import Const
from vector_log import *

def getVectors(w, h, step, get_vec):
    vectors = []
    origin = (Const.spiral_center_x, Const.spiral_center_y)
    logInit('vectors_log')
    for x in range(0, w, step):
        for y in range(0, h, step):
            vector = get_vec(origin, x, y)
            vectors.append(vector)
            logAppend('x: , {}, y: , {}, {}'.format(x, y, vector))
    logClose()
    return vectors
