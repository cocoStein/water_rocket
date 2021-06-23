from water_rocket.src.vecteur import Vecteur
import matplotlib.pyplot as plt
from water_rocket.src.rocket import *
import logging

logging.getLogger('matplotlib.font_manager').disabled = True    #enleve les debugs de font de mathplotlib


x0 = Vecteur(0, 0)
v0 = Vecteur(21, 45)

xt = x0

stuck1 = Rocket(v0,x0)
time = 0
stuck1.t = 0.5

stuck2 = Rocket(v0,x0)
stuck2.t = 0
stuck2Energie = Rocket(v0,xt)

stuck3 = Rocket(v0,x0)
stuck3.t = 0.5
time3 = 0





x = [0]
y = [0]

i = [0]
k = [0]

p = [0]
l = [stuck3.energie()]

n = [0]
m = [stuck2.energie()]


while stuck2Energie.x0.y >= 0:
    stuck2Energie.x0 = MRUA.mrua(stuck2)
    stuck2.t += 0.2
    x.append(stuck2Energie.x0.x)
    y.append(stuck2Energie.x0.y)
    #print(xt)
    nrj = stuck2Energie.energie()
    time += stuck2.t
    n.append(time)
    m.append(nrj)

while stuck3.x0.y >= 0:
    stuck3.x0 = PasAPas.pas_a_pas(stuck3)
    i.append(stuck3.x0.x)
    k.append(stuck3.x0.y)
    #print(stuck3.x0)
    aaa = stuck3.energie()
    time3 += stuck3.t
    p.append(time3)
    l.append(aaa)
    print(aaa)

plt.figure(1)
plt.plot(x, y, '-', color='blue')
plt.plot(i, k, '-ok', color='black')

plt.figure(2)
plt.plot(p, l, '-', color='black')
plt.figure(3)
plt.plot(n, m, '-', color='blue')

plt.show()
