import rc_simulator as sim
import matplotlib.pyplot as plt

x_list, y_list, v_list, a_list = [], [], [], []

# User Inputs
watts = float(input("Simulation Wattage (w):  "))
distance = float(input("Simulation Distance (m): "))


mass = 1.0
Vo, x, time = 0, 0, 0
step = 0.01
a = sim.net_force(Vo, watts) / mass
while x < distance:
    time += step
    a = sim.net_force(Vo, watts) / mass
    Vo += a * step
    x += Vo * step
    y_list.append(x)
    x_list.append(time)
    a_list.append(a)
    v_list.append(Vo)

label = "Position at stable " + str(watts) + "w"
plt.plot(x_list, y_list, "-", label=label)
plt.xlabel("Time(s)")
plt.ylabel("Position(m)")
plt.grid(True)
plt.legend()
plt.show()

label = "Velocity at stable " + str(watts) + "w"
plt.plot(x_list, v_list, "-", label=label, color="red")
plt.xlabel("Time(s)")
plt.ylabel("Velocity(m/s)")
plt.grid(True)
plt.legend()
plt.show()

label = "Acceleration at stable " + str(watts) + "w"
plt.plot(x_list, a_list, "-", label=label, color="orange")
plt.xlabel("Time(s)")
plt.ylabel("Acceleration(m/s²)")
plt.grid(True)
plt.legend()
plt.show()
