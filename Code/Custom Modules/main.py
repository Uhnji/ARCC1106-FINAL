import pygame
import sys
import map_interpreter
import map_data
import os

from player import Player_Object
from map_interpreter import *
from map_data import *

def initialize_pygame(): 
    """Sets starting parameters, WIDTH, HEIGHT, and TITILE parameters and instantilizes PyGame"""
    TITLE = "CSCI_FINAL V.0.1 - MOVEMENT TEST"

    winWidth = 640
    winHeight = 480
    win = pygame.display.set_mode((winWidth, winHeight))
    pygame.display.set_caption(TITLE)
    pygame.init()

    clock = pygame.time.Clock()
    return win,clock


if __name__ == '__main__':

    win, clock = initialize_pygame()
    player = Player_Object(winWidth/2,winHeight/2)
    dungeon = map_object(win, 0, 0, 64, map1)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player.left = True
            else:
                player.left = False

            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player.right = True
            else:
                player.right = False

            if keys[pygame.K_w] or keys[pygame.K_UP]:
                player.up = True
            else:
                player.up = False

            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                player.down = True
            else:
                player.down = False

            if keys[pygame.K_SPACE] or keys[pygame.K_RCTRL]:
                player.dash_active = True
            else:
                player.dash_active = False

                
        #Move camera based on player movement. (Temporary solution)
        
        if player.x > 340:

            player.x -= player.velX

            dungeon.x -= player.velX

        if player.x < 300 - 64:

            player.x -= player.velX

            dungeon.x -= player.velX

        if player.y > 280:

            player.y -= player.velY

            dungeon.y -= player.velY

        if player.y < 200:

            player.y -= player.velY

            dungeon.y -= player.velY

        win.fill((12,24,36))

        player.draw(win)

        dungeon.draw_map()

        player.update()
        pygame.display.flip()
        clock.tick(120)

