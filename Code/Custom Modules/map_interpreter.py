import pygame
pygame.init()

winWidth, winHeight = 640, 480
win = pygame.display.set_mode((winWidth, winHeight))

WHITE = (255, 255, 255)

class map_object:

    def __init__(self, display, x, y, tilesize, map):

        self.display = display
        self.x, self.y = x, y
        self.tilesize = tilesize
        self.map = map

    def draw_map(self):

        self.xInit = self.x
        self.yInit = self.y

        self.collision = []

        for i in range(0, len(self.map)):

            for j in range(0, len(self.map[i])):

                if self.map[i][j] == 1:

                    pygame.draw.rect(self.display, WHITE, (self.x, self.y, self.tilesize, self.tilesize))
                    self.collision.append([self.x, self.y])
                    self.x += self.tilesize

                else:

                    self.x += self.tilesize

            self.y += self.tilesize
            self.x = self.xInit

        self.y = self.yInit