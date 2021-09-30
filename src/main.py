# import
from settings import *
from rocket import *
import pygame
import sys
import time

pygame.init()


# création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Rocket")


def input():
    #module des inputs pour la simulation

    running = True
    click = False
    #input_xx = InputBox(175, 100, 10, 32)
    #input_xy = InputBox(400, 100, 10, 32)
    input_vx = InputBox(160, 200, 10, 32)
    input_vy = InputBox(385, 200, 10, 32)
    input_boxes = [input_vx, input_vy]


    while running:
        screen.fill((0, 0, 0))

        # obtenir la position de la souris
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(HEIGHT/2, WIDTH/2, 295, 50)

        if button_1.collidepoint((mx, my)):
            if click:

                running = True
                click = False
                v0 = Vecteur(int(input_vx.text), int(input_vy.text))
                #x0 = Vecteur(int(input_xx.text), int(input_xy.text))
                x0 = Vecteur(1,1)
                simulator(v0, x0)

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

def simulator(v0, x0):
    # module de la simulation

    method = MRUA()
    rrr = Rocket(v0, x0)

    sim = False
    running = True
    rocket_coo_x = rrr.x0.x
    rocket_coord_y = rrr.x0.y + 570
    miniRocketX = rocket_coo_x + 1000
    miniRocketY = rocket_coord_y + 200
    scroll = [0, 0]
    text_move = police.render('Type de mover:', True, (0, 0, 0))


    while running:
        # background
        screen.blit(sky_img, (0, 0))



        # afficher les images
        screen.blit(dirt_img, (0 - scroll[0], HEIGHT - scroll[1] + 410))
        screen.blit(dirt_img, (dirt_imgX - scroll[0], HEIGHT - scroll[1] + 410))
        screen.blit(dirt_img, (dirt_imgX*2 - scroll[0], HEIGHT - scroll[1] + 410))

        screen.blit(rocket_img, (rocket_coo_x - scroll[0] + 450, rocket_coord_y - scroll[1] + 495))
        screen.blit(text_move, (0, 0))
        rocket_cp = pygame.Rect(rocket_coo_x + 450 - scroll[0], rocket_coord_y - scroll[1] + 495, rocket_imgX, rocket_imgY)
        dirt_cp = pygame.Rect((0 - scroll[0]), (HEIGHT - scroll[1] + 410), dirt_imgX*3, dirt_imgY)

        if pygame.Rect.colliderect(dirt_cp, rocket_cp):
            # vérifie la colision entre la fusée et le sol

            sim = False


        # miniMap
        miniMap = pygame.Rect(WIDTH-175, 130, 160, 20)
        pygame.draw.rect(screen, GREEN,  miniMap)
        pygame.draw.circle(screen, RED, (miniRocketX,miniRocketY), 5)
        draw_text("Distance:", mini_police, WHITE, screen, WIDTH -175, 160)
        draw_text("Vitesse:", mini_police, WHITE, screen, WIDTH - 175, 180)

        # affichage de la distance
        distance_txt = mini_police.render(str(rrr.x0.x), 1, WHITE)
        pos_dist_txt = [WIDTH - 115, 160]
        screen.blit(distance_txt, pos_dist_txt)
        # afichage de la vitesse
        speed_txt = mini_police.render(str(rrr.v0), 1, WHITE)
        pos_speed_txt = [WIDTH - 120, 180]
        screen.blit(speed_txt, pos_speed_txt)

        #pygame.draw.rect(screen, PURPLE, rocket_cp)
        #pygame.draw.rect(screen, PURPLE, dirt_cp)

        # scroll (pour faire que la tous bouge en suivant la caméra)
        scroll[0] += (rocket_coo_x - scroll[0])/5
        scroll[1] += (rocket_coord_y - scroll[1])/7



        if sim == True:
            method.move(rrr, dt=0.25)
            rocket_coo_x = rrr.x0.x
            rocket_coord_y = -rrr.x0.y + 570
            miniRocketX = rocket_coo_x * 0.1 + 930
            miniRocketY = rocket_coord_y * 0.1 + 65
            Particles((rocket_coo_x + 480 - scroll[0]), (rocket_coord_y - scroll[1] + 540), screen, RED)
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
                    rocket_coo_x, rocket_coord_y = pygame.mouse.get_pos()
                    rocket_coo_x -= 45
                    rocket_coord_y -= 50
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
