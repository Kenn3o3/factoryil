import time
from franky import Robot, CartesianMotion, CartesianStopMotion

IP = "172.16.0.2"

def safe_stop(robot):
    try:
        robot.move(CartesianStopMotion(), asynchronous=True)
        robot.join_motion()
    except Exception:
        pass

robot = Robot(IP)  # default controller_mode is joint impedance ([timschneider42.github.io](https://timschneider42.github.io/franky/robot_8hpp_source.html))
robot.recover_from_errors()
robot.relative_dynamics_factor = 0.02

try:
    for name, joint_imp in [
        ("SOFT",  [50.0]*7),
        ("STIFF", [3000.0]*7),
    ]:
        safe_stop(robot)

        input(f"\nPress Enter to apply {name} joint impedance...")
        robot.set_joint_impedance(joint_imp)

        hold = CartesianMotion(robot.current_cartesian_state, return_when_finished=False)
        robot.move(hold, asynchronous=True)

        input(f"{name} holding active. Push EE, then press Enter to stop...")
        safe_stop(robot)
        time.sleep(0.2)

finally:
    safe_stop(robot)