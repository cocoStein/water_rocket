from water_rocket.src.vecteur import Vecteur
import matplotlib.pyplot as plt
from rocket import *
import logging

logging.getLogger('matplotlib.font_manager').disabled = True    #enleve les debugs de font de mathplotlib

v0 = Vecteur(50, 40)
x0 = Vecteur(0, 1)


poids = Poids()
trainee = Frottement()

forces = [poids, trainee]
method = PasAPas()
method1 = MRUA()

f1 = Rocket(v0, x0, forces, m=0.5)
f2 = Rocket(v0, x0, forces, m=0.5, C=cubeC, S=cubeS)
f3 = Rocket(v0, x0, forces, m=0.5, C=balleC, S=balleS)
f4 = Rocket(v0, x0, forces, m=0.5, C=coneC, S=coneS)
f5 = Rocket(v0, x0, forces, m=0.5, C=cylindreC, S=cylindreS)




x = [0]
y = [0]

i = [0]
k = [0]

p = [0]
l = [0]

n = [0]
m = [0]

b = [0]
d = [0]

while f1.x0.y >= 0:
    method.move(f1, 0.2)
    x.append(f1.x0.x)
    y.append(f1.x0.y)

while f2.x0.y >= 0:
    method.move(f2, 0.2)
    i.append(f2.x0.x)
    k.append(f2.x0.y)

while f3.x0.y >= 0:
    method.move(f3, 0.2)
    p.append(f3.x0.x)
    l.append(f3.x0.y)

while f4.x0.y >= 0:
    method.move(f4, 0.2)
    n.append(f4.x0.x)
    m.append(f4.x0.y)

while f5.x0.y >= 0:
    method.move(f5, 0.2)
    b.append(f5.x0.x)
    d.append(f5.x0.y)

plt.plot(x, y, 'b')
plt.plot(i, k, 'r')
plt.plot(p, l, 'k')
plt.plot(n, m, 'g')
plt.plot(b, d, 'm')

plt.show()

