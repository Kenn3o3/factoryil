#!/usr/bin/env python3
"""Move Franka robot using relative motions."""

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
robot.relative_dynamics_factor = 0.04

# Perform a series of relative motions
print("\n1. Moving 10cm in +X direction (forward)...")
motion1 = CartesianMotion(Affine([0.1, 0.0, 0.0]), ReferenceType.Relative)
robot.move(motion1)
print("✓ Completed")

print("\n2. Moving 5cm in +Y direction (left)...")
motion2 = CartesianMotion(Affine([0.0, 0.05, 0.0]), ReferenceType.Relative)
robot.move(motion2)
print("✓ Completed")

print("\n3. Moving 5cm in +Z direction (up)...")
motion3 = CartesianMotion(Affine([0.0, 0.0, 0.05]), ReferenceType.Relative)
robot.move(motion3)
print("✓ Completed")

print("\n4. Moving back: -10cm X, -5cm Y, -5cm Z...")
motion4 = CartesianMotion(Affine([-0.1, -0.05, -0.05]), ReferenceType.Relative)
robot.move(motion4)
print("✓ Completed - returned to starting position")

# Gripper control
speed = 0.05  # [m/s]

print("\nOpening gripper...")
gripper.open(speed)
print("✓ Gripper opened")

# Display final state
print("\n" + "=" * 50)
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
