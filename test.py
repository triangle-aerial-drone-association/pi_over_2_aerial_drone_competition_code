from codrone_edu.drone import *
drone=Drone()

drone.pair()
roll_value=-12
pitch_value=3
drone.set_trim(roll_value,pitch_value)
drone.takeoff()
drone.land()
drone.close()