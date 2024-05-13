# RcPlaneSim

A simple physics model for at RC Plane.

## Hardware Info

- **FRAME:** ATOMRC Dolphin
- **MOTOR:** 2804, 1800kv Motor
- **Control Surfaces:** 9G Analog Servos
- **PROP:** 7in Prop, 2in Pitch

## Usage

To use simply run either main.py or main_gui.py.
Input Sim Distance and Wattage and Caculate!
Be aware the plane is not intended to draw more than ~1250 Watts (25V @ 50AMPS)
Thus the simulator accuracy has not been tested after that power draw.

## Physic Calculations

[NASA Documentation](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/propeller-thrust/)

- Thrust = 0.5*P*A*(Ve^2 - Vo^2)
    Air Density in kg/m^3
    P = 1.255

    Prop Area in m^2
    A = 0.025

    Velocity Exaust = Ve
    Dynamically Based on Watts & Vo --> See Thrust Function within rc_simulator.py

    Oncoming Airspeed = Vo
    AKA: The Speed the plane is traveling at

    NOTE That due to *Physics* Propeller Thrust is lost as the plane goes faster, this simulator deals with that within thrust function

- Drag = 0.5*C*p*A*Vo^2
    Frontal Area meters squared
    A = 0.10
    air density in km/m^3
    p = 1.255

- Net Force = Thrust - Drag

- Force/Mass = Acceleration
    Force = Net Force
    Mass = 1.0kg

## Other Notes

- ModelAnalyzer.py to Caculate Relationship Curves
- old_drag.py and old_thrust.py can also fufill this function
