from water_rocket.src.rocket import Mover
from water_rocket.src.vecteur import Vecteur
import matplotlib.pyplot as plt

coeff = 0.5
t = 0
t2 = 0

v0 = Vecteur(12, 46)
x0= Vecteur(0,0)

x = [x0.x]
y = [x0.y]

w = [x0.x]
z = [x0.y]



Stuka = Mover(v0, x0)
Stuka2 = Mover(v0, x0)
B17 = Mover(v0, x0)

i = [t2]
k = [B17.energie]

xt = x0
plt.figure(1)
while xt.y >= 0:
    xt = Stuka2.MRUA(t)
    t += 0.1
    plt.plot(Stuka2.x0.x, Stuka2.x0.y)
    w.append(xt.x)
    z.append(xt.y)

plt.plot(w, z)


while Stuka.x0.y >= 0:      #pas-a-pas
    sqw, fff = Stuka.pas_a_pas(coeff)
    plt.plot(Stuka.x0.x, Stuka.x0.y)
    x.append(Stuka.x0.x)
    y.append(Stuka.x0.y)
    print(Stuka.energie)
plt.plot(x, y, '-ok')


plt.figure(2)
#while B17.x0.y >= 0:
#    B17.x0, B17.v0 = B17.pas_a_pas(t2)
#    plt.plot(t2, B17.energie)
#    i.append(t2)
#    k.append(B17.energie)
#    t2 += 0.1
#
#plt.plot(i, k)

plt.show()

