import pygame
import math
import random

class Enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velX = 0
        self.velY = 0
        self.init_speed = 2
        self.speed = 1
        self.accel = .5
        self.friction = .5
        self.dir = 1

        self.dir_timer = 0
        self.dir_timer_max = 120

        self.up = True
        self.down = False
        self.right = False
        self.left = False

    def update(self):
        if self.dir_timer <= 0:
            self.dir_timer = self.dir_timer_max
        else:
            self.dir_timer -= 1

        if self.dir == 1:
            self.up = True

        else:
            self.up = False

        if self.dir == 2:
            self.down = True

        else:
            self.down = False

        if self.dir == 3:
            self.right = True

        else:
            self.right = False

        if self.dir == 4:
            self.left = True

        else:
            self.left = False

        if self.up and self.velY >= -self.speed:
            self.velY -= self.accel

        elif self.down and self.velY <= self.speed:
            self.velY += self.accel

        else:
            if self.velY > 0:
                self.velY -= self.friction

                if self.velY <= self.friction:
                    self.velY = 0

            if self.velY < 0:
                self.velY += self.friction

                if self.velY >= self.friction:
                    self.velY = 0

        if self.left and self.velX >= -self.speed:
            self.velX -= self.accel

        elif self.right and self.velX <= self.speed:
            self.velX += self.accel

        else:
            if self.velX > 0:
                self.velX -= self.friction

                if self.velX <= self.friction:
                    self.velX = 0

            if self.velX < 0:
                self.velX += self.friction

                if self.velX >= self.friction:
                    self.velX = 0

        self.y += self.velY
        self.x += self.velX

        self.rect = pygame.Rect(self.x, self.y, 32, 32)

    def check_collisions(self, tiles, player_rect):#Checks if player rect and tile rect are colliding, player speed cancels when they do.
        self.player_rect = player_rect
        for i in range(len(tiles)):
            self.tile_rect = pygame.Rect(tiles[i][1], tiles[i][2], 64,64)
            self.colliding = pygame.Rect.colliderect(self.rect, self.tile_rect)
            self.accuracy = 11 #Multiples of 10 make the collisions weird. Play around with this value if collisions are weird anyways.

            if self.colliding:
                if abs(self.tile_rect.top - self.rect.bottom) < self.accuracy and self.velY > 0 or abs(self.tile_rect.bottom - self.rect.top) < self.accuracy and self.velY < 0:
                    self.y -= self.velY * 1.1
                    if abs(self.x - self.player_rect.x) <= abs(self.y - self.player_rect.y):
                        if player_rect.x > self.x:
                            self.dir = 3
                        else:
                            self.dir = 4

                    else:
                        if player_rect.y > self.y:
                            self.dir = 2
                        else:
                            self.dir = 1

                if abs(self.tile_rect.right - self.rect.left) < self.accuracy and self.velX < 0 or abs(self.tile_rect.left - self.rect.right) < self.accuracy and self.velX > 0:
                    self.x -= self.velX * 1.1
                    if abs(self.x - self.player_rect.x) <= abs(self.y - self.player_rect.y):
                        if player_rect.x > self.x:
                            self.dir = 3
                        else:
                            self.dir = 4

                    else:
                        if player_rect.y > self.y:
                            self.dir = 2
                        else:
                            self.dir = 1

            if self.dir_timer <= 0:
                if abs(self.x - self.player_rect.x) >= abs(self.y - self.player_rect.y):
                    if player_rect.x > self.x:
                        self.dir = 3
                    else:
                        self.dir = 4

                else:
                    if player_rect.y > self.y:
                        self.dir = 2
                    else:
                        self.dir = 1
    def render(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 32, 32))