import debug
import math_utils
from abstract_module import measures
from typing import List, Tuple
import univector

obstacle = list([measures.obstacle])

def avoidObstacles(r_x: int, r_y: int, __, obs_pos: Tuple[int, int]) -> List[float]:
    
    obs_x, obs_y = obs_pos[0]
    robot_obs_x, robot_obs_y = math_utils.delta_axis(obs_x, obs_y, r_x, r_y)
    robot_obs_dist = math_utils.norm(robot_obs_x, robot_obs_y)
    phi_auf = univector.phiAuf(obs_x, obs_y, r_x, r_y, robot_obs_dist)

    return univector.Nh(phi_auf)

if __name__ == '__main__':
    debug.debug('avoid obstacles', avoidObstacles, None, obstacle)