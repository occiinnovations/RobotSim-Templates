#include <webots/Robot.hpp>
#include <webots/Motor.hpp>
#include <webots/PositionSensor.hpp>
#include <list>
#include <iostream>

using namespace webots;
using namespace std;

int main()
{
    Robot *robot = new Robot();

    int timeStep = 32;
    bool allPresent = true;

    Motor *ACT1 = robot->getMotor("A motor");
    Motor *ACT2 = robot->getMotor("B motor");
    Motor *ACT3 = robot->getMotor("C motor");
    Motor *ACT4 = robot->getMotor("D motor");
    Motor *ACT5 = robot->getMotor("E motor");
    Motor *ACT6 = robot->getMotor("F motor");

    PositionSensor *ps1 = robot->getPositionSensor("A sensor");
    PositionSensor *ps2 = robot->getPositionSensor("B sensor");
    PositionSensor *ps3 = robot->getPositionSensor("C sensor");
    PositionSensor *ps4 = robot->getPositionSensor("D sensor");
    PositionSensor *ps5 = robot->getPositionSensor("E sensor");
    PositionSensor *ps6 = robot->getPositionSensor("F sensor");

    std::list<Motor *> motorList = {ACT1, ACT2, ACT3, ACT4, ACT5, ACT6};
    std::list<PositionSensor *> sensorList = {ps1, ps2, ps3, ps4, ps5, ps6};

    for (Motor *m : motorList)
    {
        if (m == nullptr)
            allPresent = false;
    }

    for (PositionSensor *s : sensorList)
    {
        if (s == nullptr)
        {
            allPresent = false;
        }
        else
        {
            s->enable(timeStep);
        }
    }

    if (allPresent == true)
    {
        std::cout << "Connection Success" << std::endl;

        while (robot->step(32) != -1)
        {
            std::cout << "Hello World!" << std::endl;
            // place motor and sensor movement here
        }
    }

    delete robot;
    return 0;
}