from water_rocket.src.rocket import *
import pygame


pygame.init()

#Variables
WIDTH = 1080
HEIGHT = 720
running = True

x0 = Vecteur(0, 0)
v0 = Vecteur(21, 45)
xt = x0

stuck1 = Rocket(v0,x0)
time = 0
stuck1.t = 0.5


#charcher les images
rocket_img = pygame.image.load('/Users/corentinsteinhauser/PycharmProjects/water_rocket/water_rocket/src/img/rocket.png')

#création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Rocket")



while running:
    #couleur pour le backgground
    screen.fill((18, 182, 195))
    pygame.display.flip()

    #afficher les images
    screen.blit(rocket_img, (0, HEIGHT-60))
    pygame.display.flip()

    #boucle de la fusee
    while stuck1.x0.y > HEIGHT-60:
        MRUA.move(stuck1)

    #check si la fenêtre est ouverte
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
