from abstract_module import measures
import debug
import math_utils
from typing import List, Tuple
import univector

ball = measures.ball

def moveToGoal(r_x: int, r_y: int, ball_pos: Tuple[int, int]) -> List[float]:

    ball_x, ball_y = ball_pos
    delta_x, delta_y = math_utils.delta_axis(ball_x, ball_y, r_x, r_y)
    theta = univector.phiR(delta_x, delta_y)
    phi_tuf = univector.phiTuf(theta, delta_x, delta_y)

    return univector.Nh(phi_tuf)

if __name__ == '__main__':
    debug.debug('move to goal', moveToGoal, ball, None)
