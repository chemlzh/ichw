"""planets(circle-orbit-and-random-position).py

This program simulates the motion of planets in the solar system.

__author__ = "Li Zihan"
__pkuid__  = "1700011735"
__email__  = "chemlzh@pku.edu.cn"
"""
import math
import random
import turtle


Star = turtle.Pen()
Planet = []
PlanetColor = ["blue", "green", "red", "black", "orange", "cyan"]
PlanetRadius = [15.48, 28.93, 40.00, 60.95, 208.13, 381.48]
OrbitalPeriod = [2.41, 6.15, 10.00, 18.81, 118.63, 294.47]


def init():
    global Star
    Star.shape("circle")
    Star.pencolor("yellow")
    Star.fillcolor("yellow")
    for i in range(6):
        Planet.append(turtle.Pen())
        Planet[i].shape("circle")
        Planet[i].speed(0)
        Planet[i].shapesize(0.5, 0.5)
        Planet[i].pencolor(PlanetColor[i])
        Planet[i].fillcolor(PlanetColor[i])
        theta = random.uniform(0, 360) / 180 * math.pi
        x = math.cos(theta) * PlanetRadius[i]
        y = math.sin(theta) * PlanetRadius[i]
        Planet[i].penup()
        Planet[i].setposition(x, y)
        Planet[i].left(theta * 180 / math.pi + 90)
        Planet[i].pendown()


def motion():
    while True:
        for i in range(6):
            Planet[i].circle(PlanetRadius[i], 360 / OrbitalPeriod[i])


def main():
    init()
    motion()


if __name__ == "__main__":
    main()
