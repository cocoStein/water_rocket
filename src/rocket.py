from water_rocket.src.vecteur import Vecteur


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

class Mover(Rocket):
    #selecteur entre les différents types de mover
    def __init__(self, t):
        self.t = t
        super().__init__(self)

#class Forces(Rocket):
#    #class des forces ou l'on peut rajouter et choisir les forces que l'on souhaite prendre en compte pour la somme des forces
#    def __init__(self, P = 1, Ff = 1):
#        self.P = P
#        self.Ff = Ff
#    P = 1       #pas la bonne solution pour le faire mais si je le fais avec la classe alors tous est décalé et je n'arriv plus à définir les def
#    Ff = 1
#    if P == 1:
#        def Poids(self):
#        #poids de l'objet
#            self.Poids = Vecteur(0, self.m * -9.81)
#            return self.Poids
#
#    elif Ff == 1:
#        def Force_frot(self):
#            #force de frottement de l'objet
#            self.Force_frot = self.v0 * self.v0
#            return self.Force_frot
#    else:
#        pass
#
#    def somme_f(self):
#        # somme des forces prisent en compte
#            return Vecteur(Forces.Poids() + Forces.Force_frot() #je ne comprends pas pk Forces n'a pas de Poids et de ff ?


class Energie(Mover):
    def energie(self):
        # type de mouvement avec l'énergie cinétique et potentielle
      return 0.5 * self.m * self.v0 * self.v0 + self.m * self.a0 * self.x0



class MRUA(Mover):
    def Mrua(self):
        # type de mouvenemt avec des MRUA basiques
        return self.x0 + self.v0 * self.t + 0.5 * self.a0 * self.t * self.t


class PasAPas(Mover):
    def pas_a_pas(self):
        #type de mouvement dit Pas à Pas (version 1)
        forces = Rocket.somme_f(self)
        self.a0 = Vecteur(forces.x / self.m, forces.y / self.m)
        self.v0 = self.a0 * self.t + self.v0
        self.x0 += self.v0 * self.t
        return self.x0

if __name__ == "__main__": #pour tester la class
    v0 = Vecteur(12,78)
    x0 = Vecteur(0,0)
    rrr = Rocket(v0,x0)
    rrr.t = 0.5
    print(rrr.somme_f())
    print(PasAPas.pas_a_pas(rrr))
    print(MRUA.Mrua(rrr))
    print(Energie.energie(rrr))






