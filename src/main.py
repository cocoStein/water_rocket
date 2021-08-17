# import
from water_rocket.src.settings import *
from water_rocket.src.rocket import *
import pygame
import sys
import time

pygame.init()


# création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Rocket")


# Rocket
v0 = Vecteur(90, 100)
x0 = Vecteur(0, 1)
rrr = Rocket(v0, x0)
g = 0


def input():
    #module des inputs pour la simulation

    running = True
    click = False
    input_box1 = InputBox(175, 100, 10, 32)
    input_box2 = InputBox(160, 200, 100, 32)
    input_boxes = [input_box1, input_box2]


    while running:
        screen.fill((0, 0, 0))

        # obtenir la position de la souris
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(HEIGHT/2, WIDTH/2, 295, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                simulator()
                running = True
                click = False
                #v0 = Vecteur(int(input_box2.text), 100)
                #return v0

        pygame.draw.rect(screen, GREEN, button_1)
        draw_text('Réglages de la fusée', police, WHITE, screen, 20, 20)
        draw_text('Position:', police, WHITE, screen, 20, 100)
        draw_text('Vitesse:', police, WHITE,screen, 20, 200)
        draw_text('Lancement', police, WHITE, screen, HEIGHT/2 +5, WIDTH/2 +10)

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)
        for event in pygame.event.get():
            for box in input_boxes:
                box.handle_event(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True  #ça fait un bug avec le bouton et les zones de textes

        pygame.display.update()
        clock.tick(60)

def simulator():
    # module de la simulation

    sim = False
    running = True
    Rocket_x = rrr.x0.x
    Rocket_y = rrr.x0.y + 570
    miniRocketX = Rocket_x + 1000
    miniRocketY = Rocket_y + 200
    scroll = [0, 0]
    dirtX = dirt_imgX

    text_move = police.render('Type de mover:', True, (0, 0, 0))

    while running:
        # background
        screen.blit(sky_img, (0, 0))

        # afficher les images
        screen.blit(dirt_img, (0 - scroll[0], HEIGHT - scroll[1] + 410))
        screen.blit(rocket_img, (Rocket_x - scroll[0] + 450, Rocket_y - scroll[1] + 495))
        screen.blit(text_move, (0, 0))
        rocket_cp = pygame.Rect(Rocket_x + 450 - scroll[0], Rocket_y - scroll[1] + 495, rocket_imgX, rocket_imgY)
        dirt_cp = pygame.Rect((0 - scroll[0]), (HEIGHT - scroll[1] + 410), dirt_imgX, dirt_imgY)

        if Rocket_x > (dirtX - dirt_imgX/1.5):
            # loop pour créer le sol en fonction de la position de la Rocket

            dirtX =+ dirt_imgX
            dirt_cp = pygame.Rect((0 - scroll[0]) + dirtX, (HEIGHT - scroll[1] + 410), dirt_imgX, dirt_imgY)
            screen.blit(dirt_img, (0 - scroll[0] + dirtX, HEIGHT - scroll[1] + 410))
            # print("dirt:", dirtX)

        if pygame.Rect.colliderect(dirt_cp, rocket_cp):
            # vérifie la colision entre la fusée et le sol

            sim = False
            # print('x0:', rrr.x0)
            rrr.v0 = Vecteur(50, 100)
            rrr.x0 = Vecteur(0, 1)
            dirtX = dirt_imgX

        # miniMap
        miniMap = pygame.Rect(WIDTH-175, 130, 160, 20)
        pygame.draw.rect(screen, GREEN,  miniMap)
        pygame.draw.circle(screen, RED, (miniRocketX,miniRocketY), 5)
        draw_text("Distance:", mini_police, WHITE, screen, WIDTH -175, 160)
        draw_text("Vitesse:" , mini_police, WHITE, screen, WIDTH - 175, 180)
        #pygame.draw.rect(screen, PURPLE, rocket_cp)
        #pygame.draw.rect(screen, PURPLE, dirt_cp)

        # scroll
        scroll[0] += (Rocket_x - scroll[0])/5
        scroll[1] += (Rocket_y - scroll[1])/7

        if sim == True:
            MRUA.move(g, Rocket=rrr, dt=0.25)
            Rocket_x = rrr.x0.x
            Rocket_y = -rrr.x0.y + 570
            miniRocketX = Rocket_x * 0.1 + 930
            miniRocketY = Rocket_y * 0.1 + 65
            time.sleep(0.02)

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
                    sim = True
                if event.key == pygame.K_3:
                    Rocket_x, Rocket_y = pygame.mouse.get_pos()
                    Rocket_x -= 45
                    Rocket_y -= 50
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

input()

clock.tick(60)

# update la fenêtre
pygame.display.flip()
