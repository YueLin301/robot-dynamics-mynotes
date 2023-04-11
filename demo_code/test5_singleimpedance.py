import math
import numpy as np
import sys
from librhext3_v6 import *

if __name__ == '__main__':
    unityqueue = []
    arhext3 = rhext3(r=0.08, gear_rate=2, unityqueue=unityqueue)
    arhext3.id_list = [1]
    arhext3.init()
    id_list = arhext3.id_list
    arhext3.switch_mode(id_list, 'cur')

    while True:
        vel = arhext3.get_velocitys(id_list)
        q_raw = arhext3.get_positions(id_list)
        # q_raw = np.array(q_raw)
        q = q_raw[0] / 2048.0 * math.pi
        dq = vel[0] / 2048.0 * math.pi

        dx = q - 0
        # tau = -dx
        # tau = -0.1 * dx - 0.3*dq
        tau = -0.3 * dq
        cur = arhext3.torqueTocurrent(tau)
        cur = [np.array([cur])]
        arhext3.set_currents(id_list, cur)

        read_cur = arhext3.get_currents(id_list)
        print(read_cur,q_raw)
