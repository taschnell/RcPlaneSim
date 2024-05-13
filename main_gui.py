import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import rc_simulator as sim

class SimulationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dolphin Model")

        self.watt_label = ttk.Label(root, text="Wattage (w): ")
        self.watt_entry = ttk.Entry(root)
        self.watt_label.grid(row=0, column=0, padx=5, pady=5)
        self.watt_entry.grid(row=0, column=1, padx=5, pady=5)

        self.distance_label = ttk.Label(root, text="Distance (m): ")
        self.distance_entry = ttk.Entry(root)
        self.distance_label.grid(row=1, column=0, padx=5, pady=5)
        self.distance_entry.grid(row=1, column=1, padx=5, pady=5)

        self.plot_button = ttk.Button(root, text="Plot", command=self.plot_simulation)
        self.plot_button.grid(row=2, columnspan=2, padx=5, pady=5)

        self.notebook = ttk.Notebook(root)
        self.notebook.grid(row=3, columnspan=2, padx=5, pady=5)

        self.figure_pos = plt.Figure(figsize=(12, 6), dpi=100)
        self.ax_pos = self.figure_pos.add_subplot(111)
        self.ax_pos.set_xlabel("Time(s)")
        self.ax_pos.set_ylabel("Position(m)")
        self.ax_pos.grid(True)
        self.canvas_pos = FigureCanvasTkAgg(self.figure_pos, self.notebook)

        self.figure_vel = plt.Figure(figsize=(12, 6), dpi=100)
        self.ax_vel = self.figure_vel.add_subplot(111)
        self.ax_vel.set_xlabel("Time(s)")
        self.ax_vel.set_ylabel("Velocity(m/s)")
        self.ax_vel.grid(True)
        self.canvas_vel = FigureCanvasTkAgg(self.figure_vel, self.notebook)

        self.figure_acc = plt.Figure(figsize=(12, 6), dpi=100)
        self.ax_acc = self.figure_acc.add_subplot(111)
        self.ax_acc.set_xlabel("Time(s)")
        self.ax_acc.set_ylabel("Acceleration(m/s²)")
        self.ax_acc.grid(True)
        self.canvas_acc = FigureCanvasTkAgg(self.figure_acc, self.notebook)

        self.notebook.add(self.canvas_pos.get_tk_widget(), text="Position")
        self.notebook.add(self.canvas_vel.get_tk_widget(), text="Velocity")
        self.notebook.add(self.canvas_acc.get_tk_widget(), text="Acceleration")

    def plot_simulation(self):
        # User Inputs
        watts = float(self.watt_entry.get())
        distance = float(self.distance_entry.get())

        x_list, y_list, v_list, a_list = [], [], [], []

        mass = 1.0
        Vo, x, time = 0, 0, 0
        step = 0.001
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

        self.ax_pos.clear()
        label_pos = "Position at " + str(watts) + "w"
        self.ax_pos.plot(x_list, y_list, "-", label=label_pos)
        self.ax_pos.set_xlabel("Time(s)")
        self.ax_pos.set_ylabel("Position(m)")
        self.ax_pos.grid(True)
        self.ax_pos.legend()
        self.canvas_pos.draw()

        self.ax_vel.clear()
        label_vel = "Velocity at " + str(watts) + "w"
        self.ax_vel.plot(x_list, v_list, "-", label=label_vel, color="red")
        self.ax_vel.set_xlabel("Time(s)")
        self.ax_vel.set_ylabel("Velocity(m/s)")
        self.ax_vel.grid(True)
        self.ax_vel.legend()
        self.canvas_vel.draw()

        self.ax_acc.clear()
        label_acc = "Acceleration at " + str(watts) + "w"
        self.ax_acc.plot(x_list, a_list, "-", label=label_acc, color="orange")
        self.ax_acc.set_xlabel("Time(s)")
        self.ax_acc.set_ylabel("Acceleration(m/s²)")
        self.ax_acc.grid(True)
        self.ax_acc.legend()
        self.canvas_acc.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationGUI(root)
    root.mainloop()
