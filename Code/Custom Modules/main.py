import pygame
import sys
import os
from player import Player_Object

def initialize_pygame(): 
    """Sets starting parameters, WIDTH, HEIGHT, and TITILE parameters and instantilizes PyGame"""
    TITLE = "CSCI_FINAL V.0.1 - MOVEMENT TEST"
   
    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption(TITLE)
    pygame.init()

    clock = pygame.time.Clock()
    return win,clock


if __name__ == '__main__':
    win, clock = initialize_pygame()
    
    player = Player_Object(0,0)

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


        win.fill((12,24,36))
        player.draw(win)

        player.update()
        pygame.display.flip()
        clock.tick(120)


