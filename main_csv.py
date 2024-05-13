import rc_simulator as sim
import csv

x_list, y_list, v_list, a_list = [], [], [], []

# User Inputs
watts = float(input("Simulation Wattage (w):  "))
distance = float(input("Simulation Distance (m): "))


mass = 1.0
Vo, x, time = 0, 0, 0
step = 0.01
a = sim.net_force(Vo, watts) / mass
with open("Simulated.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Time(s)","Position(m)", "Velocity(m/s)", "Acceleration(m/s²)"])
    while x < distance:
        writer.writerow([round(time,2), round(x,2), round(Vo,2), round(a,2)])
        time += step
        a = sim.net_force(Vo, watts) / mass
        Vo += a * step
        x += Vo * step
        y_list.append(x)
        x_list.append(time)
        a_list.append(a)
        v_list.append(Vo)

