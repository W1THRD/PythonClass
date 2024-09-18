# DO NOT RUN THIS!
# Run CodingPractice.py instead
# This file handles game menus

# import libraries
import pygame, pygame.freetype
pygame.init()

# instructions text
instructions_text = ["Arrow keys to move",
                     "Press P to pause",
                     "Don\'t touch trees or rocks",
                     "Use campfires to shrink"]

# score counter: displays the player's distance traveled
class ScoreCounter:
    # initiate variables
    def __init__(self, y):
        self.y = y
        self.font = pygame.freetype.Font("Archivo-Italic.ttf", 48)
        self.font.fgcolor = (0, 0, 0)
    
    # draw score counter, with player's distance traveled
    def draw(self, window, player, win_size):
        text = str(round(player.distance)) + " meters"
        
        screen_width, screen_height = win_size
        r = self.font.get_rect(text)
        width = r.width
        height = r.height
        x = .5 * screen_width - .5 * width
        self.font.render_to(window, (x, self.y), text)

# UI Manager manages the start menu and the death/losing menu
class UIManager:
    # initiate the UI manager
    def __init__(self, state=0):
        # UI state codes:
        # 0: start menu
        # 1: playing game (no UI)
        # 2: death/losing menu
        # 3: pause menu
        self._oldstate = state
        self.state = state
        self.title = pygame.freetype.Font("Modak-Regular.ttf", 88)
        self.subtitle = pygame.freetype.Font("Modak-Regular.ttf", 48)
        self.button_text = pygame.freetype.Font("Archivo-Italic.ttf", 48)
        self.instructions = pygame.freetype.Font("Archivo-Italic.ttf", 28)
        self.button = pygame.Rect(125, 260, 250, 80)
        self.timer = 0
        
        # initiate music
        self.death_music = pygame.mixer.Sound("Grunting.mp3") # Not really music, but oh well
        self.death_music_length = self.death_music.get_length() * 1000
    
    # draws centered title text on the screen
    def centerText(self, window, font, text, win_size, y):
        screen_width, screen_height = win_size
        r = font.get_rect(text)
        width = r.width
        height = r.height
        x = 0.5 * screen_width - 0.5 * width
        font.render_to(window, (x, y), text)
        
    # pause/unpause the game
    def pause(self):
        if self.state == 1:
            self.state = 3
        elif self.state == 3:
            self.state = 1
        
    # draws the menus
    def draw(self, window, win_size, time):
        if self.state != 2:
            self.death_music.stop()
            self._oldstate = self.state
        
        if self.state == 0:
            # draw background
            window.fill((100, 100, 100))
            
            # draw centered title
            self.title.fgcolor = (255, 255, 255)
            self.centerText(window, self.title, "Snow Roller", win_size, 20)
            
            # draw centered subtitle
            self.subtitle.fgcolor = (225, 225, 225)
            self.centerText(window, self.subtitle, "A game by W1THRD", win_size, 120)
            
            # draw button with text
            self.button_text.fgcolor = (255, 255, 255)
            pygame.draw.rect(window, (226, 80, 80), self.button)
            self.centerText(window, self.button_text, "PLAY", win_size, self.button.y + 20)
            
            # draw instructions
            for i in range(len(instructions_text)):
                self.centerText(window, self.instructions, instructions_text[i], win_size, 360 + (i*30))
        elif self.state == 1:
            return
        elif self.state == 2:
            # if the state just barely changed, start music
            if (self.state != self._oldstate):
                self.death_music.play()
                self._oldstate = self.state
            
            # if the music is over, play it again
            self.timer += time
            if self.timer >= self.death_music_length:
                self.death_music.play()
                self.timer = 0
            
            
            # fill window
            window.fill((200, 0, 0))
            
            # draw centered title
            self.title.fgcolor = (255, 255, 255)
            self.centerText(window, self.title, "YOU DIED!", win_size, 150)
            
            # draw button with text
            self.button_text.fgcolor = (255, 255, 255)
            pygame.draw.rect(window, (226, 80, 80), self.button)
            self.centerText(window, self.button_text, "RESTART", win_size, self.button.y + 20)
        elif self.state == 3:
            window.fill((200, 200, 200))
            
            # draw pause text
            self.title.fgcolor = (255, 255, 255)
            self.centerText(window, self.title, "PAUSED", win_size, 240)
    
    # handle mouse clicks
    def clicked(self, pos, restart):
        if self.state == 0:
            # start the game if the button is clicked
            if self.button.collidepoint(pos):
                self.state = 1  
        elif self.state == 1:
            # do nothing, there is no mouse input during gameplay
            return
        elif self.state == 2:
            # restart the game if the button is clicked
            if self.button.collidepoint(pos):
                restart()
                self.state = 1
        elif self.state == 3:
            # do nothing, there is no mouse input during pause mode
            return