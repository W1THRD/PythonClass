
import os, pygame, random, pygame.freetype

pygame.init()
win = pygame.display.set_mode((500, 500))

text = pygame.freetype.Font("Asset-Regular.ttf", 12)
text.fgcolor = (123, 255, 123)

def randColor():
    return((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

def randRect():
    r = pygame.Rect(random.randint(0, 500), random.randint(0, 500), random.randint(5, 300), random.randint(5, 300))
    return(r)

def randPos():
    return((random.randint(0, 500), random.randint(0, 500)))

def randPolygon():
    points = []
    for i in range(random.randint(3, 5)):
        points.append(randPos())
    return(points)

words = []
with open("words.txt", "r") as f:
    words = f.read().splitlines()

sound_names = os.listdir("./sounds/")
sounds = []

for sound in sound_names:
        sounds.append(pygame.mixer.Sound("sounds/" + sound))


timer = 20000
c = pygame.time.Clock()
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
    win.fill(randColor())
    for i in range(random.randint(8, 15)):
        pygame.draw.polygon(win, randColor(), randPolygon())  
    for i in range(15):
        text.render_to(win, (0, i * 10), random.choice(words))
    pygame.display.flip()
    random.choice(sounds).play()
    
    c.tick(30)
    timer -= c.get_time()
    if timer <= 0:
        playing = False