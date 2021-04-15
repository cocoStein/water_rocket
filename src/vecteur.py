class Vecteur:
    def __init__(self, x = [0, 0], y = [0, 0]):
        self.x = x
        self.y = y

    def addvect(x = [0, 0], y = [0, 0]):
        return ( [x[0] + y[0], x[1]+ y[1]])

    def multivect(x = [0, 0], y = 0):
        return ([x[0] * y, x[1] * y])

    def scalvect(x = [0, 0], y = [0, 0]):
        return ((x[0] * y[0]) + (x[1] * y[1]))

if __name__ == "__main__":

    K = [2,4]
    L = [2,3]
    J = Vecteur.addvect(K,L)
    print(J)

    print(Vecteur.multivect(K,3))

