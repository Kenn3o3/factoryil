#!/usr/bin/env python3
"""Move Franka robot to a default pose (absolute) using Cartesian impedance control.

Key points (from franky docs + related issues):
- We run in ControllerMode.CartesianImpedance and set stiffness via set_cartesian_impedance().
- Cartesian impedance is only "felt" while a Cartesian controller is actively running.
  Therefore, we optionally keep holding the final pose with return_when_finished=False
  (helps with "stiffness doesn't change" observations and "continuous impedance" requests).
- Large target jumps can lead to oscillations/noise in impedance mode -> we split big
  translations into smaller steps (issue #30).
"""

from franky import *
import math

ROBOT_IP = "172.16.0.2"

# ----------------------------
# User-tunable parameters
# ----------------------------

# Slow = safer/smoother.
RELATIVE_DYNAMICS_FACTOR = 0.01

# Internal Franka Cartesian impedance (libfranka):
# [x, y, z, Rx, Ry, Rz] = [N/m, N/m, N/m, Nm/rad, Nm/rad, Nm/rad]
# Start moderate; too high stiffness + large pose jump can cause oscillations.
CARTESIAN_IMPEDANCE = [50.0, 50.0, 50.0, 20.0, 20.0, 20.0]

# Internal Franka joint impedance (libfranka): 7 values [Nm/rad]
JOINT_IMPEDANCE = [200.0] * 7

# Absolute target position in base frame [m]
TARGET_POSITION = [0.5, 0.0, 0.2]

# Break large translations into smaller steps to reduce oscillations/noise in impedance mode
MAX_TRANSLATION_STEP = 0.10  # [m]

# Keep holding pose in Cartesian control so you can "feel" the impedance settings
ENABLE_IMPEDANCE_HOLD = True

# ----------------------------
# Connect to robot
# ----------------------------

robot = Robot(
    fci_hostname=ROBOT_IP,
    controller_mode=ControllerMode.CartesianImpedance,
)
robot.recover_from_errors()

gripper = Gripper(ROBOT_IP)

# ----------------------------
# Print initial state
# ----------------------------

print("=" * 60)
print("INITIAL STATE")
print("=" * 60)
current_state = robot.current_cartesian_state
ee_pose = current_state.pose.end_effector_pose
pos = ee_pose.translation
quat = ee_pose.quaternion

print(f"End-effector position [m]: [{pos[0]:.3f}, {pos[1]:.3f}, {pos[2]:.3f}]")
print(f"End-effector quaternion [x,y,z,w]: [{quat[0]:.3f}, {quat[1]:.3f}, {quat[2]:.3f}, {quat[3]:.3f}]")

g = gripper.state
print(f"Gripper width: {g.width:.3f} m")
print(f"Gripper max_width: {g.max_width:.3f} m")
print(f"Gripper temperature: {g.temperature}°C")
print("=" * 60)

# ----------------------------
# Configure dynamics + impedance
# ----------------------------

robot.relative_dynamics_factor = RELATIVE_DYNAMICS_FACTOR

# These affect Franka's *internal* impedance controller (libfranka API)
robot.set_cartesian_impedance(CARTESIAN_IMPEDANCE)
robot.set_joint_impedance(JOINT_IMPEDANCE)

print("Impedance settings:")
print(f"  Cartesian impedance [N/m, Nm/rad]: {CARTESIAN_IMPEDANCE}")
print(f"  Joint impedance [Nm/rad]: {JOINT_IMPEDANCE}")
print(f"  Relative dynamics factor: {RELATIVE_DYNAMICS_FACTOR}")

# ----------------------------
# Build target pose
# ----------------------------

# Safety / robustness: keep the current orientation to avoid unexpected flips
# due to quaternion convention misunderstandings.
target_quat = [float(quat[0]), float(quat[1]), float(quat[2]), float(quat[3])]
print(f"Target position (absolute): {TARGET_POSITION}")
print(f"Keeping current orientation quaternion [x,y,z,w]: {target_quat}")

# ----------------------------
# Move to target (split if far)
# ----------------------------

start_pos = [float(pos[0]), float(pos[1]), float(pos[2])]
delta = [TARGET_POSITION[i] - start_pos[i] for i in range(3)]
dist = math.sqrt(sum(d * d for d in delta))

n_steps = max(1, math.ceil(dist / MAX_TRANSLATION_STEP))
if n_steps > 1:
    print(f"Target is {dist:.3f} m away -> moving in {n_steps} steps (<= {MAX_TRANSLATION_STEP:.2f} m each).")

for k in range(1, n_steps + 1):
    alpha = k / n_steps
    pos_k = [start_pos[i] + alpha * delta[i] for i in range(3)]
    pose_k = Affine(pos_k, target_quat)
    robot.move(CartesianMotion(pose_k))
    print(f"  ✓ Step {k}/{n_steps}: position={pos_k}")

print("✓ Reached target pose!")

# ----------------------------
# Gripper examples (same as your original)
# ----------------------------

speed = 0.05  # [m/s]
force = 0.5   # [N]

print("Opening gripper...")
gripper.open(speed)

print("Grasping object... (disabled by default)")
# success = gripper.grasp(0.0, speed, force, epsilon_outer=0.1)
# print("success:", success)

# ----------------------------
# Optional: keep holding pose in impedance mode
# ----------------------------

if ENABLE_IMPEDANCE_HOLD:
    hold_pose = robot.current_cartesian_state.pose.end_effector_pose
    print("\nHolding pose in Cartesian impedance mode (press Enter to stop)...")

    try:
        hold_motion = CartesianMotion(hold_pose, return_when_finished=False)
        robot.move(hold_motion, asynchronous=True)

        try:
            input()
        except KeyboardInterrupt:
            pass

    finally:
        # Preempt the hold with a stop motion in the SAME control mode (cartesian pose)
        try:
            robot.move(CartesianStopMotion())
        finally:
            # Ensures async exceptions (if any) get raised in the main thread
            robot.join_motion()

# ----------------------------
# Print final state
# ----------------------------

print("=" * 60)
print("FINAL STATE")
print("=" * 60)
current_state = robot.current_cartesian_state
ee_pose = current_state.pose.end_effector_pose
pos = ee_pose.translation
quat = ee_pose.quaternion

print(f"End-effector position [m]: [{pos[0]:.3f}, {pos[1]:.3f}, {pos[2]:.3f}]")
print(f"End-effector quaternion [x,y,z,w]: [{quat[0]:.3f}, {quat[1]:.3f}, {quat[2]:.3f}, {quat[3]:.3f}]")

g = gripper.state
print(f"Gripper width: {g.width:.3f} m")
print(f"Gripper max_width: {g.max_width:.3f} m")
print(f"Gripper temperature: {g.temperature}°C")
print("=" * 60)