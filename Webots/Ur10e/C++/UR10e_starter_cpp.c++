#include <webots/Robot.hpp>
#include <webots/Motor.hpp>
#include <webots/PositionSensor.hpp>
#include <list>
#include <iostream>

using namespace webots;
using namespace std;

int main() {
  Robot *robot = new Robot();
  
  int timeStep = 32;
  bool allPresent = true;
  
  Motor *ACT1 = robot->getMotor("shoulder_pan_joint");
  Motor *ACT2 = robot->getMotor("elbow_joint");
  Motor *ACT3 = robot->getMotor("shoulder_lift_joint");
  Motor *ACT4 = robot->getMotor("wrist_1_joint");
  Motor *ACT5 = robot->getMotor("wrist_2_joint");
  Motor *ACT6 = robot->getMotor("wrist_3_joint");
  
  PositionSensor *ps1 = robot->getPositionSensor("shoulder_pan_joint_sensor");
  PositionSensor *ps2 = robot->getPositionSensor("elbow_joint_sensor");
  PositionSensor *ps3 = robot->getPositionSensor("shoulder_lift_joint_sensor");
  PositionSensor *ps4 = robot->getPositionSensor("wrist_1_joint_sensor");
  PositionSensor *ps5 = robot->getPositionSensor("wrist_2_joint_sensor");
  PositionSensor *ps6 = robot->getPositionSensor("wrist_3_joint_sensor");
  
  std::list<Motor*> motorList = {ACT1, ACT2, ACT3, ACT4, ACT5, ACT6};
  std::list<PositionSensor*> sensorList = {ps1, ps2, ps3, ps4, ps5, ps6};
  
  for (Motor* m : motorList) {
    if (m == nullptr) allPresent = false;
  }
  
  for (PositionSensor* s : sensorList) {
    if (s == nullptr) {
      allPresent = false;
    } else {
      s->enable(timeStep);
    }
  }

  
  if (allPresent == true) {
    std::cout << "Connection Success" << std::endl;
    

   while (robot->step(32) != -1) {
    std::cout << "Hello World!" << std::endl;
    
    //place motor and sensor movement here later
  }
 }

  delete robot;
  return 0;
}