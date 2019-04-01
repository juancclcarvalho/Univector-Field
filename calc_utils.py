import math

def getDelta(x1,y1,x2,y2):
    '''
    Calculates the x-axis variation
    Input:  x1 and x2: Initial and final x-axis and y-axis coordinates
    '''
    return x2 - x1, y2 - y1

def getDistance(d_x, d_y):
    '''
    Gets the distance vector (pp) between the spiral's central point and the vector origin
    Input:  q: Constant
            d_x: x-axis variation
    '''
    return math.sqrt((d_x**2) + (d_y**2))

def getTheta(d_x, d_y):
    '''
    Gets the theta angle between distance vector (pp) and the x-axis
    Input:  d_x: x-axis variation
            d_y: y-axis variation
    '''
    return math.atan2(d_y, d_x)

def getPhi(theta, pp, d, de, kr):
    if pp > de:
        phi = theta + d * (math.pi / 2) * (2 - ((de + kr) / (pp + kr)))
    elif pp >= 0 and pp <= de:
        phi = theta + d * (math.pi / 2) * math.sqrt(pp / de)

    return phi
