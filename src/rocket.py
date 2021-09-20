from vecteur import Vecteur
from math import *
from forces import *

class Rocket:
    #Definition de la fusée avec toutes les variables nécessaire au programme
    def __init__(self, v0,x0,forces=[], a0=Vecteur(0, -9.81), m=1):
        self.x0 = x0  # position initiale (Vecteur)
        self.v0 = v0  # vitesse initiale (Vecteur)
        self.a0 = a0  # vitesse initiale (Vecteur)
        self.m = m    #masse initiale
        self.forces = forces  #Selecteur de force

    #def somme_f(self):
    #    poids = Vecteur(self.m*0, self.m*-9.81)
    #    ff = -0.25*self.v0
    #    self.somme_f = poids + ff
    #    return self.somme_f

    def somme_f(self):
        Sf = Vecteur(0,0)
        for force in self.forces:
               Sf = Sf + force.apply(self)
        return Sf
    def energie(self):
        # type de mouvement avec l'énergie cinétique et potentielle
        self.v0 = sqrt(2*self.a0*self.x0)
        self.x0 = (self.v0*self.v0)/(2*self.a0)
        #0.5 * self.m * self.v0 * self.v0 + self.m * self.a0 * self.x0

#forces = []
#
#class Forces:
#    def __init__(self):
#        pass
#
#    def poids(self, rocket):
#        poids = Vecteur(rocket.m * 0, rocket.m * -9.81)
#        return poids
#
#    def frottement(self, rocket):
#        frottement = Vecteur(-1/4*Rocket.v0.x, -1/4*Rocket.v0.y)
#        return frottement
#
#    def sum(self, rocket):
#        sum = Vecteur(0, 0)
#        for force in forces:
#            if force == "poids":
#                sum += self.poids(rocket)
#            if force == "":
#                sum += self.frottement(rocket)
#        return sum
#

class MRUA():
    def move(self, rocket, dt):
        # type de mouvenemt avec des MRUA basiques
        rocket.v0 += rocket.a0*dt
        rocket.x0 += rocket.v0 * dt + 0.5 * rocket.a0 * dt * dt
        #Rocket.x0 + Rocket.v0 * dt + 0.5 * Rocket.a0 * dt * dt

class PasAPas():
    def move(self, rocket, dt):
        #type de mouvement dit Pas à Pas (version 1)
        forces = rocket.somme_f()
        rocket.a0 = forces / rocket.m
        rocket.v0 = rocket.a0 * dt + rocket.v0
        rocket.x0 += rocket.v0 * dt

if __name__ == "__main__": #pour tester la class
    v0 = Vecteur(50,40)
    x0 = Vecteur(0,1)
    poids = Poids()
    frottement = Frottement()
    
    forces = [poids, frottement]
    rrr = Rocket(v0,x0,forces)
    method = PasAPas()
    method.move(rrr, 0.5)
    print(rrr.x0)