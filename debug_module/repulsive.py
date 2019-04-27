from abstract_module import measures
import debug
import math_utils
from typing import List, Tuple
import univector

obstacle = list([measures.obstacle])

def repulsive(r_x: int, r_y: int, __, obs_pos: Tuple[int, int]) -> List[float]:
    
    obs_x, obs_y = obs_pos[0]
    delta_x, delta_y = math_utils.delta_axis(obs_x, obs_y, r_x, r_y)
    phi_r = univector.phiR(delta_x, delta_y)

    return univector.Nh(phi_r)

if __name__ == '__main__':
    debug.debug('repulsive', repulsive, None, obstacle)