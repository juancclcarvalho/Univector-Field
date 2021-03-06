from abstract_module import measures
import debug
import math_utils
from typing import List, Tuple
import univector

ball = measures.ball

def hyperbolic(r_x: int, r_y: int, ball_pos: Tuple[int, int]) -> List[float]:
    
    ball_x, ball_y = ball_pos
    delta_x, delta_y = math_utils.delta_axis(ball_x, ball_y, r_x, r_y)
    theta = univector.phiR(delta_x, delta_y)
    rho = math_utils.norm(delta_x, delta_y)
    phi_h = univector.phiH(rho, theta)

    return univector.Nh(phi_h)

if __name__ == '__main__':
    debug.debug('hyperbolic', hyperbolic, ball, None)

