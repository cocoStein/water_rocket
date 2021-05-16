from water_rocket.src.rocket import Rocket
from water_rocket.src.vecteur import Vecteur
from math import cos, sin, tan, radians, degrees
import matplotlib.pyplot as plt
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


x0 = Vecteur(0, 0)

x0.y = float(input("Hauteur de la fusée:"))
if x0.y > 150:
    logging.warning("La valeur de la hauteur de la fusée ne corresponds pas")
    raise NotImplementedError

v_pas0 = float(input("vitesse de la fusée:"))

theta = float(input("Angle de la fusée:"))
if theta > 360:
    logging.warning("L'angle de la fusée est trop élever")
    raise NotImplementedError
theta_rad = radians(theta)
print(theta_rad)

v0 = Vecteur(cos(theta_rad)*v_pas0, sin(theta_rad)*v_pas0)

if theta == 90 or theta == 270:
    v0 = Vecteur(0, sin(theta_rad)*v_pas0)

rocket = Rocket(x0, v0)
time = 0

xt = x0
x = [0]
y = [0]

while time < 50 and xt.y >= 0:
    xt = rocket.MRUA(time)
    time += 0.1
    x.append(xt.x)
    y.append(xt.y)

plt.plot(x, y)
plt.show()
