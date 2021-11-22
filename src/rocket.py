from math import *
from forces import *
from settings import *


class Rocket:
    # Definition de la fusée avec toutes les variables nécessaire au programme

    def __init__(self, v0, x0, forces=[], a0=Vecteur(0, -9.81), forme = bouteille, mRocket=0.1, mCarburant = 0.5, P = 10000 ):
        self.x0 = x0  # position initiale (Vecteur)
        self.v0 = v0  # vitesse initiale (Vecteur)
        self.a0 = a0  # acceleration initiale (Vecteur)
        self.forces = forces  # Liste pour le selecteur de force
        self.forme = forme  # Forme de la fusée (c'est une classe)
        self.mRocket = mRocket # Masse de la rocket sans le carburant
        self.mCarburant = mCarburant # Masse du carburant
        self.P = P # Pression dans la bouteille en pascal
    def somme_f(self,dt = 0):
        """
        Retourne la somme des forces qui aggisent sur la rocket à un moment
        :param dt: float
        :return: Vecteur
        """
        Sf = Vecteur(0,0)
        for force in self.forces:
               Sf = Sf + force.apply(self, dt)
        return Sf
    def energie(self):
        """
        calculer l'energie de la fusée
        :return: float
        """

        potentielle = self.masse() * self.x0.y * 9.81
        cinetique = 0.5 * self.masse() * self.v0.norme()**2
        return potentielle + cinetique
    def volumeWater(self):
        """
        Retourne le volume de l'eau dans la fusée
        :return: float
        """
        if self.mCarburant > 0:
            M = self.mCarburant/1000
        else:
            M = 0
        return M

    def masseTime(self,dt=0):
        """
        Change la masse du carburant dans la fusée
        :param dt: float
        :return: None
        """
        if self.mCarburant > 0:
            self.mCarburant = self.mCarburant - 0.5*dt
            self.mCarburant = round(self.mCarburant,2)
        else:
            self.mCarburant = 0

    def masse(self):
        """
        Retourne la masse de la fusée
        :return: float
        """
        return self.mRocket + self.mCarburant


class MRUA():
    def move(self, rocket, dt):
        """
        Change la position et la vitesse de la rocket d'un certain instant dt d'une méthode de mouvement uniformément accéléré
        :param rocket: Rocket
        :param dt: float
        :return: None
        """
        rocket.v0 += rocket.a0*dt
        rocket.x0 += rocket.v0 * dt
        #Rocket.x0 + Rocket.v0 * dt + 0.5 * Rocket.a0 * dt * dt

class PasAPas():
    def move(self, rocket, dt):
        """
        Change la position, la vitesse et l'accélération de la rocket d'un certain instant.
        :param rocket: Rocket
        :param dt: float
        :return: None
        """
        forces = rocket.somme_f(dt)
        rocket.a0 = forces / rocket.masse()
        rocket.v0 = rocket.a0 * dt + rocket.v0
        rocket.x0 += rocket.v0 * dt

if __name__ == "__main__": #pour tester la class
    v0 = Vecteur(0, 0)
    x0 = Vecteur(0, 1)
    poids = Poids()
    poussee = Poussee()
    trainee = Frottement()
    archimede = Archimede()

    forces = [poussee, poids]
    rrr = Rocket(v0, x0, forces)
    pas = PasAPas()
    rrr2 = Rocket(v0, x0, forces)
    mua = MRUA()

    for i in range(10):
        pas.move(rrr, 0.2)
        mua.move(rrr2, 0.2)
        print("-----------------")
        print(rrr.v0)
        print(rrr2.x0)