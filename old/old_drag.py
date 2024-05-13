import csv
# Frontal Area meters squared
A = 0.10
# Drag Coefficent estimate, to be tuned
C = 0.10
# Air Density in km/m^3
p = 1.255

x = []

y = []
"""
Formula:

D = .5*CpAv^2

"""
with open("Perdicted Drag, with respect to Velocity.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Drag (N)", "Velocity (m/s)", "Velocity (km/h)"])
    for v in range(1, 42):
        d = 0.5 * C * p * A * v * v
        print(f"At {v}m/s and {round((v*3.6),1)}km/h, drag force of {round(d,2)}N")
        writer.writerow([round(d, 2), round(v, 2), round(v*3.6, 2)])
        x.append(v)
        y.append(d)


import matplotlib.pyplot as plt

plt.plot(x, y, "-", label="Predicted Drag")
plt.ylabel("Drag(N)")
plt.xlabel("Velocity (m/s)")
plt.legend()
plt.show()
