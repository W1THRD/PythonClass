# DO NOT RUN THIS!
# Run CodingPractice.py instead
# This file manages objects (player, obstacles, pickups, etc.)

# import modules
import pygame, math, random

# initiate pygame
pygame.init()

# create a rect with coordinates relative to another rect or object
def relRect(rect, relX, relY, rel_width, rel_height):
    x = round((relX * rect.width) + rect.x)
    y = round((relY * rect.height) + rect.y)
    width = round(rel_width * rect.width)
    height = round(rel_height * rect.height)
    return(pygame.Rect(x, y, width, height))

def relPoints(rect, points):
    new_points = []
    for i in range(len(points)):
        x, y = points[i]
        x = round((x * rect.width) + rect.x)
        y = round((y * rect.height) + rect.y)
        new_points.append((x, y))
    return(new_points)

def scrollPoints(points, yv):
    for i in range(len(points)):
        x, y = points[i]
        y += yv
        points[i] = (x, y)


# class for the player
class Player:
    # initate player variables
    def __init__(self, pos, radius=20, move_speed=0.1, max_speed=0.5):
        self.x, self.y = pos
        self.radius = radius
        
        self.move_speed = 0.04
        self.max_speed = 0.5
        self.xv = 0
        
        self.distance = 0
        
    # check if the player size is too big or too small
    def sizeCheck(self):
        if self.radius > 50:
            return((True, 2))
        elif self.radius < 10:
            return((True, 1))
        else:
            return((False, 0))
    
    
    # updates the snowball's position once every frame
    # deals with horizontal control, as well as constant movement forwards
    def update(self, time, horizontal_input=0):
        # make the player bounce off the wall
        if (self.x + self.radius >= 500):
            self.xv = math.copysign(self.xv, -1)
            self.x = 500 - self.radius
        elif (self.x - self.radius <= 0):
            self.xv = math.copysign(self.xv, 1)
            self.x = 0 + self.radius
    
        # apply X velocity
        self.xv += horizontal_input * self.move_speed
        self.x += self.xv * time
        
        # apply X velocity limit
        if self.xv > (self.max_speed):
            self.xv = self.max_speed
        elif self.xv < (self.max_speed * -1):
            self.xv = self.max_speed * -1
        
        # apply X friction
        if abs(self.xv) >= 0.01:
            self.xv *= 0.92
        else:
            self.xv = 0

    # returns a rect for drawing or detecting
    @property
    def rect(self):
        return(pygame.Rect(round(self.x - self.radius), round(self.y - self.radius), round(self.radius) * 2, round(self.radius) * 2))
    
    # draws the player
    def draw(self, window):
        pygame.draw.ellipse(window, (255, 255, 255), self.rect)
        pygame.draw.ellipse(window, (100, 100, 100), self.rect, 4)
        
class Obstacle:
    def __init__(self, pos):
        self.x, self.y = pos
        self.width, self.height = (40, 15)
    
    @property
    def collider(self):
        return(pygame.Rect(round(self.x), round(self.y), self.width, self.height))
    
    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), self.collider)
        
# collectable snowball
class Snowball(Obstacle):
    # initiate variables
    def __init__(self, pos):
        self.x, self.y = pos
        self.xv = random.randint(-12, 12)
        self.radius = random.randint(10, 20)
        
    # return width/height, so the scroller won't throw an error when it tries to get that info
    @property
    def width(self):
        return(self.radius * 2)
    @property
    def height(self):
        return(self.radius * 2)
    
    # returns a rect for drawing or detecting
    @property
    def collider(self):
        return(pygame.Rect(round(self.x - self.radius), round(self.y - self.radius), round(self.radius) * 2, round(self.radius) * 2))
    
    # scrolls the object
    def scroll(self, yv):
        # scroll y
        self.y += yv
        
        # move snowball
        self.x += self.xv
        
        # make the snowball bounce off the wall
        if (self.x + self.radius >= 500):
            self.xv = math.copysign(self.xv, -1)
            self.x = 500 - self.radius
        elif (self.x - self.radius <= 0):
            self.xv = math.copysign(self.xv, 1)
            self.x = 0 + self.radius
    
    # draw the object
    def draw(self, window):
        pygame.draw.ellipse(window, (250, 250, 250), self.collider)
        pygame.draw.ellipse(window, (210, 210, 210), self.collider, 4)
        
# tree obstacle
class Tree(Obstacle):
    # initiate variables
    def __init__(self, pos):
        self.x, self.y = pos
        self.width, self.height = (40, 80)
        self.stump = relRect(self, 0.25, 0.75, 0.5, 0.25)
        self.leaves = relPoints(self, [(1, 0.75), (0.5, 0), (0, 0.75)])
        
    # scrolls the object
    def scroll(self, yv):
        self.y += yv
        self.stump.y += round(yv)
        scrollPoints(self.leaves, round(yv))
    
    # returns a rect for collision checking
    @property
    def collider(self):
        return(pygame.Rect(round(self.x), round(self.y), self.width, self.height))
    
    # draw the tree leaves and stump
    def draw(self, window):
        pygame.draw.rect(window, (165, 42, 42), self.stump)
        pygame.draw.polygon(window, (0, 200, 0), self.leaves)

# rock obstacle
class Rock(Obstacle):
    # initiate variables
    def __init__(self, pos):
        self.x, self.y = pos
        self.width, self.height = (40, 40)
        self.rock = relPoints(self, [(0.80, 1), (1, 0.90), (0.95, 0.40), (0.35, 0.2),
                  (0, 0.90), (0.2, 1)])
    
    # scrolls the object
    def scroll(self, yv):
        self.y += yv
        scrollPoints(self.rock, yv)
    
    # returns a rect for collision checking
    @property
    def collider(self):
        return(pygame.Rect(round(self.x), round(self.y), self.width, self.height))
    
    # draw the tree leaves and stump
    def draw(self, window):
        pygame.draw.polygon(window, (120, 120, 120), self.rock)

# campfire obstacle
class Campfire(Obstacle):
    # initiate variables
    def __init__(self, pos):
        self.x, self.y = pos
        self.width, self.height = (80, 60)
        self.used = False
        self.wood = relPoints(self, [(0.5, 0.75), (0.75, 0.625), (0.75, 0.625), (0.875, 0.75), (0.75, 0.875), (0.625, 1),
                  (0.5, 0.80), (0.375, 1), (0.25, 0.875), (0.125, 0.75), (0.25, 0.625)])
        self.flame = relPoints(self, [(0.75, 0.625), (0.75, 0.25), (0.625, 0.5), (0.625, 0), (0.5, 0.625),
                  (0.375, 0.25), (0.375, 0.625), (0.25, 0), (0.25, 0.5), (0.375, 0.75)])
    
    # scrolls the object
    def scroll(self, yv):
        self.y += yv
        scrollPoints(self.wood, yv)
        scrollPoints(self.flame, yv)
    
    # returns a rect for collision checking
    @property
    def collider(self):
        return(pygame.Rect(round(self.x), round(self.y), self.width, self.height))
    
    # draw the tree leaves and stump
    def draw(self, window):
        if not self.used:
            pygame.draw.polygon(window, (255, 200, 0), self.flame)
        pygame.draw.polygon(window, (165, 62, 62), self.wood)