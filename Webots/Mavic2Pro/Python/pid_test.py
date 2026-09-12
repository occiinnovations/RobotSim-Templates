import math

dt = 0.01  # Time step for PID controller, replace with actual time step in your simulation


def pid_controller(setpoint, measured_value, Kp, Ki, Kd, integral, previous_error):
    error = setpoint - measured_value
    integral += error * dt
    derivative = (error - previous_error) / dt

    output = (Kp * error) + (Ki * integral) + (Kd * derivative)

    return output, integral, error
