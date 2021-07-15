from water_rocket.src.rocket import *
import pygame


pygame.init()

#Variables
WIDTH = 1080
HEIGHT = 720
running = True
clock = pygame.time.Clock()
mover = "MRUA"

Rocket_x = 0
Rocket_y = HEIGHT-160

#charcher les images
rocket_img = pygame.image.load('/Users/corentinsteinhauser/PycharmProjects/water_rocket/water_rocket/src/img/rocket.png')
sky_img = pygame.image.load('/Users/corentinsteinhauser/PycharmProjects/water_rocket/water_rocket/src/img/SKY.png')
dirt_img = pygame.image.load('/Users/corentinsteinhauser/PycharmProjects/water_rocket/water_rocket/src/img/dirt.png')

#charger les polices
police = pygame.font.Font(None, 50)

#création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Rocket")

text_move = police.render('Type de mover:', True, (0, 0, 0))

while running:
    #background
    #screen.fill((18, 182, 195))
    screen.blit(sky_img, (0,0))
    screen.blit(dirt_img, (0, HEIGHT-100))

    #afficher les images
    screen.blit(rocket_img, (Rocket_x, Rocket_y))
    screen.blit(text_move, (0, 0))

    '''
    #boucle de la fusee
    while stuck1.x0.y > HEIGHT-60:
        MRUA.move(stuck1)
        
    '''

    Rocket_x += 1
    Rocket_y -= 1.5

    #check pour les event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                text_move = police.render('Type de mover: MRUA', True, (0, 0, 0))
            if event.key == pygame.K_2:
                text_move = police.render('Type de mover: PAS A PAS', True, (0, 0, 0))
            if event.key == pygame.K_SPACE:
                Rocket_x = 0
                Rocket_y = HEIGHT - 160

    clock.tick(60)
    # update la fenêtre
    pygame.display.flip()