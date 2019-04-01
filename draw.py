import cv2
import numpy as np

def drawVector(field, origin, end):
    # rgb -> bgr
    cv2.arrowedLine(field, origin, end, (0, 0, 255), 1)
    cv2.circle(field, (290, 290), 5, (0, 255, 255), -1)

def drawVectorField(field, vectors, w, h, step):
    length = 25
    k = 0
    for i in range(0, w, step):
        for j in range(0, h, step):
            origin = (i, j)
            end = np.array([i, j]) + length * np.array(vectors[k])
            end = (int(end[0]), int(end[1]))
            drawVector(field, origin, end)
            k += 1
            if k >= len(vectors) : return field
    return field
