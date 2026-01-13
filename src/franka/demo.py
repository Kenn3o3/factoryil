from utils.utils import activate_franka_conda_env

activate_franka_conda_env(__file__)

from franky import Robot, CartesianMotion, Affine, ReferenceType

robot = Robot("172.16.0.2")  # 改成你的 FCI IP
robot.relative_dynamics_factor = 0.05  # 建议从很小开始

motion = CartesianMotion(
    Affine([-0.1, 0.0, 0.0]),
    ReferenceType.Relative
)

print(robot.current_cartesian_state)
# Example output:
# CartesianState(pose=RobotPose(ee_pose=Affine(t=[0.489239 0.00553816 0.162337], q=[0.999872 0.0103127 -0.0120556 0.00186982]), elbow=ElbowState(joint_3_pos=0.00289798, joint_4_flip=FlipDirection.Negative)), velocity=RobotVelocity(ee_twist=Twist(lin=[0 0 0], ang=[0 0 0]), elbow_vel=0))

print(robot.current_joint_state)
# Example output:
# JointState(position=[0.00909922 0.105319 0.00289701 -2.41358 -0.00664119 2.49478 0.782101], velocity=[-0.000497612 -0.000408178 -0.000591436 0.00153467 9.843e-05 -0.000336588 -0.000919271])

robot.move(motion)
print("Done.")
