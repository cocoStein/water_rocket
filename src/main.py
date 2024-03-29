# import
from settings import *
from rocket import *
import pygame
import sys
import time
import json

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1000)

# création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Rocket")

def input():
    #module des inputs pour la simulation

    running = True
    click = False

    # Boutons vitesse
    input_vx = InputBox(160, 100, 10, 32, "0")
    input_vy = InputBox(395, 100, 10, 32, "0")

    input_name = InputBox(790, 100, 10, 32, "")
    input_boxes = [input_vx, input_vy, input_name]

    # Boutons formes
    formes = []
    bouteilleBut = buttons(175, 300, bouteille, formes, "Bouteille")
    cubeBut = buttons(260, 300, cube, formes, "Cube")
    balleBut = buttons(325, 300, balle, formes, "Balle")
    coneBut = buttons(390, 300, cone, formes, "Cone")
    cylindreBut = buttons(440, 300, cylindre, formes, "Cyindre")
    sphereBut = buttons(515, 300, sphere, formes, "Sphere")
    pyramideBut = buttons(580, 300, pyramide, formes, "Pyramide")
    formesBut = [bouteilleBut, cubeBut, balleBut, coneBut, cylindreBut, sphereBut, pyramideBut]

    # Boutons forces
    forces = []
    pousseeBut = buttons(175, 400, Poussee(), forces, "Poussee")
    poidsBut = buttons(250, 400, Poids(), forces, "Poids")
    traineeBut = buttons(325, 400, Frottement(), forces, "frottement")
    archimedeBut = buttons(425, 400, Archimede(), forces, "Archimede")
    forcesBut = [poidsBut, pousseeBut, traineeBut, archimedeBut]


    # Boutons mouvements
    methode = []
    mruaBut = buttons(200, 200, MRUA(), methode, "MUA")
    pasapasBut = buttons(275, 200, PasAPas(), methode, "Pas à pas")
    methodeBut = [mruaBut, pasapasBut]

    maxX0 = []
    maxY0 = []

    while running:
        screen.fill((0, 0, 0))

        # obtenir la position de la souris
        mx, my = pygame.mouse.get_pos()

        button_lancement = pygame.Rect(HEIGHT/2 + 75, WIDTH/2, 200, 50)

        if button_lancement.collidepoint((mx, my)):
            if click:

                v0 = Vecteur(int(input_vx.text), int(input_vy.text))
                x0 = Vecteur(1, 1)
                text_name = input_name.text
                #draw_text("Ceci n'est pas une valeur acceptée pour cette simulation", police, RED, screen, 20, 300)

                click = False
                running = True

                rocket_mini_sim = Rocket(v0, x0)

                #while rocket_mini_sim.x0.y >= 0:
                #    methode[0].move(rocket_mini_sim, dt=0.2)
                #    maxX0.append(rocket_mini_sim.x0.x)
                #    maxY0.append(rocket_mini_sim.x0.y)

                #maxY0.sort()
                #x0max = maxX0[-1]
                #y0max = maxY0[-1]
                x0max, y0max = 1,1

                # lance la simulation
                simulator(v0, x0, x0max, y0max, methode, forces, formes, text_name)

        pygame.draw.rect(screen, GREEN, button_lancement)
        draw_text('Réglages de la fusée', police, WHITE, screen, 20, 20)
        draw_text('Vitesse:', police, WHITE,screen, 20, 100)
        draw_text('x', police, WHITE, screen, 365, 100)
        draw_text('y', police, WHITE, screen, 600, 100)

        draw_text('Nom:', police, WHITE, screen, 700, 100)
        draw_text('Lancement', police, WHITE, screen, HEIGHT/2 + 80, WIDTH/2 +10)
        draw_text('Méthodes:', police, WHITE, screen, 20, 200)
        draw_text('Formes:', police, WHITE, screen, 20, 300)
        draw_text('Forces:', police, WHITE, screen, 20, 400)


        for box in input_boxes:
            box.update()
            box.draw(screen)

        for i in forcesBut:
            i.draw(screen)
        for but in methodeBut:
            but.draw(screen)
        for but in formesBut:
            but.draw(screen)
        for event in pygame.event.get():
            for but in forcesBut:
                but.handle_event(event)
                click = False
            for but in methodeBut:
                but.handle_event(event)
                click = False
            for but in formesBut:
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

