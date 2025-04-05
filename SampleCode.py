# this code use send_absolute_position

from codrone_edu.drone import *
import time
import matplotlib.pyplot as plt

def pre_flight_preparation(roll_trim,pitch_trim):
    print('Pre Flight Preparation...')
    drone.reset_gyro()
    drone.reset_move_values()
    drone.set_trim(roll_trim,pitch_trim)
    drone.set_initial_pressure()
    # Give 3 sec for the above action to finish
    time.sleep(3)
    battery_level = drone.get_battery()
    if battery_level < 90 :
        print('Need a freshly charged battery')
        exit(10)


def measure_dis(seconds):
    print("----------------Measuring the drone coordinate for",seconds)
    time_sec = seconds
    time_start = time.perf_counter()

    while (time.perf_counter() - time_start) < time_sec:
        pos_data = drone.get_position_data()
        save_flight_coordinance(pos_data)
        print(pos_data)

def save_flight_coordinance(pos_data):
    global t_list, x_list, y_list, z_list
    x_list.append(pos_data[1])
    y_list.append(pos_data[2])
    z_list.append(pos_data[3])
    t_list.append(pos_data[0])

# list generated for the graphing of the data
t_list = []
x_list = []
z_list = []
y_list = []


# ==== Flying Configurations =====
roll_trim =  0
pitch_trim = 0
# drone flying speed im m/sec
fly_sp = 0.4
# seconds idle between active fly controls
idle_time = 0.05
# the waypoints by the drone
waypoints = [
    {"name": "A", "x": 0, "y": 0, "z": 1.3},
    {"name": "B", "x": 1.0, "y": 0, "z": 1.3},
    {"name": "C", "x": 1.0, "y": 0, "z": 2.1},
    {"name": "D", "x": 2.0, "y": 0, "z": 2.1},
    {"name": "E", "x": 2.0, "y": 0, "z": 1.3},
    {"name": "B1", "x": 1.2, "y": 0, "z": 1.3},
    {"name": "C1", "x": 1.2, "y": 0, "z": 2.1},
    {"name": "F", "x": 0.4, "y": 0, "z": 2.1},
    {"name": "A1", "x": 0.4, "y": 0, "z": 1.3},
    {"name": "B2", "x": 1.0, "y": 0, "z": 1.3},
    {"name": "C2", "x": 1.0, "y": 0, "z": 2.1},
    {"name": "D2", "x": 2.0, "y": 0, "z": 2.1},
    {"name": "E2", "x": 2.0, "y": 0, "z": 1.3},
    {"name": "B3", "x": 1.2, "y": 0, "z": 1.3},
    {"name": "C2", "x": 1.2, "y": 0, "z": 2.1},
    {"name": "F1", "x": 0.4, "y": 0, "z": 2.1}
]

prog_start_time = time.perf_counter()

drone = Drone()
drone.pair()
pre_flight_preparation(roll_trim,pitch_trim)
# take off
drone.takeoff()

prog_time = 0

for point in waypoints:
        name, x, y, z = point["name"], point["x"], point["y"], point["z"]
        print(f"---Flying to {name}: ({x}, {y}, {z})")
        drone.send_absolute_position(x, y, z, fly_sp, 0, 0)
        measure_dis(idle_time)

prog_time = time.perf_counter() - prog_start_time
Total_Prog_Time = time.perf_counter() - prog_start_time
print("=====!!!!!!!===Total Runing Time",Total_Prog_Time)

drone.land()
drone.close()

plt.xlim(0, 90)
plt.ylim(0, 2.4)
plt.plot(t_list,z_list,'go')
plt.ylabel('Height (m)')
plt.xlabel('Time (seconds)')
plt.show()

plt.xlim(-1, 4)
plt.ylim(-2, 2)
plt.plot(x_list,y_list,'go')
plt.ylabel('Y (m)')
plt.xlabel('X (m)')
plt.show()