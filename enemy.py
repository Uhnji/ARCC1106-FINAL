import pygame
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

        self.move_timer = 0
        self.move_timer_max = 60

        self.up = True
        self.down = False
        self.right = False
        self.left = False

        self.frame = 0

        self.frames = {

            0: pygame.image.load('Sprites/Enemy_Frames/Enemy1.png'),  # Downrunning

            1: pygame.image.load('Sprites/Enemy_Frames/Enemy2.png'),  # Downrunning

            2: pygame.image.load('Sprites/Enemy_Frames/Enemy3.png'),  # Downrunning

            3: pygame.image.load('Sprites/Enemy_Frames/Enemy5.png'),  # Rightrunning

            4: pygame.image.load('Sprites/Enemy_Frames/Enemy6.png'),  # Rightrunning

            5: pygame.image.load('Sprites/Enemy_Frames/Enemy8.png'),  # Rightrunning

            6: pygame.image.load('Sprites/Enemy_Frames/Enemy9.png'),  # Leftrunning

            7: pygame.image.load('Sprites/Enemy_Frames/Enemy10.png'),  # Leftrunning

            8: pygame.image.load('Sprites/Enemy_Frames/Enemy12.png'),  # Leftrunning

            9: pygame.image.load('Sprites/Enemy_Frames/Enemy13.png'),  # Uprunning

            10: pygame.image.load('Sprites/Enemy_Frames/Enemy14.png'),  # Uprunning

            11: pygame.image.load('Sprites/Enemy_Frames/Enemy15.png'),  # Uprunning
        }

        self.anim = {
            0 : [self.frames[0], self.frames[1], self.frames[2], self.frames[1]], # Down

            1: [self.frames[3], self.frames[4], self.frames[3], self.frames[5]], # Right

            2: [self.frames[6], self.frames[7], self.frames[6], self.frames[8]], # Left

            3: [self.frames[9], self.frames[10], self.frames[11], self.frames[10]] # Up
        }

    def update(self, px, py):

        if self.move_timer <= 0:
            if abs(px - self.x) > abs(py - self.y):
                if self.x > px:
                    self.dir = 4
                else:
                    self.dir = 3
            else:
                if self.y > py:
                    self.dir = 1
                else:
                    self.dir = 2
            self.move_timer = self.move_timer_max
        else:
            self.move_timer -= 1


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

        if self.up and self.velY >= -self.speed and self.y >= -32 and self.y <= 480:
            self.velY -= self.accel

        elif self.down and self.velY <= self.speed and self.y >= -32 and self.y <= 480:
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

        if self.left and self.velX >= -self.speed and self.x >= -32 and self.x <= 640:
            self.velX -= self.accel

        elif self.right and self.velX <= self.speed and self.x >= -32 and self.x <= 640:
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

    def check_collisions(self, tiles):#Checks if player rect and tile rect are colliding, player speed cancels when they do.
        for i in range(len(tiles)):
            self.tile_rect = pygame.Rect(tiles[i][1], tiles[i][2], 64,64)
            self.colliding = pygame.Rect.colliderect(self.rect, self.tile_rect)
            self.accuracy = 11 #Multiples of 10 make the collisions weird. Play around with this value if collisions are weird anyways.

            if self.colliding:
                if abs(self.tile_rect.top - self.rect.bottom) < self.accuracy and self.velY > 0 or abs(self.tile_rect.bottom - self.rect.top) < self.accuracy and self.velY < 0:
                    self.y -= self.velY * 1.1
                    self.dir = random.randint(1, 4)

                if abs(self.tile_rect.right - self.rect.left) < self.accuracy and self.velX < 0 or abs(self.tile_rect.left - self.rect.right) < self.accuracy and self.velX > 0:
                    self.x -= self.velX * 1.1
                    self.dir = random.randint(1, 4)

    def render(self, window):
        if self.dir == 1:
            self.current_anim = 3
        if self.dir == 2:
            self.current_anim = 0

        if self.dir == 3:
            self.current_anim = 1

        if self.dir == 4:
            self.current_anim = 2

        #Loop through frames on sync with main game loop.
        if self.frame <= len(self.anim[self.current_anim]):
            self.sprite = [pygame.transform.scale(self.anim[self.current_anim][int(self.frame)], (96, 96)), self.x - 32, self.y - 40]#Set sprite based on frame.
            self.frame += 1/24#Go to next frame in accordance with animation speed.
        else:
            self.frame = 0#Loop when done with the animation.

        return self.sprite