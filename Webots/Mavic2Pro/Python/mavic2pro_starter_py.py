import math
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Camera Mover
cam_yaw = robot.getDevice("camera yaw")

# Propellers
prop_frp = robot.getDevice("front right propeller")
prop_rrp = robot.getDevice("rear right propeller")
prop_flp = robot.getDevice("front left propeller")
prop_rlp = robot.getDevice("rear left propeller")

# Sensors
gyro = robot.getDevice("gyro")
gps = robot.getDevice("gps")
compass = robot.getDevice("compass")

# Timestep
timestep = int(robot.getBasicTimeStep())

gps.enable(timestep)
gyro.enable(timestep)
compass.enable(timestep)

# Connection Confirmation
prop_list = [prop_frp, prop_rrp, prop_flp, prop_rlp]
sens_list = [gps, gyro, compass]

if all(prop_list) and all(sens_list):
    print("Connection Success! Enjoy.")

    for prop in prop_list:
        prop.setPosition(float('inf'))
        prop.setVelocity(1.0)

    while robot.step(timestep) != -1:
        altitude = gps.getValues()[1]

        gyro_data = gyro.getValues()
        compass_data = compass.getValues()

        roll_rate = gyro_data[0]

        if altitude < 2.0:
            takeoff_speed = 67

            prop_frp.setVelocity(-takeoff_speed)
            prop_rrp.setVelocity(takeoff_speed)
            prop_flp.setVelocity(takeoff_speed)
            prop_rlp.setVelocity(-takeoff_speed)

        else:

            hover_speed = 67

            prop_frp.setVelocity(120)
            prop_rrp.setVelocity(120)
            prop_flp.setVelocity(120)
            prop_rlp.setVelocity(120)

        pass
