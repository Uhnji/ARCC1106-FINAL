import pygame
pygame.init()

class TileMap:

    def __init__(self, map):

        self.tiles = []
        self.map = map
        self.tile_size = 16 * 4
        self.x0, self.y0 = 0, 0
        self.x, self.y = self.x0, self.y0

        self.demo_tile = pygame.image.load("Sprites/Demo_Tile.png")
        self.demo_tile = pygame.transform.scale(self.demo_tile, (self.tile_size, self.tile_size))

    def read(self):

        for i in range(len(self.map)):

            for j in range(len(self.map[i])):

                if self.map[i][j] == 1:

                    self.tiles.append([self.x, self.y, self.demo_tile])

                self.x += self.tile_size

            self.y += self.tile_size
            self.x = self.x0

        self.y = self.y0

        return self.tiles

    def check_collisions(self, px, py):

        self.px = px
        self.py = py

        for i in range(len(self.tiles)):

            if self.px > self.tiles[i][0] and self.px < self.tiles[i][0] + self.tile_size or self.px + 32 > self.tiles[i][0] and self.px + 32 < self.tiles[i][0] + self.tile_size :

                if self.py > self.tiles[i][1] and self.py < self.tiles[i][1] + self.tile_size or self.py + 32 > self.tiles[i][1] and self.py + 32 < self.tiles[i][1] + self.tile_size:

                    return "collision"