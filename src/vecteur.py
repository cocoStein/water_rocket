import logging
from math import *

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class Vecteur:
    def __init__(self, x = 0, y= 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

    def __add__(self, other):
        """
        Retourne l'addition de deux vecteurs
        :param other: Vecteur
        :return: Vecteur
        """
        return Vecteur(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other):
        """
        Retourne la soustraction de deux vecteurs
        :param other: Vecteur
        :return: Vecteur
        """
        return Vecteur(
            self.x - other.x,
            self.y - other.y,
        )
    def __neg__(self):
        """
        Retourne le vecteur avec des paramètres négatifs
        :return: Vecteur
        """
        return Vecteur(
                -1*self.x,
                -1*self.y,
                )

    def __mul__(self, other):
        """
        Retourne soit la mulitplication de deux vecteurs soit la multiplication d'un vecteur et d'une constante
        :param other: Vecteur ou float
        :return: Vecteur ou float
        """
        if isinstance(other, (int, float)):
            return Vecteur(
                self.x * other,
                self.y * other,
            )
        elif isinstance(other, Vecteur):
            return self.x * other.x + self.y * other.y
        logging.warning("La multiplication d'un Vecteur n'est définie qu'avec un scalaire")
        raise NotImplementedError

    __rmul__ = __mul__

    def __truediv__(self, other):
        """
        Divise les paramètres du vecteur par une constante
        :param other: int ou float
        :return: Vecteur
        """
        if isinstance(other, (int, float)):

            return Vecteur(
                self.x / other,
                self.y / other
            )
        logging.warning("On ne peut diviser un vecteur qu'avec un nombre.")
        raise NotImplementedError

    def __pow__(self,other):
        """
        Retourne un vecteur avec les paramètres à la puissance choissie
        :param other: int
        :return: Vecteur
        """
        return Vecteur(
            self.x**other,
            self.y**other
        )
    def norme(self):
        """
        Retourne la norme d'un vecteur
        :return: float
        """
        return sqrt(self.x**2 + self.y**2)

    def autoMul(self):
        """
        Retourne  le carré de chaques paramètres en gardant le signe de celui-ci
        :return: Vecteur
        """
        return Vecteur(
            self.x *abs(self.x),
            self.y * abs(self.y)
        )




if __name__ == "__main__":
    v1 = Vecteur(2,3)
    v2 = Vecteur(4,-3)

    print(v1 - v2)
    print(v1 + v2)

    print(v1*3)
    print(3*v1)

    print(v1 * v2)
    print(-v2)

    print(v1/2)
    print(v1**2)
    print(v2.autoMul())

    print(v1.norme())
