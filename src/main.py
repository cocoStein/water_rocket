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
    input_vx = InputBox(160, 100, 10, 32)
    input_vy = InputBox(385, 100, 10, 32)
    input_boxes = [input_vx, input_vy]
    pousseeBut = butForces(175, 300, Poussee(), "Poussee")
    poidsBut = butForces(250, 300, Poids(), "Poids")
    traineeBut = butForces(325, 300, Frottement(), "frottement")
    archimedeBut = butForces(425, 300, Archimede(), "Archimede")

    mruaBut = butMethode(200, 200, MRUA(), "MUA")
    pasapasBut = butMethode(275, 200, PasAPas(), "Pas à pas")
    #maxX0 = []
    #maxY0 = []

    methodeBut = [mruaBut, pasapasBut]
    forcesBut = [poidsBut, pousseeBut, traineeBut, archimedeBut]
    while running:
        screen.fill((0, 0, 0))

        # obtenir la position de la souris
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(HEIGHT/2, WIDTH/2, 295, 50)

        if button_1.collidepoint((mx, my)):
            if click:

                click = False
                running = True
                v0 = Vecteur(int(input_vx.text), int(input_vy.text))
                x0 = Vecteur(1, 1)


                rocket_mini_sim = Rocket(v0, x0)
                #while rocket_mini_sim.x0.y >= 0:
                #    methode.move(rocket_mini_sim, dt=0.2)
                #    maxX0.append(rocket_mini_sim.x0.x)
                #    maxY0.append(rocket_mini_sim.x0.y)

                #maxY0.sort()
                #x0max = maxX0[-1]
                #y0max = maxY0[-1]
                #print(x0max, y0max)
                x0max, y0max = 0,0
                # lance la simulation
                simulator(v0, x0, x0max, y0max, methode, forces)

        pygame.draw.rect(screen, GREEN, button_1)
        draw_text('Réglages de la fusée', police, WHITE, screen, 20, 20)
        draw_text('Vitesse:', police, WHITE,screen, 20, 100)
        draw_text('Lancement', police, WHITE, screen, HEIGHT/2 +5, WIDTH/2 +10)
        draw_text('Méthodes:', police, WHITE, screen, 20, 200)
        draw_text('Forces:', police, WHITE, screen, 20, 300)


        for box in input_boxes:
            box.update()
            box.draw(screen)

        for but in forcesBut:
            but.draw(screen)
        for but in methodeBut:
            but.draw(screen)
        for event in pygame.event.get():
            for but in forcesBut:
                but.handle_event(event)
                click = False
            for but in methodeBut:
                but.handle_event(event)
                click = False
            for box in input_boxes:
                box.handle_event(event)
                click = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def simulator(v0, x0, x0max, y0max, methode, forces):
    # module de la simulation

    rrr = Rocket(v0, x0, forces)
    methode = methode[0]
    print(methode)
    sim = False
    running = True
    max_haut = False
    rocket_coo_x = rrr.x0.x
    rocket_coord_y = rrr.x0.y + 570
    miniRocketX = rocket_coo_x + 1000
    miniRocketY = rocket_coord_y + 200
    scroll = [0, 0]
    angle_rot = 0
    max_haut_x = 0


    while running:
        # background
        screen.blit(sky_img, (0, 0))



        # afficher les images
        screen.blit(dirt_img, (0 - scroll[0], HEIGHT - scroll[1] + 410))
        screen.blit(dirt_img, (dirt_imgX - scroll[0], HEIGHT - scroll[1] + 410))
        screen.blit(dirt_img, (dirt_imgX*2 - scroll[0], HEIGHT - scroll[1] + 410))

        screen.blit(Rot_center(rocket_img, angle_rot), (rocket_coo_x - scroll[0] + 450, rocket_coord_y - scroll[1] + 495))
        rocket_cp = pygame.Rect(rocket_coo_x + 450 - scroll[0], rocket_coord_y - scroll[1] + 495, rocket_imgX, rocket_imgY)
        dirt_cp = pygame.Rect((0 - scroll[0]), (HEIGHT - scroll[1] + 410), dirt_imgX*3, dirt_imgY)

        if pygame.Rect.colliderect(dirt_cp, rocket_cp):
            # vérifie la colision entre la fusée et le sol

            sim = False


        # miniMap
        miniMap = pygame.Rect(WIDTH-175, 130, 160, 20)
        pygame.draw.rect(screen, GREEN,  miniMap)
        pygame.draw.circle(screen, RED, (miniRocketX, miniRocketY), 5)
        draw_text("Distance:", mini_police, WHITE, screen, WIDTH -175, 160)
        draw_text("Vitesse:", mini_police, WHITE, screen, WIDTH - 175, 180)

        if int(rrr.x0.y) == int(y0max): # ne fonctionne pas dans tous les cas surement à cause des arpndi
            max_haut = True
            max_haut_x = miniRocketX
            max_haut_y = miniRocketY
            print(miniRocketX, miniRocketY)
            print(max_haut_x, max_haut_y)

        if max_haut == True:
            pygame.draw.circle(screen, GREEN, (max_haut_x, max_haut_y), 5)
            #print("max")

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
            methode.move(rrr, 0.2)
            rocket_coo_x = rrr.x0.x
            rocket_coord_y = -rrr.x0.y + 570
            miniRocketX = rocket_coo_x * 0.1 + 930
            miniRocketY = rocket_coord_y * 0.1 + 65
            Particles((rocket_coo_x + 480 - scroll[0]), (rocket_coord_y - scroll[1] + 540), screen, RED)
            angle_rot += 5
            time.sleep(0.02)

        # check pour les event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
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
