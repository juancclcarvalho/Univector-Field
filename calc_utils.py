from math import cos, sin, pi
import math
import numpy as np
from constants import Const

kr = Const.kr
radius = Const.de
origin = (Const.spiral_center_x, Const.spiral_center_y)

def Nh(phi):
    return np.array([cos(phi), sin(phi)])

def wrapToPi(phi):
    '''
    Wrap a given angle to interval [-pi, pi]
    Input: (float) phi
    '''
    if phi > pi:
        return phi - 2 * pi
    if phi < -pi:
        return 2 * pi + phi
    else:
        return phi

def delta(x_1, y_1, x_2, y_2):
    '''
    Returns the x-axis and y-axis variation between two points
    Input: (tuple) origin - origin x-axis and y-axis coordinate
           (int) v_x - vector x-axis coordinate
           (int) v_y - vector y-axis coordinate
    '''

    return x_2 - x_1, y_2 - y_1

def theta(d_x, d_y):
    '''
    Returns the angle from x-axis at position p
    Input: (int) d_x - x-axis variation
           (int) d_y - y-axis variation
    '''
    return math.atan2(d_y, d_x)

def ro(d_x, d_y):
    '''
    Returns the distance between the origin and p
    '''
    return math.sqrt(d_x ** 2 + d_y ** 2)

def phiH(ro, theta, cw=False, radius=radius):
    if ro > radius:
        angle = (pi / 2) * (2 - ((radius + kr) / (ro + kr)))
    elif 0 <= ro <= radius:
        angle = (pi / 2) * math.sqrt(ro / radius)

    if cw:
        """ return wrapToPi(theta + angle) """
        return theta + angle
    else:
        """ return wrapToPi(theta - angle) """
        return theta - angle

def phiTuf(theta, d_x, d_y, radius=radius):
    y_l = d_y + radius
    y_r = d_y - radius

    ro_l = ro(d_x, d_y - radius)
    ro_r = ro(d_x, d_y + radius)

    phi_ccw = phiH(ro_l, theta, cw=True) #changed
    phi_cw = phiH(ro_r, theta, cw=False) #changed

    nh_ccw = Nh(phi_ccw)
    nh_cw = Nh(phi_cw)

    vec = (abs(y_l) * nh_ccw + abs(y_r) * nh_cw) / (2 * radius)

    if -radius <= d_y < radius:
        phi_tuf = math.atan2(vec[1], vec[0])
    elif d_y < -radius:
        phi_tuf = phiH(ro_l, theta, cw=False) #changed
    elif d_y >= radius:
        phi_tuf = phiH(ro_r, theta, cw=True) #changed

    return Nh(phi_tuf)





