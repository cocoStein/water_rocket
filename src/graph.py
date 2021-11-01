from water_rocket.src.vecteur import Vecteur
import matplotlib.pyplot as plt
from rocket import *
import logging

logging.getLogger('matplotlib.font_manager').disabled = True    #enleve les debugs de font de mathplotlib

v0 = Vecteur(13.5, 49)
x0 = Vecteur(0, 1)

#toutes formes

poids = Poids()
trainee = Frottement()
poussee = Poussee()
archimede = Archimede()

forces = [poussee, poids, trainee]
method = PasAPas()
method1 = MRUA()

f1 = Rocket(Vecteur(0, 0), x0, forces,)
f2 = Rocket(v0, x0, forces,)
f3 = Rocket(v0, x0, forces, forme=cone)
f4 = Rocket(v0, x0, forces, forme=cylindre)
f5 = Rocket(v0, x0, forces, forme=pyramide)



x = []
y = []

i = [0]
k = [0]

p = [0]
l = [0]

n = [0]
m = [0]

b = [0]
d = [0]

t = 0
while f1.x0.y >= 0:
    y.append(0)
    x.append(t)
    t += 0.2
    method1.move(f1, 0.2)



while f2.x0.y >= 0:
    method1.move(f2, 0.2)
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

plt.plot(x, y, 'b', label="Energie")
#plt.plot(i, k, 'r', label="MUA")
#plt.plot(p, l, 'k', label="cone")
#plt.plot(n, m, 'g', label="cylindre")
#plt.plot(b, d, 'm', label="pyramide")


plt.legend()
plt.show()