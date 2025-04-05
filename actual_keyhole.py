

from codrone_edu.drone import *
drone=Drone()

drone.pair()
roll_value=-12
pitch_value=3
drone.set_trim(roll_value,pitch_value)
colors = {"Red":(255,0,0,100),"Green":(0,255,0,100),"Blue":(0,0,255,100)}
detected_color = drone.get_front_color()

drone.set_drone_LED(*colors[detected_color])

drone.takeoff()

drone.sendControlWhile(-8,0,0,60,2600)
drone.sendControlWhile(0,60,0,0,2800)
drone.sendControlWhile(0,0,0,0,200)
drone.sendControlWhile(0,0,0,0,600)
drone.sendControlWhile(0,0,0,0,200)
drone.sendControlWhile(71,-19,0,0,2100)
drone.land()
drone.close()

#`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>??