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
    WbDeviceTag ACT1 = wb_robot_get_device("A motor");
    WbDeviceTag ACT2 = wb_robot_get_device("B motor");
    WbDeviceTag ACT3 = wb_robot_get_device("C motor");
    WbDeviceTag ACT4 = wb_robot_get_device("D motor");
    WbDeviceTag ACT5 = wb_robot_get_device("E motor");
    WbDeviceTag ACT6 = wb_robot_get_device("F motor");

    // Position Sensors
    WbDeviceTag POS1 = wb_robot_get_device("A sensor");
    WbDeviceTag POS2 = wb_robot_get_device("B sensor");
    WbDeviceTag POS3 = wb_robot_get_device("C sensor");
    WbDeviceTag POS4 = wb_robot_get_device("D sensor");
    WbDeviceTag POS5 = wb_robot_get_device("E sensor");
    WbDeviceTag POS6 = wb_robot_get_device("F sensor");

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

        wb_motor_set_position(ACT1, 3);
    };

    wb_robot_cleanup();

    return 0;
}