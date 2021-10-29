from vecteur import *
from settings import *
from rocket import*



class Poids():
    def apply(self, rocket,dt=0):
        return Vecteur(rocket.masse()*0, rocket.masse()*-9.81)


class Frottement():
    def apply(self, rocket,dt = 0):
        return  -(0.5 * rocket.forme.C * rocket.forme.S * 1.21 * (rocket.v0**2))
class Poussee():
    def apply(self,rocket,dt = 0):
         
         volume0 = rocket.forme.volume-rocket.volumeWater()

         rocket.masseTime(dt)
         volume1 = rocket.forme.volume-rocket.volumeWater()

         rocket.P = rocket.P * volume0 / volume1

         F = rocket.P * 0.00346 #aire du bouchon de la bouteille
         if volume0 == volume1:
             F = 0

         return Vecteur(F* 0.2,F*0.8)
class Archimède():
    def apply(self,rocket,dt = 0):
        return Vecteur(0,1.21 * rocket.forme.volume * 9.81)


if __name__ == "__main__":
    print("hello")
    v0 = Vecteur(0,0)
    x0 = Vecteur(0,0)
    poussee = Poussee()
    poids = Poids()
    frottement = Frottement()

    forces = [poussee,poids]
    rrr = Rocket(v0,x0,forces,mCarburant = 1)

    print(poussee.apply(rrr,0.2),poids.apply(rrr,0.2),frottement.apply(rrr,0.2))

