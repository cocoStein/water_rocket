from water_rocket.src.rocket import Rocket
from water_rocket.src.vecteur import Vecteur
from math import cos, sin, tan, radians, degrees, sqrt
import matplotlib.pyplot as plt

x0 = Vecteur(0, 0)
m = 5
v0 = Vecteur(10, 500)
time = 0

#somme des forces
P = m*(-9.81)


x = [0]
y = [0]

coeff = 5

while x0.y >= 0:
    sum_f = P
    a = Vecteur(0, sum_f / m)

    v_t = a * time + v0
    x_t = v_t * coeff
    x0 = x0 + x_t
    v0 = v_t

    plt.plot(x0.x, x0.y, '-ok');
    x.append(x0.x)
    y.append(x0.y)
    time += coeff

rocket = Rocket(x0, v0, m)



plt.plot(x, y)
plt.show()

#conservation de l'énergie

energy_cin = 0.5*m*v0*v0
energy_pot = m*-9.81*x0.y