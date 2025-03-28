from codrone_edu.drone import *
drone=Drone()

drone.pair()

drone.reset_sensor()
drone.reset_trim()

roll_value=-9
pitch_value=3
drone.set_trim(roll_value,pitch_value)
colors = {"Red":(255,0,0,100),"Green":(0,255,0,100),"Blue":(0,0,255,100)}
detected_color = drone.get_front_color()


multi = 5
drone.set_drone_LED(*colors[detected_color])
print(drone.get_battery())
drone.takeoff()
drone.sendControlWhile(0,30,0,0,1000*multi)
#move forward a lot under the red arch.
drone.sendControlWhile(0,0,0,50,1400*multi)
#move up over both arches.
drone.sendControlWhile(0,30,0,0,1300*multi)
#go forward above the blue arch.
drone.sendControlWhile(0,0,0,-50,1400*multi)
#go down a lot from the blue arch.
drone.sendControlWhile(0,-50,0,0,700*multi)
#go backwards in between the arches.
drone.sendControlWhile(0,0,0,60,1200*multi)
#wait a little
drone.sendControlWhile(0,0,0,80,1100*multi)
#go up above both arches to prepare go backwards to the red arch
drone.sendControlWhile(0,-60,0,0,800*multi)
#go backwards above the red arch to complete the figure 8
drone.sendControlWhile(0,0,0,-60,1500*multi)
#go down from the red arch
drone.sendControlWhile(0,40,0,20,2000*multi)
#blindly go forward in hopes of trying to get in a hole.

drone.land()
drone.close()