import math
import numpy as np


def thrust(Vo=0.0, Watts=200.0) -> float:
    """
    Caculates Ve based on current Vo and Watts input, in order to return Thrust.
    Formula: Thrust = .5*p*A*(Ve**2 - Vo**2)

    NOTE: Function is tunned specifically for a 7in prop on a 2804-1800kv motor.
    2in Pitch.
    NOTE: All caculations SI Metric units. 
    
    Returns Float in Newtons
    """

    # Function, as BaseVe relates to Watts:
    # 6.672168251812739*e^(x*0.17129478900624442)

    # Inverse Function USED
    a_base_Ve = 5.83805
    b_base_Ve = 0.14987
    # a_base_Ve = 9.26440
    # b_base_Ve = 0.02361
    BaseVe = a_base_Ve * (np.log(b_base_Ve * Watts))

    # Air Density in kg/m^3
    p = 1.255

    # Prop Area in m^2
    A = 0.025

    # Ve Caculation --> Ve = BaseVe + (Vo)^(2/3)
    Ve = BaseVe + (Vo)**(2.0/3.0)

    # Thrust Caculation:
    Thrust = 0.5 * p * A * (Ve**2 - Vo**2)

    return round(Thrust, 3)


def drag(Vo=0.0, C=0.10) -> float:
    """
    Caculates Drag Based upon Oncoming airspeed, (Vo):
    Formula: D = .5*CpAv^2

    NOTE: Function is tunned specifically for an ATOMRC Dolphin Fixed Wing Model
    NOTE: Drag Coefficient (C) is an estimate, Tune as Nessecary

    Returns Float in Newtons
    """
    # Frontal Area meters squared
    A = 0.10
    # air density in km/m^3
    p = 1.255
    Drag = 0.5 * C * p * A * Vo**2

    return round(Drag, 3)

def net_force(Vo, Watts):
    T = thrust(Vo, Watts)
    D = drag(Vo)
    return round(T-D,3)

if __name__ == "__main__":
    watts = float(input("Please Input Number of Watts: "))
    for Vo in range(50):
        Net = net_force(Vo, watts)
        if Net < 1 and Net > -1:
            eq = True
            Stable_Vo = Vo
        else:
            eq = False
        print(f"Vo: {Vo}m/s\tNet: {Net}N\tEquilibrium: {eq}")

    print(f"Stable Vo: {Stable_Vo}m/s | {round(Stable_Vo*3.6,2)}km/h")