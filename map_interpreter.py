import pygame
pygame.init()

class TileMap:

    def __init__(self, map):

        self.tiles = []#List to store tile data.
        self.map = map#Get map data.
        self.tile_size = 16 * 4
        self.x0, self.y0 = 0, 0
        self.x, self.y = self.x0, self.y0

        self.demo_tile = pygame.image.load("Sprites/Demo_Tile.png")
        self.demo_tile = pygame.transform.scale(self.demo_tile, (self.tile_size, self.tile_size))

    def read(self):#Run through each nested list in the map data, and store a tile in tiles list when map[i] = 1.

        for i in range(len(self.map)):

            for j in range(len(self.map[i])):

                if self.map[i][j] == 1:

                    self.tiles.append([self.demo_tile, self.x, self.y])

                self.x += self.tile_size

            #Reset y and x values for rows and collums.
            self.y += self.tile_size
            self.x = self.x0

        self.y = self.y0

        return self.tiles