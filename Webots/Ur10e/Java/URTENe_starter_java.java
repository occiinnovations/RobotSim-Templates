package Webots.Ur10e.Java;

import com.cyberbotics.webots.Robot;
import com.cyberbotics.webots.Motor;
import com.cyberbotics.webots.PositionSensor;
import java.util.Arrays;
import java.util.List;

public class URTENe_starter_java {
    public static void main(String args[]) {
        Robot robot = new Robot();

        int timeStep = (int) Math.round(robot.getBasicTimeStep());
        boolean allPresent = true;

        // Actuators
        Motor act1 = robot.getMotor("shoulder_pan_joint");
        Motor act2 = robot.getMotor("elbow_joint");
        Motor act3 = robot.getMotor("shoulder_lift_joint");
        Motor act4 = robot.getMotor("wrist_1_joint");
        Motor act5 = robot.getMotor("wrist_2_joint");
        Motor act6 = robot.getMotor("wrist_3_joint");

        // Sensors
        PositionSensor ps1 = robot.getPositionSensor("shoulder_pan_joint_sensor");
        PositionSensor ps2 = robot.getPositionSensor("elbow_joint_sensor");
        PositionSensor ps3 = robot.getPositionSensor("shoulder_lift_joint_sensor");
        PositionSensor ps4 = robot.getPositionSensor("wrist_1_joint_sensor");
        PositionSensor ps5 = robot.getPositionSensor("wrist_2_joint_sensor");
        PositionSensor ps6 = robot.getPositionSensor("wrist_3_joint_sensor");

        // Lists
        List<Motor> motorList = Arrays.asList(act1, act2, act3, act4, act5, act6);
        List<PositionSensor> sensorList = Arrays.asList(ps1, ps2, ps3, ps4, ps5, ps6);

        // Sensor Enabling + Check
        for (Motor m : motorList) {
            if (m == null) {
                allPresent = false;
            }
        }

        for (PositionSensor s : sensorList) {
            if (s == null) {
                allPresent = false;
            } else {
                s.enable(timeStep);
            }
        }

        if (allPresent) {
            System.out.println("Connection success");

            while (robot.step(timeStep) != -1) {
                System.out.println("Hello World!");

                // Functions go here
            }
        } else {
            System.err.println("Error");

        }

    }

}
