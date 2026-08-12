function IRBFOURSIX_starter_MLB

%desktop;
%keyboard;

TIME_STEP = 64;


%Motors
ACT1 = wb_robot_get_device('A motor');

ACT2 = wb_robot_get_device('B motor');
ACT3 = wb_robot_get_device('C motor');
ACT4 = wb_robot_get_device('D motor');
ACT5 = wb_robot_get_device('E motor');

ACT6 = wb_robot_get_device('F motor');

%Sensors
SENS1 = wb_robot_get_device('A sensor');
SENS2 = wb_robot_get_device('B sensor');
SENS3 = wb_robot_get_device('C sensor');
SENS4 = wb_robot_get_device('D sensor');
SENS5 = wb_robot_get_device('E sensor');
SENS6 = wb_robot_get_device('F sensor');

%Lists for Usage
motor_list = [ACT1, ACT2, ACT3, ACT4, ACT5, ACT6];
sensor_list = [SENS1, SENS2, SENS3, SENS4, SENS5, SENS6];

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
  wb_motor_set_position(ACT1, 1.5);
  wb_motor_set_velocity(ACT1, 0.4);
  
  drawnow;
end

end % End of code

% cleanup code here