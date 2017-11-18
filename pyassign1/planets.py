"""planets.py

This program simulates the motion of planets in the solar system.
The orbits are ellipse, and the data are set according to Wikipedia.
However, this program also has some disadvantages.
It draws the orbits one by one,
so the motion of planets aren't synchronous.
And for each orbit, it draws one degree by one degree, which is too slow.
Therefore, you'd better wait for a moment.
If you want to simulate other orbits, you can change the data,
for example, PlanetColor, PlanetRadius, OrbitalPeriod, Eccentricity,
RotationTime, and so on.
Notice: The value of Eccentricity should satisfy 0<Eccentricity<1!

__author__ = "Li Zihan"
__pkuid__  = "1700011735"
__email__  = "chemlzh@pku.edu.cn"
"""
from math import *
from random import *
from turtle import *


Star = Pen()
Planet = []
Phi = []
PlanetColor = ["blue", "lime", "red", "black", "orange", "cyan"]
PlanetRadius = [
                          15.4839572, 28.9332796, 40.0000044,
                          60.9464924, 208.1345204, 381.4828128
                          ]
OrbitalPeriod = [
                          0.2408467, 0.61519726, 1.0000174,
                          1.8808476, 11.862615, 29.447498
                          ]
Eccentricity = [
                       0.20563, 0.0067732, 0.016710,
                       0.093412, 0.048392, 0.054151
                       ]
RotationTime = 1 / 6
Step = 0


def init():
    # Initialization
    global Star, Step
    Star.shape("circle")
    Star.pencolor("yellow")
    Star.fillcolor("yellow")
    for i in range(6):
        Planet.append(Pen())
        Planet[i].shape("circle")
        Planet[i].speed(0)
        Planet[i].shapesize(0.5, 0.5)
        Planet[i].pensize(2)
        Planet[i].pencolor(PlanetColor[i])
        Planet[i].fillcolor(PlanetColor[i])
        Phi.append(uniform(0, 360) / 180 * pi)
        if Step == 0:
            Step = 2 * pi / OrbitalPeriod[i] * RotationTime
        else:
            Step = min(Step, 2 * pi / OrbitalPeriod[i] * RotationTime)
        x = cos(Phi[i]) * PlanetRadius[i] * (1 - Eccentricity[i])
        y = sin(Phi[i]) * PlanetRadius[i] * (1 - Eccentricity[i])
        Planet[i].penup()
        Planet[i].setposition(x, y)
        Planet[i].left(Phi[i] * 180 / pi + 90)
        Planet[i].pendown()


def KeplerEquation(e, M0, n):
    # The Calculation of Kepler's Equation
    Ans = M0
    for i in range(0, n):
        Ans = M0 + e * sin(Ans)
    return Ans


def motion():
    # The Simulation of planets
    M = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    E = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    R = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    Theta = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    global RotationTime
    while True:
        for i in range(6):
            M[i] = M[i] + 2 * pi / OrbitalPeriod[i] * RotationTime
            E[i] = KeplerEquation(Eccentricity[i], M[i], 8)
            Mu = 2 * atan2(
                                 sqrt(1 + Eccentricity[i]) * sin(E[i] / 2),
                                 sqrt(1 - Eccentricity[i]) * cos(E[i] / 2)
                                 )
            if Mu < 0:
                Mu = Mu + 2 * pi
            if Mu < Theta[i]:
                Mu = Mu + 2 * pi
            while Theta[i] < Mu:
                Theta[i] = Theta[i] + Step
                R = PlanetRadius[i] * (1 - Eccentricity[i] ** 2)
                R = R / (1 + Eccentricity[i] * cos(Theta[i]))
                x = cos(Theta[i] + Phi[i]) * R
                y = sin(Theta[i] + Phi[i]) * R
                Planet[i].setposition(x, y)
            Theta[i] = Theta[i] % (2 * pi)


def main():
    # The main function
    init()
    motion()


if __name__ == "__main__":
    main()
