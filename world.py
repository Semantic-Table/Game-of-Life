import numpy
import random
import pygame


class World:
    def __init__(self, size, life, overpop, solitude, screen):
        self.screen = screen
        self.size = size
        self.life = life
        self.overpop = overpop
        self.solitude = solitude
        self.world = numpy.zeros((self.size, self.size), int)
        self.populateWorld()

    def displayWorld(self):
        pass

    def checkCell(self):
        newmap = numpy.zeros((self.size, self.size), int)
        for rowindex, row in enumerate(self.world):
            for colindex, col in enumerate(row):
                neighbors = 0
                for i in range(3):
                    for j in range(3):
                        # print(str(rowindex + i - 1) + ' row ' + str(colindex + j - 1) + ' col')
                        if rowindex + i - 1 >= 0 and colindex + j - 1 >= 0 and rowindex + i - 1 < self.size and colindex + j - 1 < self.size:
                            # print('[' + str(rowindex + i - 1) + ']' + '[' + str(colindex + j - 1) + ']')
                            try:
                                # print(self.world[rowindex + i - 1][colindex + j - 1])
                                # print('hello')
                                if self.world[rowindex + i - 1][colindex + j - 1] == 1:
                                    neighbors += 1
                            except:
                                pass
                # print(neighbors)
                if col == 0 and neighbors >= self.life:
                    newmap[rowindex][colindex] = 1
                if col == 1 and neighbors-1 < self.overpop and neighbors-1 > self.solitude:
                    newmap[rowindex][colindex] = 1
        self.world = newmap

    def populateWorld(self):
        for rowindex, row in enumerate(self.world):
            for colindex, col in enumerate(row):
                if random.random() > 0.93:
                    self.world[rowindex][colindex] = 1

    def displayWorld(self, size):
        width = size[0] / self.size
        height = size[1] / self.size
        for rowindex, row in enumerate(self.world):
            for colindex, col in enumerate(row):
                if col == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), [colindex*width,rowindex*height,width,height])
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), [colindex*width,rowindex*height,width,height])



