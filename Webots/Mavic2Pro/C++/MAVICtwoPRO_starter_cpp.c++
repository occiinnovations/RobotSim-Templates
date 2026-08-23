#include <webots/Robot.hpp>
#include <webots/Motor.hpp>
#include <webots/Compass.hpp>
#include <webots/GPS.hpp>
#include <webots/Gyro.hpp>
#include <list>
#include <iostream>

using namespace webots;
using namespace std;

int main()
{
    Robot *robot = new Robot();

    int timeStep = 32;
    bool allPresent = true;

    Motor *prop_frp = robot->getMotor("front right propeller");
    Motor *prop_rrp = robot->getMotor("rear right propeller");
    Motor *prop_flp = robot->getMotor("front left propeller");
    Motor *prop_rlp = robot->getMotor("rear left propeller");

    Gyro *gyro = robot->getGyro("gyro");
    GPS *gps = robot->getGPS("gps");
    Compass *compass = robot->getCompass("compass");

    std::list<Motor *> prop_list = {prop_frp, prop_rrp, prop_flp, prop_rlp};
    std::list<Device *> sensor_list = {gyro, gps, compass};

    for (Motor *m : prop_list)
    {
        if (m == nullptr)
            allPresent = false;
    }

    for (Device *s : sensor_list)
    {
        if (s == nullptr)
        {
            allPresent = false;
        }

        if (allPresent == true)
        {
            std::cout << "Connection Success" << std::endl;

            while (robot->step(timeStep) != -1)
            {
                std::cout << "Hello World!" << std::endl;
                // place motor and sensor movement here
            }
        }

        delete robot;
        return 0;
    }
}