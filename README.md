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
            └── URTENe_starter_py.py
```

## Template Specification

Every template in this repository runs the exact same baseline hardware setup sequence to bring a robot model to a ready state:

*   **Actuator Mapping:** Resolves device string identifiers to target motor objects for every mechanical joint.
*   **Sensor Mapping:** Resolves device string identifiers to feedback sensor objects for tracking joint states.
*   **Clock Initialization:** Establishes and synchronizes the baseline hardware simulation timestep.
*   **Execution Gate:** Builds the baseline conditional `while` loop to contain custom tracking, trajectory math, or controller logic.
