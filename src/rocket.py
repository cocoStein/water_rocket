from water_rocket.src import vecteur as vctr

class Rocket:
    def __init__(self, x, y, weight, speed=0):
        self.x = x
        self.y = y
        self.initial_rocket_speed = speed
        self.weight = weight

    def MRUA(position_I = [0, 0], speed = [0, 0], g = [0, -9.81], time = 0):
        return vctr.Vecteur.addvect(vctr.Vecteur.addvect(position_I, vctr.Vecteur.multivect(speed, time)), vctr.Vecteur.multivect(g,(time**2)*0.5))

if __name__ == "__main__": #pour tester la class
    pos_I = [0, 0]
    speed = [12, 40]
    g = [0, -9.81]
    time = 0
    add = Rocket.MRUA(pos_I, speed,g , time )
    essaies = 0

    #while time < 20:
        ###time += 0.2
        ##add = Rocket.MRUA(pos_I, speed, g, time)
        #if round(add[0]) == 25:
        #print("temps :", time, add )

    while add[1] > -0.00001:
        time += 0.001
        essaies += 1
        add = Rocket.MRUA(pos_I, speed, g, time)
        print("essaies n°", essaies, "Pour un temps de:", time, add )