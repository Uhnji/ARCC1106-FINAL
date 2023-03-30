import pygame
import sys
import os

class Player_Object:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.x = int(x)
        self.y = int(y)
        self.color = pygame.Color("red")
        self.velX = 0
        self.velY = 0

        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.speed = 3
        
        self.dash_active = False
        self.dash_timer = 0 # counts down to 0 from dash duration (Base: 2 seconds)
        self.cooldown = 240 # 2 second cooldown duration at spawning
        self.DASH_MULTIPLIER = 2

        self.health = 100
        self.is_tired = False
        
        self.is_dodging = False

    def draw(self,win): #Draws the Player object
        pygame.draw.rect(win, self.color,self.rect)

    def update(self):
        self.velX = 0
        self.velY = 0

        # movement 
        if self.left and not self.right:
            self.velX = -self.speed

        elif self.right and not self.left:
            self.velX = self.speed

        if self.up and not self.down:
            self.velY = -self.speed

        elif self.down and not self.up:
            self.velY = self.speed

        # dash adjustment
        if self.dash_active and self.cooldown<=0:
            self.cooldown = 2430 # 20 second cooldown for dashing + 1/4 second of dashing
            self.dash_timer = 30

        if self.dash_timer>0: # Dash Velocity Modification
            self.velX *= self.DASH_MULTIPLIER
            self.velY *= self.DASH_MULTIPLIER
            self.dash_timer -=1

        if self.cooldown > 0: # Cooldown Deincrementer
            self.cooldown -= 1
            
        # penalties
        if self.is_tired: # Tired Movement Penalty
            self.velX *= .75
            self.velY *= .75

        self.x += self.velX
        self.y += self.velY

        print(f"VelocityX: {self.velX} VelocityY: {self.velY} Cooldown: {self.cooldown}")

        self.rect = pygame.Rect(self.x, self.y, 32, 32)
