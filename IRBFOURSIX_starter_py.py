import math
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Base Joint
ACT1 = robot.getDevice("A motor")

# Arm Joints
ACT2 = robot.getDevice("B motor")
ACT3 = robot.getDevice("C motor")
ACT4 = robot.getDevice("D motor")
ACT5 = robot.getDevice("E motor")

# End Effector
ACT6 = robot.getDevice("F motor")

# Sensors
SENS1 = robot.getDevice("A sensor")
SENS2 = robot.getDevice("B sensor")
SENS3 = robot.getDevice("C sensor")
SENS4 = robot.getDevice("D sensor")
SENS5 = robot.getDevice("E sensor")
SENS6 = robot.getDevice("F sensor")

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
    ACT3.setVelocity(0.1)  # Set safe speed threshold (rad/s)
    ACT3.setPosition(-1.0)

# Important
while robot.step(timestep) != -1:
    pass
