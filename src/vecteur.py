import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class Vecteur:
    def __init__(self, x, y):
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

    def __mul__(self, constante):
        if isinstance(constante, (int, float)):
            return Vecteur(
                self.x * constante,
                self.y * constante,
            )
        logging.warning("La multiplication d'un Vecteur n'est définie qu'avec un scalaire")
        raise NotImplementedError

    __rmul__ = __mul__

    def scalvect(x = [0, 0], y = [0, 0]):
        return ((x[0] * y[0]) + (x[1] * y[1]))

if __name__ == "__main__":
    v1 = Vecteur(2,3)
    v2 = Vecteur(4,-3)

    print(v1 - v2)
    print(v1 + v2)

    print(v1*3)
    print(3*v1)

    print(v1*v2)


