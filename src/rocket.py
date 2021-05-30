from water_rocket.src.vecteur import Vecteur

class Rocket:
    def __init__(self, v0,x0, a0=Vecteur(0, -9.81), m=1):
        self.x0 = x0  # position initiale (Vecteur)
        self.v0 = v0  # vitesse initiale (Vecteur)
        self.a0 = a0  # vitesse initiale (Vecteur)
        self.m = m  #masse initiale
        self.energie = 0.5*self.m*self.v0.y*self.v0.y + self.m*self.a0.y*self.x0.y
        self.poids = self.m*self.a0.y


class Mover(Rocket):

    def MRUA(self, t):
        xt = self.x0 + self.v0*t + 0.5*self.a0*t*t
        return xt

    def pas_a_pas(self, coeff):
        sum_f_y = self.poids    #uniquement en y
        sum_f_x = 0
        a0 = Vecteur(sum_f_x / self.m, sum_f_y / self.m)
        v_t = a0 * coeff + self.v0
        x_t = v_t * coeff
        self.v0 = v_t
        self.x0 = self.x0 + x_t
        return self.x0, self.v0

if __name__ == "__main__": #pour tester la class
    x2 = Vecteur(12, 21)
    v1 = Vecteur(36, 545)

    qw= Mover(v1, x2)
    rt, ht = qw.pas_a_pas(4)
    print(rt, ht)


