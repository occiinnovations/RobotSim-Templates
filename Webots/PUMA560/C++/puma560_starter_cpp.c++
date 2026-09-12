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

    Motor *act1 = robot->getMotor("joint1");
    Motor *act2 = robot->getMotor("joint2");
    Motor *act3 = robot->getMotor("joint3");
    Motor *act4 = robot->getMotor("joint4");
    Motor *act5 = robot->getMotor("joint5");
    Motor *act6 = robot->getMotor("joint6");

    PositionSensor *ps1 = robot->getPositionSensor("sens1");
    PositionSensor *ps2 = robot->getPositionSensor("sens2");
    PositionSensor *ps3 = robot->getPositionSensor("sens3");
    PositionSensor *ps4 = robot->getPositionSensor("sens4");
    PositionSensor *ps5 = robot->getPositionSensor("sens5");
    PositionSensor *ps6 = robot->getPositionSensor("sens6");

    std::list<Motor *> motorList = {act1, act2, act3, act4, act5, act6};
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

            // place motor and sensor movement here later
        }
    }

    delete robot;
    return 0;
}