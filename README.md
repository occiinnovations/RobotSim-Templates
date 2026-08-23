<img width="2022" height="1124" alt="webots-bin_9NY1MoBC8U" src="https://github.com/user-attachments/assets/ad9a33fa-2ae4-463e-8a3e-998f95e5176f" />

# RobotSim-Templates

Universal initialization templates for robot models across simulation environments. 

## Directory Structure

```text
STARTERTEMPLATES/
└── Webots/
    ├── Puma560/...
    │       └── Python/...
    │       └── Modified_URDF/...       
    ├── Mavic2Pro/ ...
    ├── Irb4600-40/ ...
    └── Ur10e/
        ├── C/
        │   └── URTENe_starter_c.c
        ├── C++/
        │   └── URTENe_starter_cpp.cpp
        ├── Java/
        │   └── URTENe_starter_java.java
        ├── MATLAB/
        │   └── URTENe_starter_MLB.m
        └── Python/
            └── URTENe_starter_py.py
```
## Template Specification

Every template in this repository runs the exact same baseline hardware setup sequence to bring a robot model to a ready state:

*   **Actuator Mapping:** Resolves device string identifiers to target motor objects for every mechanical joint.
*   **Sensor Mapping:** Resolves device string identifiers to feedback sensor objects for tracking joint states.
*   **Clock Initialization:** Establishes and synchronizes the baseline hardware simulation timestep.
*   **Execution Gate:** Builds the baseline conditional `while` loop to contain custom tracking, trajectory math, or controller logic.

## How to Use

Follow these steps to create a new controller in Webots so that you can copy and paste the code from this repository:

1. Open your world file in Webots.
2. Go to the top menu and select **Wizards** > **New Robot Controller...**
3. Click **Next** on the welcome screen.
4. Select your preferred language (Python, C++, C, Java, or MATLAB) and click **Next**.
5. Choose your default code editor and click **Next**.
6. Type a name for your new controller and click **Next**.
7. Click **Finish** to generate the new controller file.
8. Navigate to the folder of the robot you want in this repo, open the matching language file, and copy all the code.
9. Open your newly created Webots controller file, erase everything inside it, and paste my code directly into it.
10. Save the file.

## Tips To Setup

*   **Change from Generic:** In the Webots scene tree, click on your robot, locate the `controller` field, and change it from `<generic>` to the exact name of your newly created controller.
*   **Track File Locations:** Always keep track of where your project files are stored on your hard drive so you can easily reference or backup your files.
*   **Check Syntax Errors Always:** Pay close attention to your compiler or console output and always check for syntax errors before running the simulation.
*   **Rename Class and Function Names:** When using the **MATLAB** or **Java** templates, make sure to rename the main function name (MATLAB) or the public class name (Java) inside the script to match your local filename exactly.

## Roadmap

- [x] Include starter templates for all 5 Languages for included robots (Python, Java, MATLAB, C++, C)

- [ ] Expand the repository to include every significant robot.

- [ ] Add an FK/IK solver template alongside each of the starter templates.

- [ ] Add an OpenCV + NumPy connection template under each of the Python starter template folders.

- [ ] Expand the repository to include versions designed for Unity and Isaac Sim via ROS2.

## Versions

* MATLAB R2025a
* Webots R2025a
