import time
import franky
from franky import (
    Robot, Gripper, Affine, ReferenceType,
    CartesianMotion, CartesianStopMotion,
    Measure, Reaction, ControllerMode
)

IP = "172.16.0.2"

DYN = 0.02
STEP_M = 0.001
MAX_DOWN_M = 0.08

# Sliding impedance (start here)
K_SLIDE = [150.0, 150.0, 1500.0, 200.0, 200.0, 20.0]

# Safety limits (do NOT set these too high; tune carefully)
FZ_MAX = 25.0     # N
FXY_MAX = 20.0    # N
TXY_MAX = 3.0     # Nm

def main():
    robot = Robot(IP, controller_mode=ControllerMode.CartesianImpedance)
    gripper = Gripper(IP)

    robot.recover_from_errors()
    robot.relative_dynamics_factor = DYN

    # Close gripper
    gripper.move(0.0, 0.02)

    # Set sliding impedance BEFORE moving
    robot.set_cartesian_impedance(K_SLIDE)

    input("Object fixed below. Clear workspace. Press Enter to start sliding descent...")

    total = 0.0
    try:
        while total < MAX_DOWN_M:
            motion = CartesianMotion(Affine([0.0, 0.0, -STEP_M]), ReferenceType.Relative)

            # Only stop on "too much" load (safety), not on first contact
            stop = CartesianStopMotion()
            motion.add_reaction(Reaction(Measure.FORCE_Z > FZ_MAX, stop))
            motion.add_reaction(Reaction(Measure.FORCE_X > FXY_MAX, stop))
            motion.add_reaction(Reaction(Measure.FORCE_X < -FXY_MAX, stop))
            motion.add_reaction(Reaction(Measure.FORCE_Y > FXY_MAX, stop))
            motion.add_reaction(Reaction(Measure.FORCE_Y < -FXY_MAX, stop))
            motion.add_reaction(Reaction(Measure.TORQUE_X > TXY_MAX, stop))
            motion.add_reaction(Reaction(Measure.TORQUE_X < -TXY_MAX, stop))
            motion.add_reaction(Reaction(Measure.TORQUE_Y > TXY_MAX, stop))
            motion.add_reaction(Reaction(Measure.TORQUE_Y < -TXY_MAX, stop))

            robot.move(motion)
            total += STEP_M
            time.sleep(0.01)

        print("Finished: reached max descent.")
    except Exception as e:
        print("Aborted:", repr(e))
        robot.recover_from_errors()

if __name__ == "__main__":
    main()