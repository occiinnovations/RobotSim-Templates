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
sens1 = robot.getDevice("shoulder_pan_joint_sensor")
sens2 = robot.getDevice("elbow_joint_sensor")
sens3 = robot.getDevice("shoulder_lift_joint_sensor")
sens4 = robot.getDevice("wrist_1_joint_sensor")
sens5 = robot.getDevice("wrist_2_joint_sensor")
sens6 = robot.getDevice("wrist_3_joint_sensor")

# Timestep
timestep = int(robot.getBasicTimeStep())
sens1.enable(timestep)
sens2.enable(timestep)
sens3.enable(timestep)
sens4.enable(timestep)
sens5.enable(timestep)
sens6.enable(timestep)

# Connection Confirmation
actList = [act1, act2, act3, act4, act5, act6]
sensorList = [sens1, sens2, sens3, sens4, sens5, sens6]

for act in actList:
    act.setVelocity(0.1)

if all(actList) and all(sensorList):
    print("Connection Success! Enjoy.")


# Important
while robot.step(timestep) != -1:
    ACT3.setPosition(-1.0)
    ACT2.setPosition(-1.0)

    pass
