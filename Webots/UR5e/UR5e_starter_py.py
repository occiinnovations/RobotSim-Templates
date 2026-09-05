import math
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Base Joint
ACT1 = robot.getDevice("shoulder_pan_joint")

# Arm Joints
ACT2 = robot.getDevice("elbow_joint")
ACT3 = robot.getDevice("shoulder_lift_joint")
ACT4 = robot.getDevice("wrist_1_joint")
ACT5 = robot.getDevice("wrist_2_joint")

# End Effector
ACT6 = robot.getDevice("wrist_3_joint")

# Sensors
SENS1 = robot.getDevice("shoulder_pan_joint_sensor")
SENS2 = robot.getDevice("elbow_joint_sensor")
SENS3 = robot.getDevice("shoulder_lift_joint_sensor")
SENS4 = robot.getDevice("wrist_1_joint_sensor")
SENS5 = robot.getDevice("wrist_2_joint_sensor")
SENS6 = robot.getDevice("wrist_3_joint_sensor")

# Timestep
timestep = int(robot.getBasicTimeStep())
SENS1.enable(timestep)
SENS2.enable(timestep)
SENS3.enable(timestep)
SENS4.enable(timestep)
SENS5.enable(timestep)
SENS6.enable(timestep)

# Connection Confirmation
ACTlist = [ACT1, ACT2, ACT3, ACT4, ACT5, ACT6]
SENSlist = [SENS1, SENS2, SENS3, SENS4, SENS5, SENS6]

for ACT in ACTlist:
    ACT.setVelocity(0.1)

if all(ACTlist) and all(SENSlist):
    print("Connection Success! Enjoy.")


# Important
while robot.step(timestep) != -1:
    ACT3.setPosition(-1.0)
    ACT2.setPosition(-1.0)

    pass
