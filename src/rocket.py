from water_rocket.src.vecteur import Vecteur



class Rocket:
    def __init__(self, v0,x0, a0=Vecteur(0, -9.81), m=1):
        self.x0 = x0  # position initiale (Vecteur)
        self.v0 = v0  # vitesse initiale (Vecteur)
        self.a0 = a0  # vitesse initiale (Vecteur)
        self.m = m  #masse initiale


class Mover(Rocket):
    def __init__(self, t):
        self.t = t
        super().__init__(self)

class Forces(Mover):
    def Poids(self):
        self.Poids = Vecteur(0, self.m * -9.81)
        return self.Poids

    def Force_frot(self):
        self.Force_frot = self.v0 * self.v0

    def somme_f(self):
        return Vecteur(self.Poids + self.Force_frot)


class Energie(Mover):
    def energie(self):
        self.energie = 0.5 * self.m * self.v0 * self.v0 + self.m * self.a0 * self.x0
        return self.energie


class MRUA(Mover):
    def Mrua(self):
        self.x0 = self.x0 + self.v0 * self.t + 0.5 * self.a0 * self.t * self.t
        return self.x0


class PasAPas(Mover):
    def pas_a_pas(self):
        self.a0 = Vecteur(Forces.somme_f / Vecteur(self.m))
        self.v0 = self.a0 * self.t + self.v0
        self.x0 += self.v0 * self.t
        return self.x0, self.v0

if __name__ == "__main__": #pour tester la class
    gten = Rocket(10, 1, 23)
    gten = Energie.energie(gten)
    print(gten)

    fff = Rocket(2, 1, 3)
    fff.t = 1
    fdd = MRUA.Mrua(fff)
    print(fdd)

