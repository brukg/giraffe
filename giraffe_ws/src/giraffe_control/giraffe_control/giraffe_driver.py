#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from giraffe_control.feetech import FeetechMotorsBus
import numpy as np

class GiraffeDriver(Node):

    def __init__(self):
        super().__init__("giraffe_driver")

        self.motors_bus = FeetechMotorsBus(
            port="/dev/ttyACM0",
            motors={
                "shoulder_pan_actuator_shoulder_pan_joint": (1, "sts3215"),
                "shoulder_lift_actuator_shoulder_lift_joint": (2, "sts3215"),
                "elbow_actuator_elbow_joint": (3, "sts3215"),
                "wrist_1_actuator_wrist_1_joint": (4, "sts3215"),
                "wrist_2_actuator_wrist_2_joint": (5, "sts3215"),
                "finger_actuator_gripper_joint": (6, "sts3215"),
            },
        )
        self.motor_order = [
            "shoulder_pan_actuator_shoulder_pan_joint",
            "shoulder_lift_actuator_shoulder_lift_joint",
            "elbow_actuator_elbow_joint",
            "wrist_1_actuator_wrist_1_joint",
            "wrist_2_actuator_wrist_2_joint",
            "finger_actuator_gripper_joint",
        ]
        self.motors_bus.connect()

        self.joint_reverse = {}
        for motor_name in self.motor_order:
            param_name = f'joint_reverse.{motor_name}'
            self.declare_parameter(param_name, False)
            param_value = self.get_parameter(param_name).get_parameter_value().bool_value
            self.joint_reverse[motor_name] = param_value

        self.get_logger().info(f'Loaded joint_reverse: {self.joint_reverse}')

        self.joint_state_pub = self.create_publisher(JointState, "/feedback", 10)
        self.joint_command_sub = self.create_subscription(
            JointState, "/command", self.joint_state_callback, 10
        )

        self.timer = self.create_timer(0.01, self.publish_joint_states)

        self.offsets = [3.223, 4.6138, 1.4083, 3.152, 1.5708, 4.9532]
        self.set_motor_acceleration(5, 50)

    def joint_state_callback(self, msg: JointState):
        positions = []

        for motor_name, offset in zip(self.motor_order, self.offsets):
            if motor_name in msg.name:
                idx = msg.name.index(motor_name)
                radians = msg.position[idx]
                if self.joint_reverse[motor_name]:
                    radians = -radians
                model = self.motors_bus.motors[motor_name][1]
                step_value = self.radians_to_steps(-radians, model) + self.radians_to_steps(offset, model)
                positions.append(step_value)
            else:
                positions.append(0)

        self.motors_bus.write("Goal_Position", np.array(positions), self.motor_order)

    def publish_joint_states(self):
        joint_state = JointState()
        joint_state.header.stamp = self.get_clock().now().to_msg()
        joint_state.name = self.motor_order
        positions = self.motors_bus.read("Present_Position", self.motor_order)
        position_radians = self.motors_bus.steps_to_radians(positions, self.motors_bus.motors[self.motor_order[0]][1])

        for motor_name, position, offset in zip(self.motor_order, position_radians, self.offsets):
            radians = -position + offset
            if self.joint_reverse[motor_name]:
                radians = -radians
            joint_state.position.append(radians)

        self.joint_state_pub.publish(joint_state)

    def set_motor_acceleration(self, acceleration: int, gripper_acceleration: int):
        try:
            motor_names = self.motors_bus.motor_names
            non_gripper_motors = motor_names[:-1]
            accelerations = [acceleration] * len(non_gripper_motors)
            self.motors_bus.write("Acceleration", accelerations, non_gripper_motors)
            gripper = motor_names[-1]
            self.motors_bus.write("Acceleration", gripper_acceleration, gripper)
        except Exception as e:
            self.get_logger().warn(f"Failed to set acceleration: {e}")

    def radians_to_steps(self, radians: float, model: str) -> int:
        resolution = 4096
        degrees = np.degrees(radians)
        steps = int(degrees / 360.0 * resolution)
        return steps


def main(args=None):
    rclpy.init(args=args)
    giraffe_driver = GiraffeDriver()

    try:
        rclpy.spin(giraffe_driver)
    except KeyboardInterrupt:
        pass

    giraffe_driver.destroy_node()
    giraffe_driver.motors_bus.disconnect()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
