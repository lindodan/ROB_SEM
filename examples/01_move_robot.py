#!/usr/bin/env python
#
# Copyright (c) CTU -- All Rights Reserved
# Created on: 2024-10-31
#     Author: Vladimir Petrik <vladimir.petrik@cvut.cz>
#
import numpy as np
from ctu_crs import CRS93

robot = CRS93()
robot.initialize()

#q0 = robot.q_home
q_rad = robot.get_q()
q_deg = np.rad2deg(q_rad)
print(f"Position {q_deg}")

q_deg = np.array([-180,0,0,0,0,0])
q_rad = np.deg2rad(q_deg)
q = robot.get_q()
print(q)
robot.move_to_q(q+q_rad)
robot.wait_for_motion_stop()
print(robot.in_motion())
q_rad = robot.get_q()
q_deg = np.rad2deg(q_rad)
print(f"Position {q_deg}")

"""for i in range(len(q0)):
    q = q0.copy()
    q[i] += np.deg2rad(10)
    robot.move_to_q(q)
"""
robot.close()
