import math
import numpy as np
from librhext3_v6 import *

if __name__ == '__main__':
    unityqueue = []
    arhext3 = rhext3(r=0.08, gear_rate=2, unityqueue=unityqueue)
    arhext3.init()
    id_list = arhext3.id_list
    arhext3.switch_mode(id_list, 'poscur')

    fkine = fkine(r=0.08)

    while True:

        vel = arhext3.get_velocitys(id_list)
        q_raw = arhext3.get_positions(id_list)
        q_raw = np.array(q_raw)
        q = q_raw / 2048.0 * math.pi

        # print('q_raw',q_raw)
        # print('q',q)

        jds = []
        x = []
        tau = []
        cur = []
        for i in range(0, 12, 2):
            while q[i] > 2 * math.pi:
                q[i] -= 2 * math.pi
            while q[i] < 0:
                q[i] += 2 * math.pi
            while q[i+1] < q[i]:
                q[i+1] += 2 * math.pi
            while q[i+1] - q[i] > 2 * math.pi:
                q[i+1] -= 2 * math.pi

            jd = fkine.jacobe(q[i], q[i + 1])
            jds.append(jd)
            xd, yd = fkine.dpoint(q[i], q[i + 1])
            x.append(xd-0)
            x.append(yd+0.16)

            tau = - np.transpose(jd) @ np.array([[xd-0], [yd+0.16]])
            tau1 = tau[0]
            tau2 = tau[1]

            cur.append(arhext3.torqueTocurrent(tau1/10))
            cur.append(arhext3.torqueTocurrent(tau2/10))
        arhext3.set_currents(id_list, cur)


        read_cur = arhext3.get_currents(id_list)
        print(read_cur)
