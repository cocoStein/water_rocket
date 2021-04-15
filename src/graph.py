from water_rocket.src import rocket as rckt
from water_rocket.src import vecteur as vctr

import matplotlib.pyplot as plt


pos_I = [0, 0]
speed = [12, 40]
g = [0, -9.81]
time = 0
add = rckt.Rocket.MRUA(pos_I, speed,g , time )

x = [0]
y = [0]

while add[1] > -0.1:
    time += 0.1
    add = rckt.Rocket.MRUA(pos_I, speed, g, time)
    x.append(add[0])
    y.append(add[1])

plt.plot(x, y)
plt.show()
