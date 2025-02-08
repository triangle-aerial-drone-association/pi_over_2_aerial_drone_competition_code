

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

drone.takeoff()
drone.sendControlWhile(0,35,0,-25,900)
drone.sendControlWhile(0,30,0,0,800)
drone.sendControlWhile(-10,40,0,0,1200)
drone.sendControlWhile(-10,0,0,100,1000)
drone.sendControlWhile(0,0,0,40,700)
drone.sendControlWhile(0,60,0,0,800)
drone.sendControlWhile(0,0,0,-80,1400)
drone.sendControlWhile(0,-50,0,0,1000)
drone.sendControlWhile(0,0,0,0,300)
drone.sendControlWhile(0,-25,0,0,200)
time.sleep(1)
drone.sendControlWhile(0,0,0,70,700)
time.sleep(1)
drone.sendControlWhile(0,-60,0,0,800)

drone.sendControlWhile(0,0,0,-60,2000)
drone.sendControlWhile(0,60,0,0,2500)





drone.land()
drone.close()