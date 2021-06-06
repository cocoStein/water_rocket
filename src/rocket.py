from water_rocket.src.vecteur import Vecteur



class Rocket:
    def __init__(self, v0,x0, a0=Vecteur(0, -9.81), m=1):
        self.x0 = x0  # position initiale (Vecteur)
        self.v0 = v0  # vitesse initiale (Vecteur)
        self.a0 = a0  # vitesse initiale (Vecteur)
        self.m = m  #masse initiale


class Mover(Rocket):
    pass

class Forces(Mover):
    def Poids(self):
        self.Poids = Vecteur(0, Mover.m * -9.81)
        return self.Poids

    def Force_frot(self):
        self.Force_frot = Mover.v0 * Mover.v0

    def somme_f(self):
        return self.Poids + self.Force_frot


class Energie(Mover):
    def energie(self):
        self.energie = 0.5 * Mover.m * Mover.v0 * Mover.v0 + Mover.m * Mover.a0 * Mover.x0
        return self.energie


class MRUA(Mover):
    def Mrua(self):
        Mover.x0 = Mover.x0 + Mover.v0 * Mover.t + 0.5 * Mover.a0 * Mover.t * Mover.t
        return Mover.x0


class PasAPas(Mover):
    def pas_a_pas(self):
        Mover.a0 = Vecteur(Forces.somme_f / Mover.m)
        Mover.v0 = Mover.a0 * Mover.t + Mover.v0
        Mover.x0 += Mover.v0 * Mover.t
        return Mover.x0, Mover.v0
if __name__ == "__main__": #pour tester la class
    gten = Rocket(12, 5, 65)
    gten = Energie.energie(gten)


