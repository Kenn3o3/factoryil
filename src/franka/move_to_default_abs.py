#!/usr/bin/env python3
"""Move Franka robot to default pose."""

from franky import *

# Connect to robot
robot = Robot("172.16.0.2")
robot.recover_from_errors()

# Connect to gripper
gripper = Gripper("172.16.0.2")

# Display initial state
print("=" * 50)
print("INITIAL STATE")
print("=" * 50)
current_state = robot.current_cartesian_state
ee_pose = current_state.pose.end_effector_pose
pos = ee_pose.translation
quat = ee_pose.quaternion
print(f"End-effector position: [{pos[0]:.3f}, {pos[1]:.3f}, {pos[2]:.3f}]")
print(f"End-effector quaternion: [{quat[0]:.3f}, {quat[1]:.3f}, {quat[2]:.3f}, {quat[3]:.3f}]")

gripper_state = gripper.state
print(f"Gripper width: {gripper_state.width:.3f} m")
print(f"Gripper max_width: {gripper_state.max_width:.3f} m")
print(f"Gripper temperature: {gripper_state.temperature}°C")
print("=" * 50)

# Set dynamics to 5% for slower, smoother motion
# Lower values = slower (range: 0.0 to 1.0)
# Try 0.05 for slower, 0.02 for very slow
robot.relative_dynamics_factor = 0.04

# Define target pose: [x, y, z, qw, qx, qy, qz]
# Position: [0.7, 0.3, 0.582] meters
# Quaternion: [1, 0, 0, 0] (w, x, y, z) - no rotation
target_pose = Affine([0.5, 0.0, 0.2], [1.0, 0.0, 0.0, 0.0])

print(f"Moving to default pose: position=[0.5, 0.0, 0.2], quaternion=[1, 0, 0, 0]")

# Create and execute motion (absolute by default)
motion = CartesianMotion(target_pose)
robot.move(motion)

print("✓ Reached default pose!")

# Gripper control examples
speed = 0.05  # [m/s]
force = 0.5  # [N]

# Open the gripper
print("Opening gripper...")
gripper.open(speed)

# Grasp an object (closes until it detects resistance)
# print("Grasping object...")
# success = gripper.grasp(0.0, speed, force, epsilon_outer=0.1)
# print("success: ", success)

# Display final state
print("=" * 50)
print("FINAL STATE")
print("=" * 50)
current_state = robot.current_cartesian_state
ee_pose = current_state.pose.end_effector_pose
pos = ee_pose.translation
quat = ee_pose.quaternion
print(f"End-effector position: [{pos[0]:.3f}, {pos[1]:.3f}, {pos[2]:.3f}]")
print(f"End-effector quaternion: [{quat[0]:.3f}, {quat[1]:.3f}, {quat[2]:.3f}, {quat[3]:.3f}]")

gripper_state = gripper.state
print(f"Gripper width: {gripper_state.width:.3f} m")
print(f"Gripper max_width: {gripper_state.max_width:.3f} m")
print(f"Gripper temperature: {gripper_state.temperature}°C")
print("=" * 50)
