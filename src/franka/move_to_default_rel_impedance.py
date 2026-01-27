#!/usr/bin/env python3
"""Move Franka robot using relative Cartesian motions in Cartesian impedance mode.

Notes:
- Relative motions are defined in the *current end-effector frame* (per franky docs).
- We set internal impedance via set_cartesian_impedance / set_joint_impedance.
- Optional hold at the end keeps the Cartesian controller running so you can feel stiffness
  (relevant to issues like #10 and #73).
"""

from franky import *

ROBOT_IP = "172.16.0.2"

# ----------------------------
# User-tunable parameters
# ----------------------------

RELATIVE_DYNAMICS_FACTOR = 0.02

CARTESIAN_IMPEDANCE = [50.0, 50.0, 50.0, 20.0, 20.0, 20.0]  # [N/m, Nm/rad]
JOINT_IMPEDANCE = [200.0] * 7  # [Nm/rad]

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
robot.set_cartesian_impedance(CARTESIAN_IMPEDANCE)
robot.set_joint_impedance(JOINT_IMPEDANCE)

print("Impedance settings:")
print(f"  Cartesian impedance [N/m, Nm/rad]: {CARTESIAN_IMPEDANCE}")
print(f"  Joint impedance [Nm/rad]: {JOINT_IMPEDANCE}")
print(f"  Relative dynamics factor: {RELATIVE_DYNAMICS_FACTOR}")

# ----------------------------
# Relative motions
# ----------------------------

print("\n1. Moving 10cm in +X direction (relative EE frame)...")
robot.move(CartesianMotion(Affine([0.10, 0.00, 0.00]), ReferenceType.Relative))
print("✓ Completed")

print("\n2. Moving 5cm in +Y direction (relative EE frame)...")
robot.move(CartesianMotion(Affine([0.00, 0.05, 0.00]), ReferenceType.Relative))
print("✓ Completed")

print("\n3. Moving 5cm in +Z direction (relative EE frame)...")
robot.move(CartesianMotion(Affine([0.00, 0.00, 0.05]), ReferenceType.Relative))
print("✓ Completed")

print("\n4. Moving back: -10cm X, -5cm Y, -5cm Z (relative EE frame)...")
robot.move(CartesianMotion(Affine([-0.10, -0.05, -0.05]), ReferenceType.Relative))
print("✓ Completed - returned to starting position (approximately)")

# ----------------------------
# Gripper
# ----------------------------

speed = 0.05  # [m/s]
print("\nOpening gripper...")
gripper.open(speed)
print("✓ Gripper opened")

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
        try:
            robot.move(CartesianStopMotion())
        finally:
            robot.join_motion()

# ----------------------------
# Print final state
# ----------------------------

print("\n" + "=" * 60)
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