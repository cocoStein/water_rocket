from vecteur import Vecteur

class Rocket:
    def __init__(self, x0, v0, a0=Vecteur(0, -9.81), m=1):
        self.x0 = x0  # position initiale (Vecteur)
        self.v0 = v0  # vitesse initiale (Vecteur)
        self.a0 = a0  # vitesse initiale (Vecteur)
        self.m = m

    def MRUA(self, t):
        return self.x0 + self.v0*t + 0.5*self.a0*t*t

if __name__ == "__main__": #pour tester la class
    x0 = Vecteur(0,0)
    v0 = Vecteur(4.5,4)
    rocket = Rocket(x0, v0)
    print(rocket.MRUA(13))

    #while time < 20:
        ###time += 0.2
        ##add = Rocket.MRUA(pos_I, speed, g, time)
        #if round(add[0]) == 25:
        #print("temps :", time, add )

    time = 0
    xt = x0
    while time < 10 and xt.y >= 0:
        xt = rocket.MRUA(time)
        time += 0.1
        print(xt)
