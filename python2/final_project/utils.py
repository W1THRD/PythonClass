# DO NOT RUN THIS!
# Run CodingPractice.py instead
# This file handles controls and debugging

# import modules
import pygame, pygame.freetype, tsk
pygame.init()

# types of controls (horizontal or vertical)
horizontal_mode = (pygame.K_LEFT, pygame.K_RIGHT)
vertical_mode = (pygame.K_DOWN, pygame.K_UP)

# function for detecting directional controls (horizontal or vertical)
def control(mode):
    key_minus, key_plus = mode
    key = 0
    if tsk.get_key_pressed(key_minus):
        key -= 1
    if tsk.get_key_pressed(key_plus):
        key += 1
    return(key)

# debugger class: displays debug text
class Debugger:
    # iniate font, font size, color, and messages array
    def __init__(self, color, size=16):
        self.font = pygame.freetype.Font("Archivo-Italic.ttf", size)
        self.font.fgcolor = color
        self.messages = []
    
    # add text to messages
    def add(self, text):
        self.messages.append(text)
    
    # draw text, clear messages
    def draw(self, window):
        y = 0
        for i in range(len(self.messages)):
            message = self.messages[i]
            message_rect = self.font.get_rect(message)
            self.font.render_to(window, (0, y), message)
            y += message_rect.height + 4
        self.messages = []