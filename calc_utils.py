from math import *

def getDelta(x1,y1,x2,y2):
    '''
    Calculates the x-axis variation
    Input:  x1 and x2: Initial and final x-axis and y-axis coordinates
    '''
    return x2 - x1, y2 - y1

def getDistance(d_x, d_y):
    '''
    Gets the distance vector (ro) between the spiral's central point and the vector origin
    Input:  q: Constant
            d_x: x-axis variation
    '''
    return sqrt((d_x**2) + (d_y**2))

def getTheta(d_x, d_y):
    '''
    Gets the theta angle between distance vector (ro) and the x-axis
    Input:  d_x: x-axis variation
            d_y: y-axis variation
    '''
    return atan2(d_y, d_x)

def getPhi_h(theta, ro, dir, de, kr):
    if ro > de:
        phi = theta + dir * (pi / 2) * (2 - ((de + kr) / (ro + kr)))
    else:
        phi = theta + dir * (pi / 2) * sqrt(ro / de)

    if dir:
        wrapped_phi = wrap_to_pi(theta + phi)
    else:
        wrapped_phi = wrap_to_pi(theta - phi)
    return phi, wrapped_phi

def wrap_to_pi(theta):
    if theta > pi:
        return theta - 2*pi
    if theta < -pi:
        return 2*pi + theta
    else:
        return theta

def getPhi_tuf():
    pass

