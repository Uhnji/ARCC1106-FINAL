import pygame
import sys
import map_interpreter
import map_data
import os

from player import Player_Object
from map_interpreter import *
from map_data import *

winWidth = 640
winHeight = 480

def y_sort(render_layer):
    for i in range(len(render_layer)):
        for j in range(i, len(render_layer)):
            if render_layer[i][2] >= render_layer[j][2]:
                cache = render_layer[i]
                render_layer[i] = render_layer[j]
                render_layer[j] = cache

def initialize_pygame(): 
    """Sets starting parameters, WIDTH, HEIGHT, and TITILE parameters and instantilizes PyGame"""
    TITLE = "CSCI_FINAL V.0.3 - PRESENTATION EDITION"
    win = pygame.display.set_mode((winWidth, winHeight))
    pygame.display.set_caption(TITLE)
    pygame.init()

    clock = pygame.time.Clock()
    return win,clock

if __name__ == '__main__':
    render_layer1 = []
    render_layer2 = []
    win, clock = initialize_pygame()
    player = Player_Object(320, 240)
    dungeon = TileMap(map1)

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

        tiles = dungeon.read()

        player.update()
        player.check_collisions(tiles)



        timer_frame = None 

        if 450 < player.cooldown <= 600: # Mainline check to append the Player Cooldown icon to the screen following the Dash (Accessibility Function)
            timer_frame = (player.timer_sprites[1],player.x,player.y-45)

        elif 300 < player.cooldown <= 450:
            timer_frame = (player.timer_sprites[2],player.x,player.y-45)

        elif 150 < player.cooldown <= 300:
            timer_frame = (player.timer_sprites[3],player.x,player.y-45)

        elif 50 < player.cooldown <= 150:
            timer_frame = (player.timer_sprites[4],player.x,player.y-45)

        elif 0 < player.cooldown <= 50: 
            timer_frame = (player.timer_sprites[5],player.x,player.y-45)


        if timer_frame != None:
            render_layer2.append(timer_frame)



        #Camera movement section start.
        camera_x = (player.x - winWidth/2 + 16)/20
        camera_y = (player.y - winHeight/2 + 16)/20

        dungeon.x0 -= camera_x
        dungeon.y0 -= camera_y

        player.x -= camera_x
        player.y -= camera_y
        #Camera movement section end.

        #Add to render layer 1.
        render_layer1.append(player.draw(win))

        render_layer1 += tiles
        tiles.clear()
        #End to render layer 1.

        y_sort(render_layer1)

        #Render loop.
        win.fill((12,24,36))

        #Render render layer 1.
        for i in range(len(render_layer1)): # Walls, Players, Enemies
            win.blit(render_layer1[i][0], (render_layer1[i][1], render_layer1[i][2]))

        for i in range(len(render_layer2)): # Rendered HUD icons, Projectiles, Items
            win.blit(render_layer2[i][0], (render_layer2[i][1], render_layer2[i][2]))

        pygame.display.flip()

        render_layer1.clear()
        render_layer2.clear()

        clock.tick(120)
