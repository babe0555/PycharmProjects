import sys

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400))

pos_x = 150
pos_y = 150

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 0))

    # 画正方形
    color = 255, 255, 0
    pos = pos_x, pos_y, 100, 100
    width = 0
    pygame.draw.rect(screen, color, pos, width)

    pygame.display.update()
