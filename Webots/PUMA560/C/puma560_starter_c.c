#include <webots/robot.h>
#include <webots/motor.h>
#include <webots/position_sensor.h>
#include <stdio.h>
#include <stdbool.h>

#define TIME_STEP 64

int main(int argc, char **argv)
{

    wb_robot_init();

    // Actuators
    WbDeviceTag ACT1 = wb_robot_get_device("joint1");
    WbDeviceTag ACT2 = wb_robot_get_device("joint2");
    WbDeviceTag ACT3 = wb_robot_get_device("joint3");
    WbDeviceTag ACT4 = wb_robot_get_device("joint4");
    WbDeviceTag ACT5 = wb_robot_get_device("joint5");
    WbDeviceTag ACT6 = wb_robot_get_device("joint6");

    // Position Sensors
    WbDeviceTag POS1 = wb_robot_get_device("sens1");
    WbDeviceTag POS2 = wb_robot_get_device("sens2");
    WbDeviceTag POS3 = wb_robot_get_device("sens3");
    WbDeviceTag POS4 = wb_robot_get_device("sens4");
    WbDeviceTag POS5 = wb_robot_get_device("sens5");
    WbDeviceTag POS6 = wb_robot_get_device("sens6");

    // Lists
    WbDeviceTag motor_list[] = {ACT1, ACT2, ACT3, ACT4, ACT5, ACT6};
    WbDeviceTag sensor_list[] = {POS1, POS2, POS3, POS4, POS5, POS6};

    bool allPresent = true;

    // Sensor Enabling + Check
    for (int i = 0; i < 6; i++)
    {
        if (motor_list[i] == 0 || sensor_list[i] == 0)
        {
            allPresent = false;
        }
        else
        {
            wb_position_sensor_enable(sensor_list[i], TIME_STEP);
        }
    }
    if (allPresent)
    {
        printf("Connection Success\n");
    }

    while (wb_robot_step(TIME_STEP) != -1)
    {

        wb_motor_set_position(ACT1, 1);
    };

    wb_robot_cleanup();

    return 0;
}