import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class Vecteur:
    def __init__(self, x = 0, y= 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

    def __add__(self, other):
        return Vecteur(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other):
        return Vecteur(
            self.x - other.x,
            self.y - other.y,
        )
    def __neg__(self):
        return Vecteur(
                -1*self.x,
                -1*self.y,
                )

    def __mul__(self, other):
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
        if isinstance(other, (int, float)):

            return Vecteur(
                self.x / other,
                self.y / other
            )
        logging.warning("On ne peut diviser un vecteur qu'avec un nombre.")
        raise NotImplementedError




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


