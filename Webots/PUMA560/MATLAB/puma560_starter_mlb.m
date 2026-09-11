function puma560_starter_mlb()

%desktop;
%keyboard;

TIME_STEP = 64;


%Motors
act1 = wb_robot_get_device('joint1');

act2 = wb_robot_get_device('joint2');
act3 = wb_robot_get_device('joint3');
act4 = wb_robot_get_device('joint4');
act5 = wb_robot_get_device('joint5');

act6 = wb_robot_get_device('joint6');

%Sensors
sens1 = wb_robot_get_device('sensor1');
sens2 = wb_robot_get_device('sensor2');
sens3 = wb_robot_get_device('sensor3');
sens4 = wb_robot_get_device('sensor4');
sens5 = wb_robot_get_device('sensor5');
sens6 = wb_robot_get_device('sensor6');

%Lists for Usage
motor_list = [act1, act2, act3, act4, act5, act6];
sensor_list = [sens1, sens2, sens3, sens4, sens5, sens6];

for i = 1:length(sensor_list)
  wb_position_sensor_enable(sensor_list(i), TIME_STEP);
end

%Error or Success Message
if all(motor_list > 0) && all(sensor_list > 0) 
  disp('All devices connected');
else
  disp('Connection Failed');
end

% Main Stuff
while wb_robot_step(TIME_STEP) ~= -1
  
  % place all motor/sensor/camera code here:
  wb_motor_set_position(act1, 1.5);
  wb_motor_set_velocity(act1, 0.4);
  
  drawnow;
end

end % End of code

% cleanup code here