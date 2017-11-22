"""planets.py

This program simulates the motion of planets in the solar system.
The orbits are ellipse, and the data are set according to Wikipedia.
With others' help, I upgrade my algorithm,
and now the planets rotate synchronously!
If you want to simulate other orbits, you can change the data,
for example, PlanetColor, PlanetRadius, OrbitalPeriod, Eccentricity,
RotationStep, and so on.
Notice: The value of Eccentricity should satisfy 0<Eccentricity<1!
In addition, RotationStep should be a positive integer!

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
AngularVelocity = []
PlanetColor = ["blue", "lime", "red", "black", "orange", "cyan"]
PlanetRadius = [
                15.4839572, 28.9332796, 40.0000044,
                60.9464924, 208.1345204, 381.4828128
                ]
OrbitalPeriod = [
                 24.08467, 61.519726, 100.00174,
                 188.08476, 1186.2615, 2944.7498
                 ]
Eccentricity = [
                0.20563, 0.0067732, 0.016710,
                0.093412, 0.048392, 0.054151
                ]
RotationStep = 2


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
        AngularVelocity.append(2 * pi / OrbitalPeriod[i])
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
    global RotationStep
    while True:
        for i in range(6):
            M[i] = M[i] + AngularVelocity[i]
            E[i] = KeplerEquation(Eccentricity[i], M[i], 10)
            Mu = 2 * atan2(
                           sqrt(1 + Eccentricity[i]) * sin(E[i] / 2),
                           sqrt(1 - Eccentricity[i]) * cos(E[i] / 2)
                           )
            if Mu < 0:
                Mu = Mu + 2 * pi
            if Mu < Theta[i]:
                Mu = Mu + 2 * pi
            Delta = Mu - Theta[i]
            for j in range(0, RotationStep):
                Theta[i] = Theta[i] + Delta / RotationStep
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
