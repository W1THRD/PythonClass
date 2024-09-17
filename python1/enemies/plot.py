# DO NOT RUN THIS FILE!
# This is just a library for the game
# To play the game, go to tile_game.py

import pygame, levels, math, random

pygame.init()

# coin class!
class Coin:
    # spawn coin at random position
    def __init__(self):
        self.x = random.randint(80, 420)
        self.y = random.randint(80, 420)
        self.rect = ColorRect(self.x - 10, self.y - 10, 20, 20, (255, 255, 0))
    def draw(self, Surface):
        self.rect.drawEllipse(Surface)

# moving ellipse enemy
class BadEllipse:
    def __init__(self, pos, mult):
        # define position data
        self.x, self.y = pos
        self.xmult, self.ymult = mult
        if self.xmult == 0 and self.ymult == 0:
            if random.randint(1, 2) == 1:
                self.xmult = random.choice([-1, 1])
            else:
                self.ymult = random.choice([-1, 1])
        
        # define offsets and rect
        self.offset_x = 0
        self.offset_y = 0
        self.rect = pygame.Rect(self.x - 20, self.y - 15, 40, 30)
    def draw(self, Surface, frame):
        # move x
        self.offset_x = math.sin(frame/8) * 160 * self.xmult 
        self.rect.x = int((self.x + self.offset_x) - 15)
        
        # move y
        self.offset_y = math.sin(frame/8) * 160 * self.ymult 
        self.rect.y = int((self.y + self.offset_y) - 15)
        
        # draw
        pygame.draw.ellipse(Surface, (255, 0, 0), self.rect)

# moving rect enemy
class BadRect:
    def __init__(self, pos, mult):
        # define position data
        self.x, self.y = pos
        self.xmult, self.ymult = mult
        if self.xmult == 0 and self.ymult == 0:
            if random.randint(1, 2) == 1:
                self.xmult = random.choice([-1, 1])
            else:
                self.ymult = random.choice([-1, 1])
        
        # define offsets and rect
        self.offset_x = 0
        self.offset_y = 0
        self.rect = pygame.Rect(self.x - 5, self.y - 15, 10, 30)
    def draw(self, Surface, frame):
        # move x
        self.offset_x = math.sin(frame/8) * 160 * self.xmult 
        self.rect.x = int((self.x + self.offset_x) - 15)
        
        # move y
        self.offset_y = math.sin(frame/8) * 160 * self.ymult 
        self.rect.y = int((self.y + self.offset_y) - 15)
        
        # draw
        pygame.draw.rect(Surface, (255, 0, 0), self.rect)

