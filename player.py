import pygame




class Player_Object:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 64, 64)
        self.x = int(x)
        self.y = int(y)
        self.velX = 0
        self.velY = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.init_speed = 3
        self.speed = 0
        self.dash_active = False
        self.dash_timer = 0 # counts down to 0 from dash duration (Base: 2 seconds)
        self.cooldown = 240 # 2 second cooldown duration at spawning
        self.DASH_MULTIPLIER = 2
        self.health = 100
        self.is_tired = False
        self.is_dodging = False

        self.sprite_dir = "UP"
        self.sprite = 0 #Initialize sprite return value.
        self.frame = 0  # Current sprite frame.

        #Load sprite frames.
        self.frames = {

            0 : pygame.image.load('Sprites/Knight Frames/Knight1.png'),#Downidle

            1 : pygame.image.load('Sprites/Knight Frames/Knight2.png'),#Downrunning1

            2 : pygame.image.load('Sprites/Knight Frames/Knight3.png'),#Downrunning2

            3 : pygame.image.load('Sprites/Knight Frames/Knight5.png'),#Downrunning3

            4 : pygame.image.load('Sprites/Knight Frames/Knight6.png'),#Downrunning4

            5 : pygame.image.load('Sprites/Knight Frames/Knight7.png'),#Rightidle

            6 : pygame.image.load('Sprites/Knight Frames/Knight8.png'),#Rightrunning1

            7 : pygame.image.load('Sprites/Knight Frames/Knight9.png'),#Rightrunning2

            8 : pygame.image.load('Sprites/Knight Frames/Knight11.png'),#Rightrunning3

            9 : pygame.image.load('Sprites/Knight Frames/Knight12.png'),#Rightrunning4

            10: pygame.image.load('Sprites/Knight Frames/Knight19.png'),#Leftidle

            11: pygame.image.load('Sprites/Knight Frames/Knight20.png'),#Leftrunning1

            12: pygame.image.load('Sprites/Knight Frames/Knight21.png'),#Leftrunning2

            13: pygame.image.load('Sprites/Knight Frames/Knight23.png'),#Leftrunning3

            14: pygame.image.load('Sprites/Knight Frames/Knight24.png'),#Leftrunning4

            15: pygame.image.load('Sprites/Knight Frames/Knight13.png'),#Upidle

            16: pygame.image.load('Sprites/Knight Frames/Knight14.png'),#Uprunning1

            17: pygame.image.load('Sprites/Knight Frames/Knight15.png'),#Uprunning2

            18: pygame.image.load('Sprites/Knight Frames/Knight17.png'),#Uprunning3

            19: pygame.image.load('Sprites/Knight Frames/Knight18.png') #Uprunning4
        }

        #Load sprite animation.
        self.anim = {

            0 : [self.frames[0]], #Idle Down Animation

            1 : [self.frames[1], self.frames[2], self.frames[0], self.frames[3], self.frames[4], self.frames[0]], #Running Down Animation

            2: [self.frames[5]], #Idle Right Animation

            3: [self.frames[6], self.frames[7], self.frames[5], self.frames[8], self.frames[9], self.frames[5]], #Running Right Animation

            4: [self.frames[10]], #Idle Left Animation

            5: [self.frames[11], self.frames[12], self.frames[10], self.frames[13], self.frames[14], self.frames[10]], #Running Left Animation

            6: [self.frames[15]], #Idle Up Animation

            7: [self.frames[16], self.frames[17], self.frames[15], self.frames[18], self.frames[19], self.frames[15]], #Running Up Animation
        }

        self.timer_sprites = {
            1 : pygame.image.load('Sprites/Sprint Indicator/Progress0.png'), #Empty

            2 : pygame.image.load('Sprites/Sprint Indicator/Progress1.png'), #25%

            3 : pygame.image.load('Sprites/Sprint Indicator/Progress2.png'), #50%

            4 : pygame.image.load('Sprites/Sprint Indicator/Progress3.png'), #75%

            5 : pygame.image.load('Sprites/Sprint Indicator/Progress4.png')  #100%
        }

    def if_collision_adjust(self):
        if self.colliding:
                if abs(self.tile_rect.top - self.rect.bottom) < self.accuracy and self.velY > 0 or abs(self.tile_rect.bottom - self.rect.top) < self.accuracy and self.velY < 0:
                    self.y -= self.velY * 1.1

                if abs(self.tile_rect.right - self.rect.left) < self.accuracy and self.velX < 0 or abs(self.tile_rect.left - self.rect.right) < self.accuracy and self.velX > 0:
                    self.x -= self.velX * 1.1




    def draw(self,win): #Draws the Player object
        #Handle animations.
        if self.sprite_dir == "UP":
            if self.velX != 0 or self.velY != 0:
                self.current_anim = 7
            else:
                self.current_anim = 6

        if self.sprite_dir == "DOWN":
            if self.velX != 0 or self.velY != 0:
                self.current_anim = 1
            else:
                self.current_anim = 0

        if self.sprite_dir == "RIGHT":
            if self.velX != 0 or self.velY != 0:
                self.current_anim = 3
            else:
                self.current_anim = 2

        if self.sprite_dir == "LEFT":
            if self.velX != 0 or self.velY != 0:
                self.current_anim = 5
            else:
                self.current_anim = 4

        #Loop through frames on sync with main game loop.
        if self.frame <= len(self.anim[self.current_anim]):
            self.sprite = [pygame.transform.scale(self.anim[self.current_anim][int(self.frame)], (96, 96)), self.x - 32, self.y - 40]#Set sprite based on frame.
            self.frame += 1/9#Go to next frame in accordance with animation speed.
        else:
            self.frame = 0#Loop when done with the animation.

        return self.sprite

    def check_collisions(self, tiles):#Checks if player rect and tile rect are colliding, player speed cancels when they do.
        for i in range(len(tiles)):
            if tiles[i][3] == 1:
                self.tile_rect = pygame.Rect(tiles[i][1], tiles[i][2], 64,64)
                self.colliding = pygame.Rect.colliderect(self.rect, self.tile_rect)
                self.accuracy = 11 #Multiples of 10 make the collisions weird. Play around with this value if collisions are weird anyways.
            else:
                continue

            self.if_collision_adjust()
                    
    def update(self):
        self.velX = 0
        self.velY = 0
        # movement 
        if self.left and not self.right:
            self.velX = -self.speed
            self.sprite_dir = "LEFT"

        elif self.right and not self.left:
            self.velX = self.speed
            self.sprite_dir = "RIGHT"

        if self.up and not self.down:
            self.velY = -self.speed
            self.sprite_dir = "UP"

        elif self.down and not self.up:
            self.velY = self.speed
            self.sprite_dir = "DOWN"

        # dash adjustment
        if self.dash_active and self.cooldown<=0:
            self.cooldown = 630 # 20 second cooldown for dashing + 1/4 second of dashing
            self.dash_timer = 30

        if self.dash_timer>0: # Dash Velocity Modification
            self.velX *= self.DASH_MULTIPLIER
            self.velY *= self.DASH_MULTIPLIER
            self.dash_timer -= 1

        if self.cooldown > 0: # Cooldown Deincrementer
            self.cooldown -= 1
            
        # penalties
        if self.is_tired: # Tired Movement Penalty
            self.velX *= .75
            self.velY *= .75

        if self.velX != 0 and self.velY != 0:
            self.speed = self.init_speed * .7
        else:
            self.speed = self.init_speed

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(self.x - 4, self.y, 40, 30)
