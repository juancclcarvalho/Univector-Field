from abstract_module import measures
from copy import copy
import cv2
from draw_module import draw
import numpy as np
from typing import List, Tuple


def debug(name: str, univector_field, ball: Tuple[int, int], obstacles: List[Tuple[int, int]]) -> None:

    w, h = measures.arena_w, measures.arena_h
    px_w, px_h = measures.getArenaSize()
    step = measures.step
    
    #field = np.zeros((px_h, px_w, 3))
    field = np.full((px_h, px_w, 3), 255, dtype=np.uint8)
    vectors = getVectors(w, h, step, univector_field, ball, obstacles)
    vectorField = draw.drawVectorField(copy(field), vectors, w, h, step, ball, obstacles)

    cv2.imshow('{}'.format(name), vectorField)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getVectors(w: int, h: int, step: int, get_vec, ball: Tuple[int, int], obstacles: List[Tuple[int, int]]=None) -> List[List[float]]:
    
    vectors = []
    for x in range(0, w, step):
        for y in range(0, h, step):
            if obstacles is None:
                vector = get_vec(x, y, ball)
            else:
                vector = get_vec(x, y, ball, obstacles)
            vectors.append(vector)

    return vectors