# import modules
import pygame
import random

# function that limits the colors
def limitColor(num):
    if num > 255:
        return(255)
    elif num < 0:
        return(0)
    else:
        return(num)
    
# function that limits the points
def limitPos(num):
    if num > 500:
        return(500)
    elif num < 0:
        return(0)
    else:
        return(num)

# open pygame window
pygame.init()
win = pygame.display.set_mode((500, 500))

# generate a randomized polygon with points & color
polygon_points = []
polygon_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
for i in range(16):
    polygon_points.append((random.randint(0, 500), random.randint(0, 500)))

# start a sound
talk = pygame.mixer.Sound("FakeTalking.mp3")
talk.play()

# main loop
clock = pygame.time.Clock()
running = True
time = 0
while running:
    # event loop
    for event in pygame.event.get():
        # check if the user wants to quit
        if event.type == pygame.QUIT:
            running = False
    
    # draw polygon
    win.fill((255, 255, 255))
    pygame.draw.polygon(win, polygon_color, polygon_points)
    
    # update screen
    pygame.display.flip()
    clock.tick(30)
    
    # change polygon color
    r, g, b = polygon_color
    pos = random.randint(0, 50)
    neg = pos * -1
    r += random.randint(neg, pos)
    g += random.randint(neg, pos)
    b += random.randint(neg, pos)
    polygon_color = (limitColor(r), limitColor(g), limitColor(b))
    
    # change polygon points
    for i in range(0, len(polygon_points) - 1):
        x, y = polygon_points[i]
        x += random.randint(-10, 10)
        y += random.randint(-10, 10)
        polygon_points[i] = (limitPos(x), limitPos(y))