

from codrone_edu.drone import *
drone=Drone()

drone.pair()
roll_value=-9
pitch_value=3
drone.set_trim(roll_value,pitch_value)
colors = {"Red":(255,0,0,100),"Green":(0,255,0,100),"Blue":(0,0,255,100)}
detected_color = drone.get_front_color()

drone.set_drone_LED(*colors[detected_color])


print(drone.get_front_color())

drone.sendControlWhile(0,32,0,55,1900)
drone.sendControlWhile(0,73,0,0,1000)
drone.sendControlWhile(0,0,0,0,100)
drone.sendControlWhile(0,0,0,-40,300)
drone.sendControlWhile(0,0,0,0,100)
drone.sendControlWhile(71,-21,0,0,2200)
drone.land()
drone.close()