from utils.utils import activate_franka_conda_env

activate_franka_conda_env(__file__)

import time
from franky import Robot, ControllerMode, CartesianMotion, CartesianStopMotion

IP = "172.16.0.2"

def safe_stop(robot):
    # Always try to stop + join, even if already stopped / error happened
    try:
        robot.move(CartesianStopMotion(), asynchronous=True)
        robot.join_motion()
    except Exception:
        pass

robot = Robot(IP, controller_mode=ControllerMode.CartesianImpedance)
robot.recover_from_errors()
robot.relative_dynamics_factor = 0.02  # keep it slow

try:
    for name, cart_imp in [
        ("SOFT",  [100.0, 100.0, 100.0, 10.0, 10.0, 10.0]),
        ("STIFF", [2000.0, 2000.0, 2000.0, 200.0, 200.0, 200.0]),
    ]:
        safe_stop(robot)  # ensure we're NOT in "Move" mode

        input(f"\nPress Enter to apply {name} cartesian impedance...")
        robot.set_cartesian_impedance(cart_imp)  # must be called while idle

        # Start a continuous hold at the current pose
        print(robot.current_cartesian_state)
        # CartesianState(pose=RobotPose(ee_pose=Affine(t=[0.294356 -0.00349334 0.164831], q=[0.99984 -0.00532383 -0.016491 -0.00436257]), elbow=ElbowState(joint_3_pos=-0.0137737, joint_4_flip=FlipDirection.Negative)), velocity=RobotVelocity(ee_twist=Twist(lin=[0 0 0], ang=[0 0 0]), elbow_vel=0))
        hold = CartesianMotion(robot.current_cartesian_state, return_when_finished=False)
        robot.move(hold, asynchronous=True)

        input(f"{name} holding active. Gently push EE, then press Enter to stop...")
        safe_stop(robot)
        time.sleep(0.2)

finally:
    safe_stop(robot)