# player class that handles player physics
class Player:
    # initiate player object
    def __init__(self, pos, radius, color, max_velocity, friction):
        # define vars from parameters
        self.x, self.y = pos
        self.color = color
        
        # define rect
        self.rect = pygame.Rect(self.x - radius, self.y - radius, radius * 2, radius * 2)
        
        # define extra physics data
        self.xv = 0
        self.yv = 0
        self.max_velocity = max_velocity
        self.friction = friction
        
        # define mouth data
        self.mouth_offset = 0
        self.mouth_move = 1
        self.mouth_points = []
        
    # apply limit to numbers
    def limit(self, n, minimum, maximum):
        if n < minimum:
            return(minimum)
        elif n > maximum:
            return(maximum)
        else:
            return(n)
        
    # applies friction
    def applyFriction(self, v):
        if (v > -0.1) and (v < 0.1):
            return(0)
        elif v < 0:
            return(self.limit(v + self.friction, self.max_velocity * -1, 0))
        elif v > 0:
            return(self.limit(v - self.friction, 0, self.max_velocity))
    
    # updates physics/position data
    def update(self, collision):
        # apply x velocity
        if not self.xv == 0:
            self.x += self.xv
            self.rect.x = int(self.x - (self.rect.width/2))
            self.xv = self.applyFriction(self.xv)
            
            # x-collison
            col = levels.collideLevel(self.rect)
            while col != 0:
                if col == 1:
                    self.x += 1
                elif col == 2:
                    self.x -= 1
                self.rect.x = int(self.x - (self.rect.width/2))
                col = levels.collideLevel(self.rect)
        
        # apply y velocity
        if not self.yv == 0:
            self.y += self.yv
            self.rect.y = int(self.y - (self.rect.height/2))
            self.yv = self.applyFriction(self.yv)
            
            # y-collision
            col = levels.collideLevel(self.rect)
            while col != 0:
                if col == 3:
                    self.y += 1
                elif col == 4:
                    self.y -= 1
                self.rect.y = int(self.y - (self.rect.height/2))
                col = levels.collideLevel(self.rect)
                
        # update rect pos        
        self.rect.x = int(self.x - (self.rect.width/2))
        self.rect.y = int(self.y - (self.rect.height/2))
            
    # updates mouth data
    def updateMouth(self):
        self.mouth_offset += self.mouth_move
        if (self.mouth_offset >= 15) or (self.mouth_offset <= -15):
            self.mouth_offset *= -1
        self.mouth_points = []
        self.mouth_points.append((self.x, self.y))
        self.mouth_points.append((self.x + (self.rect.width/2), self.y + self.mouth_offset))
        self.mouth_points.append((self.x + (self.rect.width/2), self.y - self.mouth_offset))
        
    # draws player
    def draw(self, Surface):
        # draw ellipse from rect
        pygame.draw.ellipse(Surface, self.color, self.rect)
        
        # draw mouth
        self.updateMouth()
        pygame.draw.polygon(Surface, (255, 255, 255), self.mouth_points)
    def limitVelocity(self, v):
        # if velocity is greater than max_velocity in positive
        if v > self.max_velocity:
            return(self.max_velocity)
        
        # if velocity is greater than max_velocity in negative
        elif (abs(v) > self.max_velocity) and (v < 0):
            return(self.max_velocity * -1)
        
        # otherwise, return the same velocity
        else:
            return(v)
        
    def applyForce(self, force):
        # apply force
        self.xv += force[0]
        self.yv += force[1]
        
        # limit velocity to specified limit
        self.xv = self.limitVelocity(self.xv)
        self.yv = self.limitVelocity(self.yv)

# a rect object that has a corresponding color
class ColorRect:
    def __init__(self, leftx, topy, width, height, color):
        self.rect = pygame.Rect(leftx, topy, width, height)
        self.color = color
        self.left = leftx
        self.right = leftx + width
        self.top = topy
        self.bottom = topy + height
    def draw(self, Surface):
        try:
            pygame.draw.rect(Surface, self.color, self.rect)
        except:
            print(self.color)
    def drawEllipse(self, Surface):
        try:
            pygame.draw.ellipse(Surface, self.color, self.rect)
        except:
            print(self.color)

class Plot:
    def __init__(self, leftX, topY, unitWidth, unitHeight, level):
        self.leftX = leftX
        self.topY = topY
        self.unitWidth = unitWidth
        self.unitHeight = unitHeight
        self.rect = pygame.Rect(0, 0, self.unitWidth, self.unitHeight)
        self.level = level
        self.matrix = [] #levels.levels[level]
        for y in range(len(levels.levels[level])):
            self.matrix.append([])
            for x in range(len(levels.levels[level][y])):
                cl = levels.symbols[levels.levels[level][y][x]]
                self.matrix[y].append(ColorRect(x * unitWidth, y * unitHeight, unitWidth, unitHeight, cl))
    def setUnit(self, position, color):
        x, y = position
        original = self.matrix[y][x].color
        try:
            self.matrix[y][x].color = color
        except IndexError:
            self.matrix[y][x].color = original
    def getUnit(self, position):
        x, y = position
        return(self.matrix[y][x].color)
    def drawUnit(self, Surface, position):
        x, y = position
        r = self.matrix[y][x]
        r.draw(Surface)
    def draw(self, Surface):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                self.drawUnit(Surface, (x, y))