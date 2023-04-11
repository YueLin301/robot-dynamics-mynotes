import math
import numpy as np
import sys
import time
from librhext3_v6 import *

if __name__ == '__main__':
    unityqueue = []
    arhext3 = rhext3(r=0.08, gear_rate=2, unityqueue=unityqueue)
    arhext3.id_list = [1]
    arhext3.init()
    id_list = arhext3.id_list
    arhext3.switch_mode(id_list, 'poscur')

    t0 = time.time()
    durt = 60

    while time.time() - t0 < durt:
        t = time.time() - t0
        qd = 300*t
        arhext3.set_positions(id_list, [qd])

        # arhext3.set_currents(id_list,[np.array([1])])
        # arhext3.set_currents(id_list,[np.array([50])])
        # arhext3.set_currents(id_list,[np.array([15])])

        vel = arhext3.get_velocitys(id_list)
        q_raw = arhext3.get_positions(id_list)
        dx = q_raw[0] - qd
        # q_raw = np.array(q_raw)
        dx = dx / 2048.0 * math.pi
        dq = vel[0] / 2048.0 * math.pi

        tau = -0.05*dx
        # tau = -0.1 * dx - 0.3*dq
        # tau = -0.3 * dq
        cur = arhext3.torqueTocurrent(tau)
        cur = [np.array([cur])]
        arhext3.set_currents(id_list, cur)

        read_cur = arhext3.get_currents(id_list)
        print(read_cur)
