import pygame
import random
from forme import *

pygame.font.init()

# Variables
WIDTH = 1080
HEIGHT = 720
running = True
click = False
clock = pygame.time.Clock()


# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

# Information fusée C pour le coefficient et S la surface sur la base de notre fusée à eau
cubeC = 0.8
cubeS = 0.10**2
cubeVolume = (0.10**2) * 0.38 #La même hauteur que la bouteille
cube = Forme(cubeC,cubeS,cubeVolume)

balleC = 0.3
balleS = 3.1415 * 0.05**2
balleVolume = 3.1415 * (0.05**2) * 0.30 + 1/3 * 3.1415 * 0.08 * 0.05**2
balle = Forme(balleC,balleS,balleVolume)

coneC = 0.5
coneS = 3.1415 * 0.05**2
coneVolume = 3.1415 * 0.38 * 0.05**2
cone = Forme(coneC,coneS,coneVolume)

cylindreC = 0.85
cylindreS = 3.1415 * 0.05**2
cylindreVolume = 3.1415 * (0.05**2) * 0.38
cylindre = Forme(cylindreC,cylindreS,cylindreVolume)

sphereC = 0.47
sphereS = 3.1415 * 0.05**2
sphereVolume = 4/3 * 3.1415 * 0.05**3
sphere = Forme(sphereC,sphereS,sphereVolume)

pyramideC = 1.55
pyramideS = 0.10**2
pyramideVolume = 1/3 * (0.10**2) * 0.38
pyramide = Forme(pyramideC,pyramideS,pyramideVolume)

bouteilleC = 0.52
bouteilleS =3.1415 * 0.05**2
bouteilleVolume = 0.002
bouteille = Forme(bouteilleC,bouteilleS,bouteilleVolume)

# charcher les polices
police = pygame.font.Font(None, 50)
police_subtitle = pygame.font.Font(None, 25)
mini_police = pygame.font.Font(None, 20)
mega_police = pygame.font.Font(None, 150)
FONT = pygame.font.Font(None, 32)


# charcher les images
rocket_img = pygame.image.load('img/rocket_bouteille.png')
rocket_img_bouteille = pygame.image.load('img/rocket_bouteille.png')
rocket_img_balle = pygame.image.load('img/rocket_balle.png')
rocket_img_cone = pygame.image.load('img/rocket_cone.png')
rocket_img_cube = pygame.image.load('img/rocket_cube.png')
rocket_img_sphere = pygame.image.load('img/rocket_sphere.png')
rocket_img_cylindre = pygame.image.load('img/rocket_cylindre.png')
rocket_img_pyramide = pygame.image.load('img/rocket_pyramide.png')

# Tranformations des images
rocket_img_bouteille = pygame.transform.scale(rocket_img_bouteille, (64, 64))
rocket_img_balle = pygame.transform.scale(rocket_img_balle, (64, 64))
rocket_img_cone = pygame.transform.scale(rocket_img_cone, (64, 64))
rocket_img_cube = pygame.transform.scale(rocket_img_cube, (64, 64))
rocket_img_sphere = pygame.transform.scale(rocket_img_sphere, (64, 64))
rocket_img_cylindre = pygame.transform.scale(rocket_img_cylindre, (64, 64))
rocket_img_pyramide = pygame.transform.scale(rocket_img_pyramide, (64, 64))

sky_img = pygame.image.load('img/SKY.png')
dirt_img = pygame.image.load('img/dirt.png')

rocket_imgX, rocket_imgY = rocket_img.get_size()
dirt_imgX, dirt_imgY = dirt_img.get_size()

# Variables pour le placement des images
dirt_placementY = 410
rocket_placementX = 450


def draw_text(text, font, color, surface, x, y):
    # modules pour afficher du texte

    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


class InputBox:
    # Inputbox de SKRX trouver sur GitHub
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

particles = []
def Particles(x, y, surface, color):
    # classe particules

    particles.append([[x, y], [random.randint(0, 20) / 10 - 1.5, + 4], random.randint(4, 6)])
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        pygame.draw.circle(surface, color, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)


class buttons():
    def __init__(self, x, y, nomMethode, list, text=''):
        self.rect = pygame.Rect(x, y , 30, 30)
        self.nomMethode = nomMethode
        self.color = WHITE
        self.text = text
        self.list = list
        self.active = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the box rect.
            if self.rect.collidepoint(event.pos) and self.active == 0:
                # Toggle the active variable.
                self.color = GREEN
                self.active = 1
                self.list.append(self.nomMethode)

            elif self.rect.collidepoint(event.pos) and self.active == 1:
                self.color = WHITE
                self.list.remove(self.nomMethode)
                self.active = 0


    def draw(self, screen):
        # Blit the text.
        draw_text(self.text, police_subtitle, WHITE, screen, self.rect.x - 10, self.rect.y + 40)
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect)

def Rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
