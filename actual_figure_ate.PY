

from codrone_edu.drone import *
drone=Drone()

drone.pair()
roll_value=-9
pitch_value=3
drone.set_trim(roll_value,pitch_value)
colors = {"Red":(255,0,0,100),"Green":(0,255,0,100),"Blue":(0,0,255,100)}
detected_color = drone.get_front_color()

drone.set_drone_LED(*colors[detected_color])

drone.takeoff()
drone.sendControlWhile(0,35,0,-25,900)
#move forward and a little down
drone.sendControlWhile(0,30,0,0,1000)
#move forward a lot under the red arch.
drone.sendControlWhile(-10,40,0,0,1200)
#move forward a lot and go to the left because of drift. keep going under red arch.
drone.sendControlWhile(-10,0,0,100,1200)
#go up and go to the left because of drift. Go above the blue arch
drone.sendControlWhile(0,0,0,40,700)
#go up again but no -10 roll
drone.sendControlWhile(0,30,0,0,1300)
#go forward above the blue arch.
drone.sendControlWhile(0,0,0,-80,1500)
#go down a lot from the blue arch.
drone.sendControlWhile(0,-50,0,0,500)
#go backwards in between the arches.
drone.sendControlWhile(0,0,0,0,300)
time.sleep(1)
drone.sendControlWhile(0,0,0,80,1100)
#go up above both arches to prepare go backwards to the red arch
time.sleep(1)
drone.sendControlWhile(0,-60,0,0,800)
#go backwards above the red arch to complete the figure 8
drone.sendControlWhile(0,0,0,-60,2000)
#go down from the red arch
drone.sendControlWhile(0,40,0,0,2500)
#blindly go forward in hopes of trying to get in a hole.

drone.land()
drone.close()