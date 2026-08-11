<img width="2022" height="1124" alt="webots-bin_9NY1MoBC8U" src="https://github.com/user-attachments/assets/ad9a33fa-2ae4-463e-8a3e-998f95e5176f" />

# RobotSim-Templates

Universal initialization templates for robot models across simulation environments. 

## Directory Structure

```text
StarterTemplates/
└── Webots/
    └── Ur10e/
        ├── C++/
        │   └── URTENe_starter_cpp.c++
        └── Python/
        │     └── URTENe_starter_py.py
        └── MATLAB/
              └──URTENe_starter_MLB.m
```

## Template Specification

Every template in this repository runs the exact same baseline hardware setup sequence to bring a robot model to a ready state:

*   **Actuator Mapping:** Resolves device string identifiers to target motor objects for every mechanical joint.
*   **Sensor Mapping:** Resolves device string identifiers to feedback sensor objects for tracking joint states.
*   **Clock Initialization:** Establishes and synchronizes the baseline hardware simulation timestep.
*   **Execution Gate:** Builds the baseline conditional `while` loop to contain custom tracking, trajectory math, or controller logic.

## Versions

* MATLAB R2025a
* Webots R2025a
