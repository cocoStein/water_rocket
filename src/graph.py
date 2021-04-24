from water_rocket.src.rocket import Rocket
from water_rocket.src.vecteur import Vecteur
from numpy import cos, sin, tan, radians
import matplotlib.pyplot as plt
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

def Cos(a):
    return cos(radians(a))
def Sin(a):
    return sin(radians(a))
def Tan(a):
    return tan(radians(a))
x0 = Vecteur(0, 0)

x0.y = float(input("Hauteur de la fusée:"))
if x0.y not in range(0,150):
    logging.warning("La valeur de la hauteur de la fusée ne corresponds pas")
    raise NotImplementedError
v_pas0 = float(input("vitesse de la fusée:"))

teta = int(input("Angle de la fusée:"))
if teta not in range(1,89):
    logging.warning("L'angle de la fusée est trop élever")
    raise NotImplementedError

v0 = Vecteur(Cos(teta)*v_pas0, Sin(teta)*v_pas0)
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
