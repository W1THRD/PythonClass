# DO NOT RUN THIS!
# Run CodingPractice.py instead
# This file manages Y-scrolling

# import modules
import pygame, random, math, objects
pygame.init()

# initiate sounds
snow_roll = pygame.mixer.Sound("Scrape.mp3")
snow_shrink = pygame.mixer.Sound("SandFall.mp3")
snow_collide = pygame.mixer.Sound("Explosion.mp3")
snow_consume = pygame.mixer.Sound("ItemUse.mp3")

# fail text
fail_text = ["This message should never appear.", "Too small!", "Too big!", "Crashed!"]

# scroller class: manages player's rolling speed and scrolls objects
class Scroller:
    # initialize properties
    def __init__(self, pos, scale, roll_speed=0.35):
        # position and width
        self.x, self.y = pos
        self.width, self.height = scale
        self.snow_roll_sound_timer = 0
        
        # timers and crap
        self.accumulate = 0
        self.old_y = self.y
        
        # death sequence
        self.endtimer = 0
        self.failcode = 0
        self._oldfailcode = 576832423750
        self.font = pygame.freetype.Font("Archivo-Italic.ttf", 48)
        self.font.fgcolor = (200, 0, 0)
        # fail codes:
        # 0: didn't fail - still alive
        # 1: too small
        # 2: too big
        # 3: collision with obstacle
        
        # music stuff
        self.musictimer = 0
        self.game_music = pygame.mixer.Sound("MountainKing.mp3")
        self.game_music_length = self.game_music.get_length() * 1000
        
        # physics stuff
        self.roll_speed = roll_speed
        self.yv = 0
        
        # create background details and objects
        self.details = []
        for i in range(random.randint(10, 15)):
            self.details.append((random.randint(self.x, self.x + self.width), random.randint(self.y, self.y + self.height)))
        self.objects = []
    
    # creates a detail
    def spawnDetail(self):
        self.details.append((random.randint(round(self.x), round(self.x + self.width)), round(self.height)))
    
    # creates an object
    def spawnObject(self, object_type):
        x = random.randint(round(self.x), round(self.x + self.width))
        y = self.height
        self.objects.append(object_type((x, y)))
    
    # update scroller's onscreen objects and details
    def update(self, time, player, UI, vertical_input=0, spawn_objects=True):
        # check if the snowball is the right size
        if self.failcode != 0:
            self._oldfailcode = self.failcode
            self.game_music.stop()
            self.endtimer += time
            self.yv = 0
            if self.endtimer >= 2000:
                UI.state = 2
        else:
            # stop death music from playing
            UI.death_music.stop()
            
            # if the game just barely started, play the music
            if self._oldfailcode != 0:
                self.game_music.play()
                self._oldfailcode = 0
            
            # is the music over? play it again!
            self.musictimer += time
            if self.musictimer >= self.game_music_length:
                self.game_music.play()
                self.musictimer = 0
            
            # apply Y velocity
            velocity_change = vertical_input * self.roll_speed
            self.yv += velocity_change
            player.distance += abs(self.yv) / 10
            self.yv = math.copysign(self.yv, -1)
            if velocity_change > 0:
                self.yv *= 0.94
            elif self.yv < -20:
                self.yv = -20
            self.y += self.yv
        
            # play rolling sound
            self.snow_roll_sound_timer += time
            snow_roll.set_volume(self.yv / -20)
            if self.snow_roll_sound_timer >= 1000:
                snow_roll.stop()
                snow_roll.play()
                self.snow_roll_sound_timer = 0
        
            # increase accumulation timer
            self.accumulate += math.copysign(self.yv, 1)
        
            # if accumulation timer reaches limit, increase player size
            if self.accumulate >= 200:
                player.radius += 1
                self.accumulate = 0
                sizeCheck = player.sizeCheck()
                if sizeCheck[0]:
                    snow_collide.play()
                    self.failcode = sizeCheck[1]
            
            # apply Y-friction
            if abs(self.yv) >= 0.1:
                self.yv = math.copysign(self.yv, -1)
                self.yv *= 1.001
            else:
                self.yv = 0
            
            # has the player moved at least 30 pixels?  If so, try to spawn a new object/detail
            if self.y <= (self.old_y - 30):
                self.old_y = self.y
                # spawn details
                if random.randint(1, 2) == 1:
                    self.spawnDetail()
                
                # spawn objects
                if spawn_objects:
                    # 1/20 chance of spawning tree
                    if random.randint(1, 20) == 1:
                        self.spawnObject(objects.Tree)
                
                    # 1/15 chance of spawning rock
                    if random.randint(1, 15) == 1:
                        self.spawnObject(objects.Rock)
            
                    # 1/10 chance of spawning campfire
                    if random.randint(1, 10) == 1:
                        self.spawnObject(objects.Campfire)
                    
                    # 1/25 chance of spawning snowball
                    if random.randint(1, 15) == 1:
                        self.spawnObject(objects.Snowball)
        
        # update details
        details_to_remove = []
        for i in range(len(self.details)):
            x, y = self.details[i]
            y += self.yv
            self.details[i] = (x, y)
            # is it offscreen? if so, remove it
            if (y+14) < 0:
                details_to_remove.append(self.details[i])
        for detail in details_to_remove:
            self.details.remove(detail)
        
        # update objects
        objects_to_remove = []
        for i in range(len(self.objects)):
            # scroll object
            thing = self.objects[i]
            thing.scroll(self.yv)
            
            # is it offscreen? if so, remove it
            if (thing.y + thing.height) < 0:
                objects_to_remove.append(thing)
            
            # check player collision
            if player.rect.colliderect(thing.collider) and (self.failcode == 0):
                if (type(thing) == objects.Tree) or (type(thing) == objects.Rock):
                    snow_roll.stop()
                    snow_collide.play()
                    self.failcode = 3
                elif (type(thing) == objects.Campfire) and (not thing.used):
                    player.radius *= 0.75
                    thing.used = True
                    snow_shrink.play()
                elif (type(thing) == objects.Snowball):
                    player.radius += thing.radius
                    objects_to_remove.append(thing)
                    snow_consume.play()
        for thing in objects_to_remove:
                self.objects.remove(thing)
    
    # draw background details
    def drawDetails(self, window):
        for detail in self.details:
            x, y = detail
            pygame.draw.line(window, (185, 185, 185), (x, y), (x, y + 10), 4)
    
    # draw objects
    def drawObjects(self, window):
        for thing in self.objects:
            thing.draw(window)
    
    # draw fail text
    def drawFailText(self, window, player, win_size):
        if self.failcode != 0:
            # center text on player
            win_width, win_height = win_size
            text = fail_text[self.failcode]
            rect = self.font.get_rect(text)
            x = player.x - (rect.width/2)
            y = (player.y + player.radius) + 20
            
            # prevent offscreen text
            if (x + rect.width) > win_width:
                x = 500 - rect.width
            if x < 0:  
                x = 0
            
            self.font.render_to(window, (round(x), round(y)), text)
                