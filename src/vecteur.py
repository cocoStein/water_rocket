class Vecteur:
    def __init__(self, x = 0, y = 0, r = 0, s = 0 ):
        self.x = x
        self.y = y
        self.r = r
        self.s = s

    def addvect(x = 0, y = 0, r = 0, s = 0):
        a = x + r
        b = y + s
        return ( a, b)
    def multivect(x = 0, y = 0, r = 0):
        c = x * r  #seulement pour multiplier un variable a un vecteur
        d = y * r
        return ( c, d)

k,l = Vecteur.addvect(2,1,-3,1)

print(k,l)
g, f = Vecteur.multivect(4,3,2)
print(g, f)
h = Vecteur.addvect(k,l,g,f)

print(h)

