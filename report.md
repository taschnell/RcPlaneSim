**RC Plane Modeling Project**

Johann Kaufmann, Teo Schnell, Chris Chavez

# Introduction and Procedure

For our project we aimed to model the flight of an RC airplane given wattage supplied to the motor. We gathered data such as velocity, acceleration, and position from the plane GPS system. We used python functions to calculate the thrust and drag the plane creates. To do this we measured exhaust velocity (Ve) with the plane at varying wattages and speeds (Table in Data Section). As we lacked access to a wind tunnel; To simulate the plane moving while still being able to gather data we attached the RC plane to a car. This was necessary as propeller efficiency drops as airspeed (Vo) increases. See [NASA Documentation](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/propeller-thrust/).

Thrust and drag is used to find the acceleration of the plane, acceleration and time are used to find velocity, and then velocity and time are used to find position.

# Physics Calculations

All Calculations are done in Python. Relevant Curves are generated using SciPy & NumPy Library. MatPlotLib.pyplot is used to generate our graphs.

[NASA Documentation](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/propeller-thrust/)

- Thrust = 0.5_P_A\*(Ve^2 - Vo^2)
  - Air Density in kg/m^3
    - P = 1.255
  - Prop Area in m^2
    - A = 0.025
  - Velocity Exhaust = Ve Dynamically Based on Watts & Vo
    - Ve = BaseVE + Vo­<sup>(2/3)</sup>
      - BaseVE = 5.83805ln(0.14987\***WATTS**)
    - Function For BaseVE Derived with ModelAnalyzer.py
      - Note, ModelAnalyzer can only build an exponential function, so the Inverse is used in rc_simulator.py
  - Oncoming Airspeed = Vo
    - AKA: The Speed the plane is traveling at
  - NOTE That due to _Physics_ Propeller Thrust is lost as the plane goes faster, this simulator deals with that within thrust function.
- Drag = 0.5_C_pAVo<sup>2</sup>
  - Frontal Area:
    - A = 0.10m<sup>2</sup>
      - Measured Via
  - Drag Coefficient = 0.1
    - _Pretty Much an Educated Guess_
  - Air Density in km/m<sup>3</sup>:
    - p = 1.255
- F<sub>­net</sub> = Thrust - Drag
- Force/Mass = Acceleration
  - Mass = 1.0kg

# Data Utilized

| **Ve** | **Watts** | **Vo(mph)** |
| --- | --- | --- |
| 7   | 50  | 0   |
| 9.5 | 50  | 9   |
| 11.9 | 50  | 19  |
| 12.4 | 50  | 29  |
| 13.5 | 50  | 39  |
| 14.2 | 120 | 0   |
| 17.4 | 120 | 9   |
| 19  | 120 | 19  |
| 19.1 | 120 | 29  |
| 20.1 | 120 | 39  |
| 19.9 | 220 | 0   |
| 22.7 | 220 | 9   |
| 23  | 220 | 19  |
| 23.7 | 220 | 29  |
| 24  | 220 | 39  |

| Ve  | Watts |
| --- | --- |
| 0.0 | 0   |
| 15.0 | 90.65 |
| 17.5 | 114.21 |
| 20.7 | 272.33 |
| 22.2 | 291.56 |
| 25  | 506 |
| 24  | 368 |
| 13  | 64.4 |
| 9.5 | 34.65 |
| 12.5 | 55.2 |
| 7.4 | 18.56 |

# Usage of Scripts

The submitted work contains several main scripts. All scripts require user input, wattage, and distance. (The flight distance the simulation should calculate) Note that the stock simulation always starts with an airspeed of zero. Modification of the staring V value in any of the python main scripts may change this behavior. Note that the model can and has not been tested at a wattage over 850, as that is the maximum power draw of the plane in reality. To assess the accuracy of the model, further comparison was necessary. Thus, by accessing the telemetry of the RC plane as it flies, we can compare position, and velocity predictions to the actual result. Simulated date was accessed after being run by **main_csv.py**, which enters the simulation data into **Simulated.csv**. This data was compared when tied (by the appropriate time interval _.333 seconds_) to our sample data. Utilized data is contained within **position_vs_time.py**. ![A graph with numbers and lines

Otherwise, there are two other main scripts; **main.py** & **main_gui.py.** The only difference is that the GUI script provides a Graphical Use Interface to the user and generates all graphs simultaneously.

# Discussion and Interpretations of Results

We predicted that the plane would accelerate at a decreasing rate as it approached the max speed. The velocity of the plane was predicted to follow a similar graph that is increasing at a decreasing rate. Position was predicted to increase at an increasing rate util the plane reached max velocity then the plane would have a constant velocity moving forward. We first approximated the data without accounting for drag force, however we later accounted for drag force hoping to bring the predicted data a little closer to the experimental data.

Our Predictions where mostly correct each graph looked very similar to how we predicted. We found our theoretical data gets less accurate the farther along the time axis we go and our theory is a slight over estimate.

Overall, the experiment model was a success. The GPS data and the experimental data lined up very well. If we had wind tunnel and more accurate surface area of the front of the plane, we could probably get our data much more accurate.
