import pygame

#Variables
WIDTH = 1080
HEIGHT = 720
running = True
click = False
clock = pygame.time.Clock()

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0,0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)

#charcher les images
rocket_img = pygame.image.load('/Users/corentinsteinhauser/PycharmProjects/water_rocket/water_rocket/src/img/rocket.png')
sky_img = pygame.image.load('/Users/corentinsteinhauser/PycharmProjects/water_rocket/water_rocket/src/img/SKY.png')
dirt_img = pygame.image.load('/Users/corentinsteinhauser/PycharmProjects/water_rocket/water_rocket/src/img/dirt.png')

rocket_imgX, rocket_imgY = rocket_img.get_size()
dirt_imgX, dirt_imgY = dirt_img.get_size()


def draw_text(text, font, color, surface, x, y):
    #modules pour afficher du texte

    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)