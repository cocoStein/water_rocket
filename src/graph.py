from water_rocket.src.vecteur import Vecteur
import matplotlib.pyplot as plt
from water_rocket.src.rocket import *


x0 = Vecteur(0, 0)
v0 = Vecteur(21, 45)


stuck1 = Rocket(v0,x0)
time = 0

stuck2 = Rocket(v0,x0)
stuck2.t = 0
stuck3 = Rocket(v0,x0)
stuck3.t = 0.5

sss = PasAPas.pas_a_pas(stuck3)

xt = x0
x = [0]
y = [0]

i = [0]
k = [0]

p = [0]
l = [0]
plt.figure(1)
while xt.y >= 0:
    xt = MRUA.Mrua(stuck2)
    stuck2.t += 0.2
    x.append(xt.x)
    y.append(xt.y)
    #print(xt)

while stuck3.x0.y >= 0:
    stuck3.x0 = PasAPas.pas_a_pas(stuck3)
    i.append(stuck3.x0.x)
    k.append(stuck3.x0.y)
    #print(stuck3.x0)

plt.plot(x, y, '-')
plt.plot(i, k, '-ok')

plt.figure(2)
while time > 20:
    time += 1
    aaa = Energie.energie(stuck1)
    p.append(aaa)
    l.append(time)
    print(aaa)
plt.plot(p, l, '-')
plt.show()
