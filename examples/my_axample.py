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

"""q_deg = np.array([0,0,0,0,-20,0])
q_rad = np.deg2rad(q_deg)
q = robot.get_q()
print(q)
robot.move_to_q(q+q_rad)"""

current_pose = robot.fk(robot.get_q())
print(current_pose)
print(current_pose[:3, 3])
current_pose = np.eye(4)
theta = np.pi/2
orientation_z = np.array([[np.cos(theta), -np.sin(theta), 0.0],
                         [np.sin(theta), np.cos(theta),0.0],
                        [0.0,0.0,1.0]])

orientation_y = ([[np.cos(theta),0.0,np.sin(theta)],
                  [0.0,1.0,0.0],
                  [-np.sin(theta),0.0,np.cos(theta)],])

orientation_x = np.array([[1.0,0.0,0.0],
                          [0.0,np.cos(theta),-np.sin(theta)],
                          [0.0,np.sin(theta),np.cos(theta)]])

current_pose[:3, 3] = robot.fk(robot.get_q())[:3, 3]
print(current_pose)
current_pose[:3, :3] = orientation_y
ik_sols = robot.ik(current_pose)
print([(i,sol) for i,sol in enumerate(ik_sols)])
valid_sols = [q for q in ik_sols if robot.in_limits(q)]
print(valid_sols)
assert len(valid_sols) > 0
#closest_solution = min(ik_sols, key=lambda q: np.linalg.norm(q - q0))
closest_solution = valid_sols[1]
print(closest_solution)
robot.move_to_q(closest_solution)
robot.wait_for_motion_stop()
q_rad = robot.get_q()
q_deg = np.rad2deg(q_rad)
current_pose = robot.fk(robot.get_q())
print(current_pose[:3, 3])
robot.close()
