# PUMA 560 — Custom Joint Position Sensors and URDF Export

## Problem
The default PUMA 560 robot model provided in the Webots object library ("PUMA 560") only contains joint actuators (`RotationalMotor` nodes). It does not include built-in position sensors on the joints. Because there are no default sensors, robot controllers cannot read the actual angles of the joints during simulation.

## Hardware Modification
To read joint angles for feedback control, the default robot template was converted into base nodes inside Webots to allow direct editing. Six `PositionSensor` nodes were manually added into the device list of each respective joint. 

Each new sensor was assigned a specific hardware string name:
* **`sens1`** (Joint 1 - Base)
* **`sens2`** (Joint 2 - Shoulder)
* **`sens3`** (Joint 3 - Elbow)
* **`sens4`** (Joint 4 - Forearm Roll)
* **`sens5`** (Joint 5 - Wrist Pitch)
* **`sens6`** (Joint 6 - Wrist Roll)

After validating that the sensors worked inside the Webots simulation console, the complete physical structure was exported directly into a Unified Robot Description Format (`.urdf`) file.

---

## Hardware Configuration Mapping

Robot controllers written in C, C++, Java, Python, or MATLAB must use these exact string identifiers to enable and read the hardware devices:

| Joint Axis | Webots Motor Name | Added Sensor Name | Axis Type | Min Limit (rad) | Max Limit (rad) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Joint 1 | `joint1` | `sens1` | Rotational | -2.7925 | 2.7925 |
| Joint 2 | `joint2` | `sens2` | Rotational | -3.9269 | 0.7854 |
| Joint 3 | `joint3` | `sens3` | Rotational | -0.7854 | 2.3561 |
| Joint 4 | `joint4` | `sens4` | Rotational | -1.9198 | 1.9198 |
| Joint 5 | `joint5` | `sens5` | Rotational | -1.7453 | 1.7453 |
| Joint 6 | `joint6` | `sens6` | Rotational | -2.5132 | 2.5132 |

---

## Directory Layout

```text
Modified_URDF/
├── README.md                 <-- This documentation file
└── puma560_exported.urdf     <-- The exported XML robot description file
```

## Current Project Usage
This directory is currently used to track the physical properties and dimensions of the modified Webots robot model. The exported URDF file serves as a reference layout for matching the joint variables used in the Python and C controllers located in the sibling folders.