def simulator(v0, x0, x0max, y0max, methode, forces, formes, text_name):
    # module de la simulation

    # Variables pour la fusée
    rrr = Rocket(v0, x0, forces, forme=formes[0])
    methode = methode[0]

    # Booleans pour la simulation
    sim = False
    running = True
    max_haut = False

    # Json
    data = {}
    data['name'] = str(text_name)
    data['forme'] = str(formes)
    data['x0max'] = str(x0max)

    with open('data.json', 'a') as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True)

    # Coordonées pour la simulations
    rocket_coo_x = rrr.x0.x
    rocket_coord_y = rrr.x0.y + 570
    miniRocketX = rocket_coo_x + 1000
    miniRocketY = (rocket_coord_y + 200)

    scroll = [0, 0]
    angle_rot = 0
    max_haut_x = 0
    counter, text = 3, '3'

    if formes[0] == bouteille:
        rocket_img = rocket_img_bouteille
    elif formes[0] == balle:
        rocket_img = rocket_img_balle
    elif formes[0] == cone:
        rocket_img = rocket_img_cone
    elif formes[0] == cube:
        rocket_img = rocket_img_cube
    elif formes[0] == sphere:
        rocket_img = rocket_img_sphere
    elif formes[0] == cylindre:
        rocket_img = rocket_img_cylindre
    elif formes[0] == pyramide:
        rocket_img = rocket_img_pyramide

    while running:
        # background
        screen.blit(sky_img, (0, 0))

        # afficher les sprites
        screen.blit(dirt_img, (0 - scroll[0], HEIGHT - scroll[1] + dirt_placementY))
        screen.blit(dirt_img, (dirt_imgX - scroll[0], HEIGHT - scroll[1] + dirt_placementY))
        screen.blit(dirt_img, (dirt_imgX * 2 - scroll[0], HEIGHT - scroll[1] + dirt_placementY))
        screen.blit(Rot_center(rocket_img, angle_rot), (rocket_coo_x - scroll[0] + rocket_placementX, rocket_coord_y - scroll[1] + 495))

        # Hitbox pour le sol et la fusée
        rocket_cp = pygame.Rect(rocket_coo_x + rocket_placementX - scroll[0], rocket_coord_y - scroll[1] + 495, 64, 64)
        dirt_cp = pygame.Rect((0 - scroll[0]), (HEIGHT - scroll[1] + dirt_placementY), dirt_imgX * 3, dirt_imgY)

        if pygame.Rect.colliderect(dirt_cp, rocket_cp):
                # vérifie la colision entre la fusée et le sol

                sim = False


        # miniMap
        miniMap = pygame.Rect(WIDTH-175, 130, 160, 20)

        pygame.draw.rect(screen, GREEN,  miniMap)
        pygame.draw.circle(screen, RED, (miniRocketX, miniRocketY), 5)
        draw_text("Distance:", mini_police, WHITE, screen, WIDTH -175, 160)
        draw_text("Vitesse:", mini_police, WHITE, screen, WIDTH - 175, 180)
        draw_text("Hauteur maximale:", mini_police, WHITE, screen, WIDTH -175, 200)

        if int(rrr.x0.y) == int(y0max): # ne fonctionne pas dans tous les cas surement à cause des arondis
            max_haut = True
            max_haut_x = miniRocketX
            max_haut_y = miniRocketY
            print(miniRocketX, miniRocketY)
            print(max_haut_x, max_haut_y)

        if max_haut == True:
            pygame.draw.circle(screen, GREEN, (max_haut_x, max_haut_y), 5)
            draw_text(str(y0max), mini_police, WHITE, screen, WIDTH - 55, 200 )

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

            # Timer avant le début de la sim
            for i in pygame.event.get():
                if i.type == pygame.USEREVENT:
                    counter -= 1
                    text = str(counter) if counter > 0 else ' '
            screen.blit(mega_police.render(text, True, RED), (HEIGHT/2 + 100, WIDTH/2 - 200))

            if counter == 0:
                pygame.time.set_timer(pygame.USEREVENT, 1000000) # (User events) fait des events customs
                methode.move(rrr, 0.2)
                rocket_coo_x = rrr.x0.x
                rocket_coord_y = (-rrr.x0.y + 570)
                miniRocketX = (rocket_coo_x * 0.1 + 930)
                miniRocketY = (rocket_coord_y * 0.1 + 65)
                Particles((rocket_coo_x + rocket_placementX + 1/2*64 - scroll[0]), (rocket_coord_y - scroll[1] + 560), screen, BLUE)
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
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
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
