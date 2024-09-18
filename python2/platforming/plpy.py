# DO NOT RUN THIS FILE! Do the other one instead.
# This is a library file that contains all the functions.

import pygame

pygame.init()

def limitAbsolute(num, limit):
    if num < (limit * -1):
        return(limit * -1)
    elif num > limit:
        return(limit)
    else:
        return(num)

def checkFixedTuple(t, length):
    # is it a tuple?
    if type(t) == tuple:
        # does the tuple have 2 elements?
        if len(t) != length:
            raise ValueError("Tuple requires " + str(length) + " elements, but found " + str(len(t)) + ".")
    else:
        raise TypeError("Tuple was required, but found " + str(type(t)) + ".")

def checkCoords(t):
    # is the tuple valid?
    checkFixedTuple(t, 2)
    
    # are the coordinates integers?
    x, y = t
    if type(x) != int:
        raise TypeError("Int was expected for X coordinate, but found " + str(type(x)) + ".")
    if type(y) != int:
        raise TypeError("Int was expected for Y coordinate, but found " + str(type(y)) + ".")

def checkColor(t):
    # is the tuple valid?
    checkFixedTuple(t, 3)
    
    # are the RBG values integers between 0 and 255?
    r, g, b = t
    if type(r) != int:
        raise TypeError("Int was expected for R value, but found " + str(type(r)) + ".")
    elif r < 0 or r > 255:
        raise ValueError("R value was expected to be in range 0-255, but found " + str(r))
    
    if type(g) != int:
        raise TypeError("Int was expected for G balue, but found " + str(type(g)) + ".")
    elif g < 0 or g > 255:
        raise ValueError("G value was expected to be in range 0-255, but found " + str(g))

    if type(b) != int:
        raise TypeError("Int was expected for B balue, but found " + str(type(b)) + ".")
    elif b < 0 or b > 255:
        raise ValueError("B value was expected to be in range 0-255, but found " + str(b))

class Box:
    def __init__(self, pos, scale, color):
        checkCoords(pos)
        self.x, self.y = pos
        
        checkCoords(scale)
        self.width, self.height = scale
        
        checkColor(color)
        self.color = color
    
    @property
    def rect(self):
        return(pygame.Rect(self.x, self.y, self.width, self.height))
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

class Player:
    def __init__(self, pos, jump_height, move_speed):
        checkCoords(pos)
        self.x, self.y = pos
        self.spawnX, self.spawnY = pos
        
        self.xv = 0
        self.yv = 0
        self.jump_height = jump_height
        self.move_speed = move_speed
    
    @property
    def rect(self):
        return(pygame.Rect(round(self.x), round(self.y), 50, 50))
    
    @property
    def bottom(self):
        return(pygame.Rect(round(self.x), round(self.y + 50), 50, 1))
    
    @property
    def top(self):
        return(pygame.Rect(round(self.x), round(self.y), 50, 1))
    
    @property
    def left(self):
        return(pygame.Rect(round(self.x), round(self.y), 1, 50))
    
    @property
    def right(self):
        return(pygame.Rect(round(self.x + 50), round(self.y), 1, 50))
    
    def _gravity(self, level):
        if not level.colliderect(self.rect):
            self.yv += 1
    
    def _friction(self, velocity, friction=0.2):
        if velocity < -0.1 or velocity > 0.1:
            if velocity < 0:
                velocity += friction
            elif velocity > 0:
                velocity -= friction
        else:
            velocity = 0
        return(velocity)
    
    def respawn(self):
        self.x, self.y = (self.spawnX, self.spawnY)
        self.xv = 0
        self.yv = 0
    
    def _checkDeath(self):
        if self.y > 500:
            oldpos = (self.x, self.y)
            self.respawn()
            return(True, oldpos)
        else:
            return(False, ())
    
    def update(self, level):
        death = self._checkDeath()
        self._gravity(level)
        if self.yv != 0:
            self.yv = limitAbsolute(self.yv, 18)
            if round(self.yv)!= 0:
                repeats = abs(round(self.yv))
            else:
                repeats = 1
            for i in range(repeats):
                self.y += self.yv / repeats
                if (self.yv < 0 and level.colliderect(self.top)) or (self.yv > 0 and level.colliderect(self.bottom)):
                    self.y -= self.yv ** 0
                    self.yv = 0
                    break
                
                
        if self.xv != 0:
            self.xv = limitAbsolute(self.xv, 10)
            self.x += self.xv
            self.xv = self._friction(self.xv)
            if level.colliderect(self.right):
                while level.colliderect(self.rect):
                    self.x -= 1
                self.xv = 0
            elif level.colliderect(self.left):
                while level.colliderect(self.rect):
                    self.x += 1
                self.xv = 0
    
    def jump(self, level):
        if level.colliderect(self.bottom):
            self.yv = self.jump_height
    
    def move(self, level, direction):
        if direction == -1 and (not level.colliderect(self.left)):
            self.xv -= 1
        elif direction == 1 and (not level.colliderect(self.right)):
            self.xv += 1
    
    def draw(self, window, draw_sides=False):
        pygame.draw.rect(window, (255, 0, 0), self.rect)
        if draw_sides:
            for side in [self.top, self.bottom, self.left, self.right]:
                pygame.draw.rect(window, (0, 0, 255), side, 5)
class Level:
    def __init__(self, boxes=[]):
        if type(boxes) == list:
            for box in boxes:
                if type(box) != Box:
                    raise TypeError("Cannot create Level with elements of boxes parameter as " + str(type(boxes)) + ".")
            self.boxes = boxes
        else:
            raise TypeError("Cannot create Level with boxes parameter of " + str(type(boxes)) + ".")
    
    def addBox(self, pos, scale, color):
        self.boxes.append(Box(pos, scale, color))
    
    def collidepoint(self, point):
        for box in self.boxes:
            if box.rect.collidepoint(point):
                return(True)
        return(False)
    
    def colliderect(self, rect):
        for box in self.boxes:
            if box.rect.colliderect(rect):
                return(True)
        return(False)
    
    def draw(self, window):
        if type(window) == pygame.Surface:
            for box in self.boxes:
                box.draw(window)
        else:
            raise TypeError("Cannot draw Level on " + str(type(window)) + ".")