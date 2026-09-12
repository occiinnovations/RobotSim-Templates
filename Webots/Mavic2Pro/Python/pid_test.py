import math

# whatever your timestep is just replace it with that value
timestep = float(input("Enter timestep value: "))
t = timestep

Kp = float(input("Enter Kp value: "))
Ki = float(input("Enter Ki value: "))
Kd = float(input("Enter Kd value: "))

integral_total = 0.0
last_error = 0.0

target = 2.0

# if need be, change robot name to yours, however this shouldn't be necessary for most cases
while robot.step(timestep) != -1:

    # replace 'sensor' with your actual sensor device
    current_value = sensor.getValue()

    error = target - current_value

    integral_total += error * timestep
    derivative = (error - last_error) / timestep

    main_pid = (Kp * error) + (Ki * integral_total) + (Kd * derivative)

    last_error = error

    # replace 'motor' with your actual motor device
    motor.setVelocity(main_pid)

    pass
