import matplotlib.pyplot as plt


def find_displacement_from_velocity(x_values, y_values):
    """
    Computes the distance traveled between each data point using the trapezoidal rule.

    Args:
    - x_values (list): List of x values.
    - y_values (list): List of y values corresponding to the x values.

    Returns:
    - List of distances between each data point.
    """
    distances = []
    n = len(x_values)
    for i in range(1, n):
        distance = (x_values[i] - x_values[i - 1]) * (y_values[i] + y_values[i - 1]) / 2
        distances.append(round(distance, 3))
    return distances


# Example data points
x_values = [0, 0.3333, 1, 0.666, 1.333, 1.666, 2.0, 2.333]
y_values = [70.5, 73.0, 78, 76.0, 78.0, 80.0, 81.3, 82.0]
y_converted_values = []
conversion_factor = 0.277778

for value in y_values:
    # Convert km/h to m/s
    converted_value = value * conversion_factor
    # Append the converted value to the new list
    y_converted_values.append(converted_value)

# Calculate distances between each sim. data point:
distances = find_displacement_from_velocity(x_values, y_converted_values)
print(
    f"Distances between each sim. data point:   {distances} | Total: {round(sum(distances),3)}"
)

# Example actual data points
x_actual_values = [0, 0.3333, 1, 0.666, 1.333, 1.666, 2.0, 2.333]
y_actual_values = [70.5, 72.0, 75.0, 74.0, 75.0, 77.0, 78.5, 79.0]
y__actual_converted_values = []
for value in y_actual_values:
    # Convert km/h to m/s
    converted_value = value * conversion_factor
    # Append the converted value to the new list
    y__actual_converted_values.append(converted_value)
# Calculate distances between each actual data point

actual_distances = find_displacement_from_velocity(
    x_actual_values, y__actual_converted_values
)
print(
    f"Distances between each actual data point: {actual_distances} | Total: {round(sum(actual_distances),3)}"
)

distances.insert(0, 0)
actual_distances.insert(0, 0)
_y = []
_y_actual = []
current, current_actual = (0, 0)
for i, j in zip(distances, actual_distances):
    _y.append(i + current)
    _y_actual.append(j + current_actual)
    current += i
    current_actual += j

plt.figure(figsize=(10, 6))
plt.plot(x_values, _y, marker="o", label="Simulated Data Points")
plt.plot(x_actual_values, _y_actual, marker="o", label="Actual Data Points")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Position vs. Time @ 200 Watts")
plt.legend()
plt.grid(True)

# Adding text for correlating velocities
for i in range(len(x_values)):
    plt.text(
        x_values[i],
        _y[i] + 0.5,
        f"{round(y_converted_values[i],2)} m/s",
        fontsize=8,
        ha="right",
        va="bottom",
        color="blue",
    )
    plt.text(
        x_actual_values[i],
        _y_actual[i] - 0.8,
        f"{round(y__actual_converted_values[i],2)} m/s",
        fontsize=8,
        ha="left",
        va="top",
        color="orange",
    )

plt.show()
