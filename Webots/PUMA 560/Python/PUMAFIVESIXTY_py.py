import math
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Base Joint
ACT1 = robot.getDevice("joint1")

# Arm Joints
ACT2 = robot.getDevice("joint2")
ACT3 = robot.getDevice("joint3")
ACT4 = robot.getDevice("joint4")
ACT5 = robot.getDevice("joint5")

# End Effector
ACT6 = robot.getDevice("joint6")

# Sensors
SENS1 = robot.getDevice("sens1")
SENS2 = robot.getDevice("sens2")
SENS3 = robot.getDevice("sens3")
SENS4 = robot.getDevice("sens4")
SENS5 = robot.getDevice("sens5")
SENS6 = robot.getDevice("sens6")

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

if all(ACTlist) and all(SENSlist):
    print("Connection Success! Enjoy.")

    # Place Code Here:
    ACT1.setVelocity(0.1)
    ACT1.setPosition(0.5)

# Important
while robot.step(timestep) != -1:
    pass
