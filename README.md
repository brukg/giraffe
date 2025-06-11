<!-- @format -->

# _giraffe: a low-cost robotic manipulator_ 🦒

```text
                                   __             ___  ___
                            .-----|__.----.---.-.'  _.'  _.-----.
                            |  _  |  |   _|  _  |   _|   _|  -__|
                            |___  |__|__| |___._|__| |__| |_____|
                            |_____|

                               Why should fun be out of reach?
```

A [Koch v1.1](https://github.com/jess-moss/koch-v1-1) inspired even more cost-effective, ROS2-compatible, Open-Source robotic manipulator designed to lower the barriers of entry for Embodied AI and whatever else your robotic dreams may be.

To achieve these outcomes, we implemented the following significant changes:

## **Servo Selection**

We redesigned the arm around cost-efficient Waveshare servos replacing Dynamixel servos, effectively doubling the torque while reducing costs.

## **Design Enhancements**

- Adjusted the base design to transfer the radial load from the base motor to the supporting structure, reducing motor stress.
- Relocated the servo driver closer to the base for cleaner design.
- The servo mounts were redesigned to utilize the fasteners provided with the servos, minimizing the required assembly components to just the servos, 3D-printed parts, and a screwdriver.

- **[Teleop Tongs](https://github.com/carpit680/teleop_tongs) Integration**

  We integrated support for Teleop Tongs, another open-source project we built on top of [Dex Teleop](https://github.com/hello-robot/stretch_dex_teleop) (for the [Stretch 3](https://hello-robot.com/stretch-3-product) mobile manipulator by [Hello Robot](https://hello-robot.com/)), designed for teleoperating general-purpose robotic manipulators. This system features a 3D-printed tongs assembly equipped with multiple fiducial markers, serving as a stand-in for the end effector. This design enables intuitive and accessible control of the robotic arm.

  The motivation behind this integration was to offer a cost-effective, and user-friendly alternative to a leader & follower arm setup. By using Teleop Tongs, operators can manipulate the robotic arm naturally, simplifying teleoperation for applications in education, research, or DIY robotics projects.

---

## Assembly Instructions

| Giraffe Follower        | Giraffe Leader         |
|----------------------------------|---------------------------------|
| ![Giraffe Follower](assets/giraffe_follower.png) | ![Giraffe Leader](assets/giraffe_leader.png) |

### Sourcing Parts

Order the off the shelf parts for the arm using the links below.

| Item Name | Quantity Per Arm | Unit Cost (incl GST) | Buy (India) |
| --- | --- | --- | --- |
| Waveshare 30KG Serial Bus Servo | 6 | ₹1,949.99 | [Think Robotics](https://thinkrobotics.com/products/30kg-serial-bus-servo-high-precision-and-torque-with-encoder?variant=44399778169149&country=IN¤cy=INR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&utm_source=googleads&utm_medium=cpc&gad_source=1&gad_campaignid=18347254777&gclid=Cj0KCQjw0qTCBhCmARIsAAj8C4ZDflwdPUv_pBn_uVcO5QZiu6YQNuyX5HaoNUr8UGUoSLmTD4PTMfQaApOWEALw_wcB) |
| Serial Bus Servo Driver Board | 1 | ₹508.86 | [Sharvi Electronics](https://sharvielectronics.com/product/serial-bus-servo-driver-board-integrates-servo-power-supply-and-control-circuit-applicable-for-st-sc-series-serial-bus-servos-waveshare/) |
| 2 Inch metal C clamp  | 1 | ₹269.00 | [Amazon.in](https://www.amazon.in/Eastman-E-2036-C-CLAMP-INCH-2036/dp/B09F9F1KTF?th=1) |
| Type C USB Cable (1 metre) | 1 | ₹54.00 | [Robocraze](https://robocraze.com/products/type-c-usb-cable-1-metre?variant=40193636303001&country=IN¤cy=INR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&campaignid=21590308288&adgroupid=&keyword=&device=c&gad_source=1&gclid=Cj0KCQjwqIm_BhDnARIsAKBYcmuNnQNnYDXqS_BIkwa01enR4i1DLvQ--OMAT0BC9CL8HVrOcXE4uf0aAkGMEALw_wcB) |
| 1kg 2025 PLA PRO+ | 0.25 | ₹849.00 | [Amazon.in](https://www.amazon.in/dp/B06Y35GHT8?ref=ppx_yo2ov_dt_b_fed_asin_title) |
| 12V 5A 60W Power Supply with 5.5mm DC Plug | 1 | ₹403.00 | [Robu.in](https://robu.in/product/orange-ac-100-240v-to-dc-12v-5a-60w-power-adapter/) |
| M3 Nut | 4 | ₹1.00 | [Only Screws :P](https://onlyscrews.in/products/m3-nut-ss-304) |
| M3x16 Bolt | 4 | ₹2.00 | [Only Screws :P](https://onlyscrews.in/products/hex-allen-csk-m3-x-16-screw-pack-of-20) |

| Item Name | Quantity Per Arm | Unit Cost (incl GST) | Buy (India) |
| --- | --- | --- | --- |
| 2 pin JST-XH 2.54 male | 7 | ₹0.84 | [Ktron](https://www.ktron.in/my-account/view-order/127997/) |
| 2 pin JST-XH 2.54 female | 7 | ₹0.28 | [Ktron](https://www.ktron.in/my-account/view-order/127997/) |
| JST-XH 2.54 crimp Terminal | 14 | ₹0.84 | [Ktron](https://www.ktron.in/my-account/view-order/127997/) |
| Red 30 AWG wire 1m | 5 | ₹5.00 | [Robu.in](https://robu.in/product/high-quality-ultra-flexible-30awg-silicone-wire-1000-m-white/?gad_source=1&gclid=Cj0KCQjwqv2_BhC0ARIsAFb5Ac9y5QrmGJUhl2DLI0UtK0kKlJsocsbkqFMvQ10A4MQIIVxtX2W-G8MaApTbEALw_wcB) |
| Perf Board | 0.25 | ₹142.00 | [Robu.in](https://robu.in/product/12-x-18-cm-universal-pcb-prototype-board-single-sided-2-54mm-hole-pitch/) |
| ESP8266 | 1 | ₹182.00 | [Robu.in](https://robu.in/product/d1-mini-v2-nodemcu-4m-bytes-lua-wifi-internet-of-things-development-board-based-esp8266/?gad_source=1&gad_campaignid=21296336107&gclid=Cj0KCQjw0qTCBhCmARIsAAj8C4YbD580afd7JTV_2vWp4SIUCKdXW59jYu-Wk0YEZ4AWOdSpvBoFxyAaAvbREALw_wcB) |
| TCA9548A  I2C Mux | 1 | ₹81.21 | [Zbotic](https://zbotic.in/product/cjmcu-tca9548a-i2c-8-channel-multiple-extensions-development-board/?gad_source=1&gclid=Cj0KCQjw2N2_BhCAARIsAK4pEkWZaUEnn1AonuzN7zrrJuBwX3K-bko7J3kNjnqQfr_lUvTFPkCQnpgaAuj4EALw_wcB) |
| Female pin headers | 2 | ₹18.40 | [Robu.in](https://robu.in/product/2-54mm-1x40-pin-female-single-row-header-strip-pack-of-10/) |
| AS5600 Encoder | 6 | ₹130.80 | [Quartz Components](https://quartzcomponents.com/products/as5600-magnetic-angle-encoder-sensor-module?variant=44904504492266) |
| PLA PRO+ 3D printing filament | 0.25 | ₹849.00 | [Amazon.in](https://www.amazon.in/dp/B06Y35GHT8?ref=ppx_yo2ov_dt_b_fed_asin_title) |
| M3 x 6 philips head bolts | 48 | ₹3.00 | [Only Screws](https://onlyscrews.in/products/hex-allen-socket-head-m3-x-6-screw-pack-of-20?srsltid=AfmBOor482XuHLUrpOdCDrG-Go1E4GZqYg0EmdTY6sNbX8fbGjGZCeez) |
| M2.2 x 9.5 philips head self tapping screws | 2 | ₹47.20 | [Robotics DNA](https://roboticsdna.in/product/2-2mm-dia-9-5mm-ss-self-tapping-screw-25-pieces/?src=google&kwd=&adgroup={adgroup}&device=c&campaign={campaign}&adgroup={adgroup}&keyword=&matchtype=&gad_source=1&gad_campaignid=22411741198&gclid=Cj0KCQjw0qTCBhCmARIsAAj8C4YcSURfn4xIPfqC6ZU851A3e9wjm49ESc_jJkYKZkwkTw2ZjKHKA_AaAkHNEALw_wcB) |
| M3x16 Bolt | 4 | ₹2.20 | [Only Screws](https://onlyscrews.in/products/hex-allen-csk-m3-x-16-screw-pack-of-20) |
| Micro USB B cable 1 metre | 1 | ₹35.00 | [Robocraze](https://robocraze.com/products/usb-to-micro-usb-cable?variant=40192442007705&country=IN¤cy=INR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&utm_source=google&utm_medium=cpc&utm_campaign=BL+%7C+Pmax+%7C+Feed+Only+%7C+Top+40+Revenue+%7C+09%2F06&utm_source=googleads&utm_medium=ppc&utm_campaign=21373062889&utm_content=_&utm_term=&campaignid=21373062889&adgroupid=&campaign=21373062889&gad_source=1&gclid=Cj0KCQjw2N2_BhCAARIsAK4pEkVDPtNGpsZV-ffHMIzdULpzGFAPsKl39PljBhO8jgnAKcCk_V_ssa4aAiHVEALw_wcB) |
| M3 Nut | 4 | ₹1.00 | [Only Screws](https://onlyscrews.in/products/m3-nut-ss-304) |
| 2 Inch metal C clamp  | 1 | ₹269.00 | [Amazon.in](https://www.amazon.in/Eastman-E-2036-C-CLAMP-INCH-2036/dp/B09F9F1KTF?th=1) |

### Printing The Parts

A variety of 3D printers can be used to print the necessary parts for the arm. Follow these steps for optimal printing results.

#### 1. Select A Printer

When choosing a printer, keep the following recommended specifications in mind. While other printers may work, these spececifications are a good starting point:

- **Layer Height:** Minimum 0.2mm
- **Material:** PLA+, ABS, PETG, or other durable plastics
- **Nozzle Diameter:** Maximum 0.4mm
- **Infill Density:** Approximately 30%
- **Suggested Printers:** Prusa Mini+, Bambu P1, Ender3, and similar models

#### 2. Prepare The Printer

- **Materials Needed:**

  - Standard Glue Stick
  - Putty Knife

- **Setup and Printing Process:**
  1. Calibrate the printer and level the print bed following your printer’s specific instructions.
  2. Clean the print bed, removing any dust or grease. If you use water or other cleaning agents, ensure the bed is fully dry.
  3. Apply a thin, even layer of glue to the print area. Avoid uneven application or clumps.
  4. Load the printer filament according to the printer's guidelines.
  5. Adjust the printer settings to match the recommended specifications listed above.
  6. Verify the file format, select files from the hardware folder, and begin printing.

#### 3. Print The Parts

Print one of each part found in `/CAD/STL/common/` and `/CAD/STL/follower/` or `/CAD/STL/leader/` directories, depending on whether you are building the follower or leader arm. The files are organized as follows:

<div align="center">

| Common for Follower & Leader | Follower Arm Only           | Leader Arm Only             |
|:-----------------------------|:----------------------------|:----------------------------|
| base                         | follower_base_retainer_left | as5600_servo_1              |
| servo_driver_mount           | follower_base_retainer_right| as5600_servo_2              |
| shoulder_pan                 | follower_clamp_base         | leader_clamp_base           |
| soulder_pan_retainer         | follower_wrist_2            | leader_wrist_2              |
| shoulder_pan_pin             | follower_gripper_finger     | leader_handle               |
| shoulder_lift                |                             | leader_gripper_finger       |
| elbow                        |                             |                             |
| wrist_1                      |                             |                             |

</div>


#### 4. Take Down

- After the print is done, use the putty knife to scrape the the parts off the print bed.
- Remove any support material from parts.

### Assembling The Parts

Construct the arms using this Assembly [Video](https://www.youtube.com/watch?v=8nQIg9BwwTk&t=8m20s) (Note: Follow the assembly instructions provided for Follower Arm starting at 08:20 of the video). After you assemble the arms from the video, power the arm using the 12V power supply. In addition, plug the arm into your computer using a USB-C cable.

The assembled arms would look something like this:

![Image of Giraffe leader and follower arms](assets/giraffe.png)

---

## Hardware Setup Instructions

> NOTE: Configurator and the rest of the high-level software stack is presently only compatible with Python.

### Clone The [giraffe](https://github.com/carpit680/giraffe) Repository

```bash
git clone https://github.com/carpit680/giraffe.git
cd giraffe
```

### Install Dependencies

```bash
pip install -r requirements.txt
pip install .
```

### Setup Permissions

```bash
sudo usermod -a -G dialout $USER
sudo newgrp dialout
```

### Setup Servo IDs

Use the configurator script in `scripts/` directory

```bash
python3 scripts/st_configurator.py
```
## Optional ROS2 Docker Development Environment Setup

Follow the instructions given here to set up a ROS2 Docker development environment: [ros2_docker_env](https://github.com/carpit680/ros2_docker_env)

## ROS2 Worksapce Setup

1. Install ROS2 Humble following these [installation instructions](https://docs.ros.org/en/humble/Installation.html).
2. Install Gazebo Ignition Fortress(LTS) following these [instructions](https://gazebosim.org/docs/fortress/install_ubuntu/).
3. Install Moveit 2

   ```bash
   # Install MoveIt 2 for ROS 2 Humble
   sudo apt update
   sudo apt install -y ros-humble-moveit
   ```

4. Install other dependencies

   ```bash
   sudo apt install -y ros-humble-ros2-control ros-humble-ros2-controllers
   sudo apt install -y python3-colcon-common-extensions python3-rosdep
   ```

5. Set Up giraffe_ws

   ```bash
   # Clone giraffe repository if you have not done so already

   # Update dependencies using rosdep
   cd <path-to-giraffe-repo>/giraffe_ws
   sudo rosdep init  # Only if not already initialized
   rosdep update
   rosdep install --from-paths src --ignore-src -r -y
   ```

6. Build and source the workspace

   ```bash
   cd <path-to-giraffe-repo>/giraffe_ws
   colcon build --symlink-install

   source install/local_setup.zsh
   # OR
   source install/local_setup.bash
   ```

## ROS2 Workspace Description
[giraffe_moveit_sim.webm](https://github.com/user-attachments/assets/942947e6-a5ca-4b55-a39b-d64a580de182)

### giraffe_description

This package contains URDF for _giraffe_ robotic manipulator along with ros2 control xacro, ros2 controller config files, and the launch files for the entire workspace.

- _display.launch.py_: This launch file visualizes the giraffe robot model in ROS 2. It includes:

  1. Robot State Publisher: Publishes the robot's state using the URDF.
  2. Joint State Publisher GUI: Enables interactive joint control.
  3. RViz Visualization: Displays the robot in a pre-configured RViz environment.

  _Usage_:

  ```bash
  ros2 launch giraffe_description display.launch.py
  ```

- _simulation.launch.py_: This launch file sets up the simulation environment for the giraffe robot in Gazebo and RViz. It includes:

  1. Gazebo Simulation: Starts Gazebo server and client with the giraffe robot model.
  2. Robot Description and State Publisher: Publishes the robot's URDF and joint states.
  3. Controllers: Spawns and activates controllers for joint trajectory and gripper control.
  4. RViz Visualization: Displays the robot model and state in RViz.

  _Usage_:

  ```bash
  ros2 launch giraffe_description simulation.launch.py
  ```

- _moveit_sim.launch.py_: This launch file integrates the giraffe robot with Gazebo, MoveIt! 2, and RViz for advanced motion planning and control. Key features:

  1. Gazebo Integration:
      - Spawns the giraffe robot in Gazebo.
      - Configures ros2_control and joint controllers.
  2. MoveIt! 2 Motion Planning:
      - Loads MoveIt! 2 configurations (SRDF, kinematics, OMPL planning).
      - Starts the move_group node for motion planning and execution.
  3. RViz Visualization:
      - Launches RViz preconfigured for MoveIt! 2 to visualize and interact with the robot.

  _Usage_:

  ```bash
  ros2 launch giraffe_description moveit_sim.launch.py
  ```

- moveit_interface.launch.py_: This launch file configures and launches the giraffe robot hardware, MoveIt! 2, and a hardware interface for motion control. Key features:

  1. MoveIt! 2 Motion Planning:
      - Loads MoveIt! 2 configurations (SRDF, kinematics, and OMPL planning).
      - Starts the move_group node for motion planning and trajectory execution.
  2. RViz Visualization:
      - Displays the robot's state and motion planning visualization using a preconfigured RViz setup.
  3. Hardware Interface:
      - Includes a node for the giraffe robot's hardware interface for integration with controllers.

  _Usage_:

  ```bash
  ros2 launch giraffe_description moveit_interface.launch.py
  ```

### giraffe_moveit_config

The giraffe_moveit_config package provides the MoveIt! 2 configuration for the 5-DoF robotic arm named "Giraffe," designed for use with ROS 2 Humble. It includes essential files for motion planning and execution, such as:

- **URDF and SRDF**: Defines the robot's kinematic structure and semantic description.
- **Kinematics Configuration**: Specifies IK solvers for planning.
- **OMPL Planning Configuration**: Configures planning pipelines for trajectory generation.
- **Controller Configuration**: Integrates with ros2_control for real-time trajectory execution.
- **RViz Configuration**: Pre-configured visualization setup for MoveIt! 2.

This package is utilized by the **giraffe_description** package's launch file to enable simulation and motion planning for the Giraffe arm in Gazebo and MoveIt! 2 environments.

### giraffe_control
The giraffe_control package provides hardware-level control for the 5-DoF Giraffe robotic arm. It includes a ROS 2 node, giraffe_driver, and a corresponding launch file to facilitate communication between ROS 2 and the physical hardware.

#### Features

1. Giraffe Servo Driver (giraffe_driver):

   - Implements direct communication with the Giraffe arm's servos using the Feetech motor bus.
   - Processes incoming command messages to set motor positions.
   - Read motor position feedback from the servos to publish feedback.
   - Supports homing offsets, acceleration settings, and position conversion from radians to motor steps.
   - Subscribes to /command for joint commands and publishes feedback to /feedback topic.
   - Interfaces with six motors:
     - base_link_shoulder_pan_joint
     - shoulder_pan_shoulder_lift_joint
     - shoulder_lift_elbow_joint
     - elbow_wrist_1_joint
     - wrist_1_wrist_2_joint
     - wrist_2_gripper_joint

2. Launch File:
   - Starts the giraffe_driver node.
   - Configures parameters for easy integration with other ROS 2 packages.

_Usage_:

The giraffe_control package is used by the giraffe_description package's launch file to provide hardware control during simulations and real-world operation. It ensures seamless integration of the Giraffe robotic arm into ROS 2 for both motion execution and feedback.

### giraffe_hardware
The giraffe_hardware package provides a ros2_control hardware interface for the Giraffe 5-DoF robotic arm plus a gripper joint. This interface lets you control and monitor the arm through standard ROS 2 controllers and topics, simplifying integration with motion planning frameworks like MoveIt.

#### Features:

1. Giraffe Hardware Interface (GiraffeInterface):
   - Implements a hardware_interface::SystemInterface plugin.
   - Subscribes to feedback (sensor_msgs/msg/JointState) for joint position updates.
   - Publishes to command (sensor_msgs/msg/JointState) to send joint commands.
   - Handles all six joints of the arm.

_Usage_:

- Integrate with controller_manager and standard controllers (e.g., joint_trajectory_controller).
- Place giraffe_interface in your ros2_control configuration.
- Commands and feedback are exchanged via standard ROS topics, enabling easy simulation or real hardware operation.

