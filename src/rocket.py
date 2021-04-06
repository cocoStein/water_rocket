from water_rocket.src import vecteur as vc
from math import cos, sin, tan

class Rocket:
    def __init__(self, x, y, weight, speed=0): #MRU
        self.x = x
        self.y = y
        self.initial_rocket_speed = speed
        self.weight = weight

if __name__ == "__main__": #pour tester la class
    teta = 85
    distance_x = 20 #m
    rocket = Rocket(0, 0, 0, 15)
    acceleration = vc.Vecteur(0, -9.81)
    V0 = vc.Vecteur(rocket.initial_rocket_speed*cos(teta), rocket.initial_rocket_speed*sin(teta))

    total_height = vc.Vecteur.multivect(acceleration.x, acceleration.y , (0.5*distance_x**2)) #manque la division pour pouvoir faire avec des vecteurs


    g = -9.81
    th = -g*distance_x**2/(2*(rocket.initial_rocket_speed**2)*cos(teta)**2)+tan(teta)*distance_x
    print(th, "m en y")