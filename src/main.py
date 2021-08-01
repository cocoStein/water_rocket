#import
from water_rocket.src.rocket import *
import pygame
import sys

pygame.init()

#Variables
WIDTH = 1080
HEIGHT = 720
running = True
clock = pygame.time.Clock()


#charcher les images
rocket_img = pygame.image.load('/Users/corentinsteinhauser/PycharmProjects/water_rocket/water_rocket/src/img/rocket.png')
sky_img = pygame.image.load('/Users/corentinsteinhauser/PycharmProjects/water_rocket/water_rocket/src/img/SKY.png')
dirt_img = pygame.image.load('/Users/corentinsteinhauser/PycharmProjects/water_rocket/water_rocket/src/img/dirt.png')

rocket_imgX, rocket_imgY = rocket_img.get_size()
dirt_imgX, dirt_imgY = dirt_img.get_size()

#charger les polices
police = pygame.font.Font(None, 50)
police_subtitle = pygame.font.Font(None, 25)

#création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Rocket")

# Rocket
v0 = Vecteur(50,80)
x0 = Vecteur(0,1)
rrr = Rocket(v0,x0)
g = 0


def draw_text(text, font, color, surface, x, y):
    #modules pour afficher du texte

    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False



def main_menu():
    #module du menu

    while True:

        screen.fill((10, 10, 10))
        draw_text('main menu', police, (255, 255, 255), screen, 20, 20)

        #obtenir la position de la souris
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 295, 50)
        button_2 = pygame.Rect(50, 200, 225, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                simulator()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (0, 200, 100), button_1)
        pygame.draw.rect(screen, (0, 200, 100), button_2)

        draw_text('Rocket simulator', police, (255, 255, 255), screen, 50, 110)
        draw_text('Commandes', police, (255, 255, 255), screen, 50, 210)
        draw_text('Scores', police, (255, 255, 255), screen, 50, 310)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def simulator():
    #module de la simulation

    running = True
    Rocket_x = rrr.x0.x
    Rocket_y =  rrr.x0.y +570

    text_move = police.render('Type de mover:', True, (0, 0, 0))

    while running:
        # background
        screen.blit(sky_img, (0, 0))
        screen.blit(dirt_img, (0, HEIGHT - 100))

        # scale image de la fusee en fonction de sa position
        scaleRock_x = rocket_imgX + Rocket_x/50
        scaleRock_y = rocket_imgY + Rocket_y/50
        rocket2 = pygame.transform.scale(rocket_img, (int(scaleRock_x),int(scaleRock_y)))

        scaleDirt_x = dirt_imgX + Rocket_x / 50
        scaleDirt_y = dirt_imgY + Rocket_y / 15
        dirt2 = pygame.transform.scale(dirt_img, (int(scaleDirt_x), int(scaleDirt_y)))

        # afficher les images
        screen.blit(dirt2, (0, HEIGHT - 100))
        screen.blit(rocket2, (Rocket_x, Rocket_y))
        screen.blit(text_move, (0, 0))


        MRUA.move(g, Rocket=rrr, dt=0.25)
        Rocket_x = rrr.x0.x
        Rocket_y = -rrr.x0.y + 570


        if rrr.x0.y < 0:
            running = False
            print('x0:', rrr.x0)
            rrr.v0 = Vecteur(50,80)
            rrr.x0 = Vecteur(0,1)



        # check pour les event
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
                if event.key == pygame.K_3:
                    Rocket_x, Rocket_y =  pygame.mouse.get_pos()
                    print(pygame.mouse.get_pos())
                    Rocket_x -= 45
                    Rocket_y -= 50


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(30)

def options():
    #module des commandes et options de la simulation

    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('Commandes', police, (255, 255, 255), screen, 20, 20)
        draw_text('1. Appuyez sur 1,2 pour changer de mover', police_subtitle, (255, 255, 255), screen, 60, 60)
        draw_text('2. Appuyez sur espace pour remmettre la fusée à zero', police_subtitle, (255, 255, 255), screen, 60, 80)
        draw_text('3. Appuyez sur 3 pour remmettre la fusée à la position de votre souris', police_subtitle, (255, 255, 255), screen, 60,
                  100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)

main_menu()


clock.tick(30)

# update la fenêtre
pygame.display.flip()