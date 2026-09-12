import math
from controller import Robot

robot = Robot()
timestep = float(robot.getBasicTimeStep())


def pid_controller(setpoint, measured_value, Kp, Ki, Kd, integral, previous_error):
    error = setpoint - measured_value
    integral += error * timestep
    derivative = (error - previous_error) / timestep

    output = (Kp * error) + (Ki * integral) + (Kd * derivative)

    return output, integral, error


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

timestep = float(robot.getBasicTimeStep())
gps.enable(timestep)
gyro.enable(timestep)
compass.enable(timestep)

# Connection Confirmation
prop_list = [prop_frp, prop_rrp, prop_flp, prop_rlp]
sens_list = [gps, gyro, compass]


# Reading Sensors
def read_sensors():
    my_altitude = gps.getValues()[1]
    my_gyro_data = gyro.getValues()
    my_compass_data = compass.getValues()

    return my_altitude, my_gyro_data, my_compass_data


def speed_of_propellers(prop_flp, prop_frp, prop_rlp, prop_rrp, thrust):

    hover_speed = 67.5

    prop_flp.setVelocity((hover_speed + thrust))
    prop_frp.setVelocity(-(hover_speed + thrust))
    prop_rlp.setVelocity(-(hover_speed + thrust))
    prop_rrp.setVelocity((hover_speed + thrust))


if all(prop_list) and all(sens_list):
    print("Connection Success! Enjoy.")

    for prop in prop_list:
        prop.setPosition(float('inf'))
        prop.setVelocity(0.0)

    current_integral = 0.0
    previous_error = 0.0
    target_altitude = 2.0

    while robot.step(timestep) != -1:
        altitude, gyro_data, compass_data = read_sensors()

        roll_rate = gyro_data[0]

        thrust, current_integral, previous_error = pid_controller(
            target_altitude, altitude,
            Kp=1.0, Ki=0.1, Kd=0.05,
            integral=current_integral, previous_error=previous_error
        )

        speed_of_propellers(prop_flp, prop_frp, prop_rlp, prop_rrp, thrust)

        pass
