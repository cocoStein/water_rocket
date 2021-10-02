from vecteur import *

class Poids():
    def apply(self, rocket):
        return Vecteur(rocket.m*0, rocket.m*-9.81)

class Frottement():
    def apply(self, rocket):
        return -0.25 * rocket.v0


if __name__ == "__main__":
    print("hello")