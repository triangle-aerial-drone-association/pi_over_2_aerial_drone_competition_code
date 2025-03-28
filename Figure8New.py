from codrone_edu.drone import *
import time

drone = Drone()

def fly_2_x(max_time:10, x_ini,x_dst, y_pos,z_pos,velocity,direction):
    print("------------Flying toward coordinates with incremental instruction",x_ini,x_dst,y_pos,z_pos,direction)
    time_sec = max_time
    time_start = time.perf_counter()
    x_target = x_ini

    while (time.perf_counter() - time_start) < time_sec:
        pos_data = drone.get_position_data()
        print(pos_data)
        if direction == "forward":
            # move 1/20 of the flying speed each time
            x_target = x_target + velocity*0.05
            if pos_data[1] >= x_dst:
                break
        else:
            # move 1/20 of the flying speed each time
            x_target = x_target - velocity*0.05
            if pos_data[1] <= x_dst:
                break
        drone.send_absolute_position(x_target, y_pos, z_pos,velocity, 0, 0)
        time.sleep(0.01)

    dur = time.perf_counter() - time_start
    print("*********Time spent:", dur)

def fly_2_y(max_time:10, x_pos,y_pos,z_pos,velocity,direction):
    print("------------Flying toward coordinate", x_pos, y_pos, z_pos,direction)
    time_sec = max_time
    time_start = time.perf_counter()

    while (time.perf_counter() - time_start) < time_sec:
        pos_data = drone.get_position_data()
        print(pos_data)
        if direction == "left":
            if pos_data[2] >= y_pos:
                break
        else:
            if pos_data[2] <= y_pos:
                break

        drone.send_absolute_position(x_pos, y_pos, z_pos,velocity, 0, 0)
        time.sleep(0.01)

    dur = time.perf_counter() - time_start
    print("*********Time spent:", dur)

def fly_2_z(height, power):
    HT = drone.get_pos_z()
    print('  ', HT, 'to', height)

    if HT < height:
        drone.set_throttle(power)
        while HT < height:
            drone.move(.075)
            print('up')
            print(str(HT)+"target height"+str(height))
            HT = drone.get_pos_z()
    else:
        drone.set_throttle(-1*power)
        while HT > height:
            drone.move(.075)
            print("Down")
            print(str(HT) + "target height" + str(height))
            HT = drone.get_pos_z()

    print("  Reached Target Height & hover at ",HT)

drone.pair()
drone.takeoff()

fly_2_x(10,0.5,0.5,0,1,1,"forward")
time.sleep(5)
drone.land()
drone.close()