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

q0 = robot.q_home
print(q0)
current_pose = robot.fk(robot.get_q())
print(current_pose)
print(current_pose[:3, 3])
current_pose[:3, 3] -= np.array([0.0, 0.2, 0.4])
print(current_pose)
ik_sols = robot.ik(current_pose)
print(ik_sols)
assert len(ik_sols) > 0
closest_solution = min(ik_sols, key=lambda q: np.linalg.norm(q - q0))
print(closest_solution)
robot.move_to_q(closest_solution)
robot.wait_for_motion_stop()
q_rad = robot.get_q()
q_deg = np.rad2deg(q_rad)
print(f"Position {q_deg}")
robot.close()
