# don't run this file! it's the wrong one
# in the techsmart sidebar, click on project, and then on "pewpewpew.py"

import pygame, pygame.freetype, random

pygame.init()
hurt = pygame.mixer.Sound("ExcitedScream.mp3")

red = (255, 0, 0)
green = (0, 255, 0)

font = pygame.freetype.Font("OpenSans-ExtraBold.ttf", 20)

critFont = pygame.freetype.Font("OpenSans-ExtraBold.ttf", 20)
critFont.fgcolor = red

class critText:
    def __init__(self, position, createdTime):
        self.x, self.y = position
        self.createdTime = createdTime
    def draw(self, Surface):
        critFont.render_to(Surface, (self.x, self.y), "CRITICAL HIT")
        

class ammoBox:
    def __init__(self, position):
        self.x, self.y = position
        self.rect = pygame.Rect(self.x - 40, self.y - 30, 80, 60)
        self.textRect = font.get_rect("AMMO")
    def draw(self, Surface):
        pygame.draw.rect(Surface, (120, 120, 120), self.rect)
        pygame.draw.rect(Surface, (0, 0, 0), self.rect, 8)
        pos = (self.x - (self.textRect.width / 2), self.y - (self.textRect.height / 2))
        font.render_to(Surface, pos, "AMMO")

class enemy:
    def __init__(self, position, color):
        self.x, self.y = position
        self.color = color
        self.health = 40
        self.maxhealth = self.health
        self.rect = pygame.Rect(self.x - 25, self.y - 40, 50, 80)
        self.healthbarGreen = pygame.Rect(self.x - 10 , self.y - 60, 20, 10)
        self.healthbarRed = pygame.Rect(self.x - 10 , self.y - 60, 20, 10)
    def move(self):
        if self.health > 0:
            self.x += random.randint(-10, 10)
            while self.x < 0:
                self.x += 1
            while self.x > 1000:
                self.x -= 1
            self.y += random.randint(-10, 10)
            while self.y < 100:
                self.y += 1
            while self.y > 1000:
                self.y -= 1
        else:
            self.y += 20
    def draw(self, Surface):
        self.rect.x = self.x - 25 
        self.rect.y = self.y - 40
        
        if self.health > 0:
            pygame.draw.rect(Surface, self.color, self.rect)
            self.healthbarGreen.x = self.x - 10 
            self.healthbarGreen.y = self.y - 60
            self.healthbarGreen.width = round((self.health / self.maxhealth) * 20)
            self.healthbarRed.x = self.x - 10 
            self.healthbarRed.y = self.y - 60
            
            pygame.draw.rect(Surface, red, self.healthbarRed)
            pygame.draw.rect(Surface, green, self.healthbarGreen)
        else:
            self.rect.width = 80
            self.rect.height = 50
            pygame.draw.rect(Surface, red, self.rect)
    def dealDamage(self, damage):
        if self.health > 0:
            self.health -= damage
            hurt.play()
        if self.health < 0:
            self.health = 0
    