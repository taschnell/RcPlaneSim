import csv
import math
x = []
y = []
# Prop Area in m^2
A = 0.025
# Air Density in kg/m^3
p = 1.255

Vo = 0 
# Starts at zero, changes as plane accelerate
with open('Perdicted Ve, with respect to Watts.csv', 'r') as csvfile_Ve:
    csv_read = csv.reader(csvfile_Ve)
    next(csv_read)
    with open('Perdicted Thrust, with respect to Watts.csv', 'w', newline='') as csvfile_T:
        writer = csv.writer(csvfile_T)
        writer.writerow(["Thrust (N)", "Watts (w)", "Ve (m/s)"])        
        for row in csv_read:
            Ve = float(row[0]) + math.sqrt(Vo)
            W = float(row[1])
            T = .5*p*A*(Ve**2 + Vo**2)
            print(f"Thrust: {round(T,2)}N | Watts: {W}w | Ve: {round(Ve,2)}")

            writer.writerow([round(T,2), round(W,2), Ve])

            x.append(W)
            y.append(T)
        
import matplotlib.pyplot as plt

plt.plot(x, y, "-", label="Predicted Thrust")
plt.ylabel("Thrust(N)")
plt.xlabel("Watts (w)")
plt.legend()
plt.show()
