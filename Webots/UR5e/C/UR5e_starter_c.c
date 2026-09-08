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
    WbDeviceTag act1 = wb_robot_get_device("shoulder_pan_joint");
    WbDeviceTag act2 = wb_robot_get_device("elbow_joint");
    WbDeviceTag act3 = wb_robot_get_device("shoulder_lift_joint");
    WbDeviceTag act4 = wb_robot_get_device("wrist_1_joint");
    WbDeviceTag act5 = wb_robot_get_device("wrist_2_joint");
    WbDeviceTag act6 = wb_robot_get_device("wrist_3_joint");

    // Position Sensors
    WbDeviceTag pos1 = wb_robot_get_device("shoulder_pan_joint_sensor");
    WbDeviceTag pos2 = wb_robot_get_device("elbow_joint_sensor");
    WbDeviceTag pos3 = wb_robot_get_device("shoulder_lift_joint_sensor");
    WbDeviceTag pos4 = wb_robot_get_device("wrist_1_joint_sensor");
    WbDeviceTag pos5 = wb_robot_get_device("wrist_2_joint_sensor");
    WbDeviceTag pos6 = wb_robot_get_device("wrist_3_joint_sensor");

    // Lists
    WbDeviceTag motor_list[] = {act1, act2, act3, act4, act5, act6};
    WbDeviceTag sensor_list[] = {pos1, pos2, pos3, pos4, pos5, pos6};

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

        wb_motor_set_position(act1, 3);
    };

    wb_robot_cleanup();

    return 0;
}