from codrone_edu.drone import *

drone = Drone()
drone.pair()
color = drone.get_back_color()
if color == 'Green':
    drone.set_drone_LED(0,255,0,100)
elif color == 'Yellow':
    drone.set_drone_LED(255,205,0,100)
elif color == 'Blue':
    drone.set_drone_LED(0,0,255,100)
elif color == 'Red':
    drone.set_drone_LED(255, 0, 0, 100)
drone.takeoff()

x = drone.get_pos_x(unit="in")
drone.sendControlWhile(0,30,0,0,800)
while x < 45:
    drone.sendControlWhile(0,40,0,60,50)
    x = drone.get_pos_x(unit="in")
drone.sendControlWhile(0,30,0,0,1000)
drone.sendControlWhile(0,0,0,-40,2000)
z = drone.get_pos_z(unit="in")
#while z > 40:
  #  drone.sendControlWhile(0,0,0,-30,50)
while x > 20:
    drone.sendControlWhile(0,-40,0,65,50)
    x = drone.get_pos_x(unit="in")
#while z > 40:
drone.sendControlWhile(0,0,0,-30,3500)
drone.sendControlWhile(0,45,0,0,2000)

drone.land()
drone.close()