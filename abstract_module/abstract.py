import math_utils
import numpy as np
from typing import List, Tuple

def closerObstacle(x: int, y: int, obstacles: List[Tuple[int, int]]) -> Tuple[int, int]:

    last_ro = 0
    count = 0
    for obstacle in obstacles:
        obs_x, obs_y = obstacle
        delta_x, delta_y = math_utils.delta_axis(x, y, obs_x, obs_y)
        if not count:
            last_ro = math_utils.norm(delta_x, delta_y)
        if (math_utils.norm(delta_x, delta_y) <= last_ro):
            closer_obs = obstacle
            last_ro = math_utils.norm(delta_x, delta_y)
        count += 1
        
    return closer_obs

def v_robot():
    v_robot = np.array([0, 0])

    return np.array([0, 0])

def v_obstacle():
    v_obstacle = np.array([0, 0])

    return v_obstacle