<img width="2022" height="1124" alt="webots-bin_9NY1MoBC8U" src="https://github.com/user-attachments/assets/ad9a33fa-2ae4-463e-8a3e-998f95e5176f" />

# RobotSim-Templates

Universal initialization templates for robot models across simulation environments.

## Directory Structure

```text
RobotSim-Templates/
└── Webots/
    ├── Irb4600-40/
    │   ├── C++/
    │   └── Python/
    └── Ur10e/
        ├── C/
        ├── C++/
        ├── Java/
        ├── MATLAB/
        └── Python/
```

## Template Specification

Every template in this repository runs the exact same baseline hardware setup sequence to bring a robot model to a ready state:

*   **Actuator Mapping:** Resolves device string identifiers to target motor objects for every mechanical joint.
*   **Sensor Mapping:** Resolves device string identifiers to feedback sensor objects for tracking joint states.
*   **Clock Initialization:** Establishes and synchronizes the baseline hardware simulation timestep.
*   **Execution Gate:** Builds the baseline conditional `while` loop to contain custom tracking, trajectory math, or controller logic.

## How to Use

1. **Open Webots:** Launch your robot simulation world file inside Webots.
2. **Create a Controller:** Go to the top menu and select `Wizards` > `New Robot Controller...`.
3. **Choose Your Language:** Follow the onscreen prompts to select your preferred programming language (C, C++, Java, MATLAB, or Python).
4. **Copy and Paste:** Open the template file from this repository that matches your chosen language, copy the entire code block, and paste it directly into your new Webots controller file.
5. **Adjust File Names:** If you chose **Java** or **MATLAB**, ensure you update the class or function names inside the code to exactly match the file name you assigned during the wizard setup.

## Model Specific Notes

### ABB IRB 4600-40
When spawning the native `IRB4600` PROTO node into your Webots scene tree, the physics engine will calculate an unanchored center of mass, causing the column base to tilt upon simulation initialization. To fix this:
1. Select the **`ABB_IRB_4600`** robot node in the Scene Tree.
2. Locate the **`staticBase`** field property in the sidebar.
3. Toggle the boolean value to **`TRUE`** to rigid-anchor the manipulator foundation to the world floor grid.

## Roadmap

*   [x] Establish baseline 5-language templates for the UR10e arm.
*   [x] Expand architecture initialization layers to the ABB IRB 4600-40 industrial manipulator.
*   [ ] Expand templates to cover the remaining utility and industrial robots native to Webots (e.g., DJI Mavic 2 Pro).
*   [ ] Port these standardized boilerplate templates over to **Gazebo** and **NVIDIA Isaac Sim**.

## Versions

* MATLAB R2025a
* Webots R2025a

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file at the root of this workspace for the full, non-permissive copyright and liability disclosure text.
