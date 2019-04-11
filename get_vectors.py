from constants import Const

def getVectors(w, h, step, get_vec):
    vectors = []
    origin = (Const.spiral_center_x, Const.spiral_center_y)
    for x in range(0, w, step):
        for y in range(0, h, step):
            vector = get_vec(origin, x, y)
            vectors.append(vector)
    return vectors
