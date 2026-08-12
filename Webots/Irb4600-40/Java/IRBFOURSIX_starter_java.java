package Webots.Irb4600.Java;

import com.cyberbotics.webots.Robot;
import com.cyberbotics.webots.Motor;
import com.cyberbotics.webots.PositionSensor;
import java.util.Arrays;
import java.util.List;

public class IRBFOURSIX_starter_java {
    public static void main(String args[]) {
        Robot robot = new Robot();

        int timeStep = (int) Math.round(robot.getBasicTimeStep());
        boolean allPresent = true;

        // Actuators
        Motor act1 = robot.getMotor("A motor");
        Motor act2 = robot.getMotor("B motor");
        Motor act3 = robot.getMotor("C motor");
        Motor act4 = robot.getMotor("D motor");
        Motor act5 = robot.getMotor("E motor");
        Motor act6 = robot.getMotor("F motor");

        // Sensors
        PositionSensor ps1 = robot.getPositionSensor("A sensor");
        PositionSensor ps2 = robot.getPositionSensor("B sensor");
        PositionSensor ps3 = robot.getPositionSensor("C sensor");
        PositionSensor ps4 = robot.getPositionSensor("D sensor");
        PositionSensor ps5 = robot.getPositionSensor("E sensor");
        PositionSensor ps6 = robot.getPositionSensor("F sensor");

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