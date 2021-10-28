from math import *
from forces import *
from settings import *

class Rocket:
    # Definition de la fusée avec toutes les variables nécessaire au programme

    def __init__(self, v0, x0, forces=[], a0=Vecteur(0, -9.81), forme = bouteille, mRocket=1, mCarburant = 0.5, P = 5000 ):
        self.x0 = x0  # position initiale (Vecteur)
        self.v0 = v0  # vitesse initiale (Vecteur)
        self.a0 = a0  # vitesse initiale (Vecteur)
        self.forces = forces  # Selecteur de force
        self.forme = forme  #forme de la fusée (c'est une classe)
        self.mRocket = mRocket #masse de la rocket sans le carburant
        self.mCarburant = mCarburant #masse du carburant
        self.P = P #pression dans la bouteille en pascal
    def somme_f(self,dt = 0):
        Sf = Vecteur(0,0)
        for force in self.forces:
               Sf = Sf + force.apply(self, dt)
        return Sf
    def energie(self):
        # type de mouvement avec l'énergie cinétique et potentielle
        potentielle = self.m * self.x0.y * 9.81
        cinetique = 0.5 * self.m * self.v0.norme()**2
        return potentielle + cinetique
    def volumeWater(self):
        if self.mCarburant > 0:
            M = self.mCarburant/1000
        else:
            M = 0
        return M

    def masseTime(self,dt=0):
        if self.mCarburant > 0:
            self.mCarburant = self.mCarburant - 0.25*dt
            self.mCarburant = round(self.mCarburant,2)
        else:
            self.mCarburant = 0

    def masse(self):
        return self.mRocket + self.mCarburant


class MRUA():
    def move(self, rocket, dt):
        # type de mouvenemt avec des MRUA basiques
        rocket.v0 += rocket.a0*dt
        rocket.x0 += rocket.v0 * dt + 0.5 * rocket.a0 * dt * dt
        #Rocket.x0 + Rocket.v0 * dt + 0.5 * Rocket.a0 * dt * dt

class PasAPas():
    def move(self, rocket, dt):
        #type de mouvement dit Pas à Pas
        forces = rocket.somme_f(dt)
        rocket.a0 = forces / rocket.masse()
        rocket.v0 = rocket.a0 * dt + rocket.v0
        rocket.x0 += rocket.v0 * dt

if __name__ == "__main__": #pour tester la class
    v0 = Vecteur(0,0)
    x0 = Vecteur(0,1)
    poids = Poids()
    poussee = Poussee()
    trainee = Frottement()

    forces = [poids,trainee,poussee]
    rrr = Rocket(v0,x0, forces)
    pas = PasAPas()

    for i in range(100):
        rrr.masseTime(0.023)
        print(rrr.mCarburant)




