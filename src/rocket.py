from water_rocket.src.vecteur import Vecteur
from math import *

class Rocket:
    #Definition de la fusée avec toutes les variables nécessaire au programme
    def __init__(self, v0,x0, a0=Vecteur(0, -9.81), m=1):
        self.x0 = x0  # position initiale (Vecteur)
        self.v0 = v0  # vitesse initiale (Vecteur)
        self.a0 = a0  # vitesse initiale (Vecteur)
        self.m = m    #masse initiale

    def somme_f(self):
        poids = Vecteur(self.m*0, self.m*-9.81)
        ff = Vecteur(-1/4*self.v0.x, -1/4*self.v0.y)
        self.somme_f = poids + ff
        return self.somme_f

    def energie(self):
        # type de mouvement avec l'énergie cinétique et potentielle
        self.v0 = sqrt(2*self.a0*self.x0)
        self.x0 = (self.v0*self.v0)/(2*self.a0)
         #0.5 * self.m * self.v0 * self.v0 + self.m * self.a0 * self.x0



class MRUA():
    def move(self, Rocket, dt):
        # type de mouvenemt avec des MRUA basiques
        Rocket.v0 += Rocket.a0*dt
        Rocket.x0 += Rocket.v0 * dt + 0.5 * Rocket.a0 * dt * dt
        #Rocket.x0 + Rocket.v0 * dt + 0.5 * Rocket.a0 * dt * dt


class PasAPas():
    def move(self, Rocket, dt):
        #type de mouvement dit Pas à Pas (version 1)
        forces = Rocket.somme_f(self)
        Rocket.a0 = Vecteur(forces.x / Rocket.m, forces.y / Rocket.m)
        Rocket.v0 = Rocket.a0 * dt + Rocket.v0
        Rocket.x0 += Rocket.v0 * dt

if __name__ == "__main__": #pour tester la class
    v0 = Vecteur(23,40)
    x0 = Vecteur(0,1)
    rrr = Rocket(v0,x0)
    g = 0
    #MRUA.move(rrr)
    #print(MRUA.move(rrr))
    while rrr.x0.y > 0:
        MRUA.move(g, Rocket=rrr, dt=0.25)
        print('x0:', rrr.x0)
        #print('v0:',rrr.v0)