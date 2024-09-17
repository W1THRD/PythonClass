
import pygame

pygame.init()

class Rect:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    def draw(self, Surface):
        pygame.draw.rect(Surface, self.color, self.rect)

class Plot:
    def __init__(self, leftX, topY, width, height, unitWidth, unitHeight, color=(0,0,0)):
        self.leftX = leftX
        self.topY = topY
        self.width = width
        self.unitWidth = unitWidth
        self.height = height
        self.unitHeight = unitHeight
        self.matrix = []
        for y in range(height):
            self.matrix.append([])
            for x in range(width):
                self.matrix[y].append(color)
    def setUnit(self, position, color):
        x, y = position
        original = self.matrix[y][x]
        try:
            self.matrix[y][x] = color
        except IndexError:
            self.matrix[y][x] = original
    def getUnit(self, position):
        x, y = position
        return(self.matrix[y][x])
    def draw(self, Surface):
        rect = pygame.Rect(0, 0, self.unitWidth, self.unitHeight)
        for y in range(len(self.matrix)):
            rect.y = self.unitHeight * y
            for x in range(len(self.matrix[y])):
                color = self.matrix[y][x]
                rect.x = self.unitWidth * x 
                pygame.draw.rect(Surface, color, rect)