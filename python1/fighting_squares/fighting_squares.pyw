
import pygame, plot, random, pygame.freetype

print("Loading, please wait...")

pygame.init()
win = pygame.display.set_mode((1000, 600))

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

p = plot.Plot(0, 0, 10, 10, 50, 50, red)

redCount = 50
blueCount = 50
leader = black
totalTakeovers = 0
leaderChanges = 0

redTakeovers = 0
blueTakeovers = 0

redBar = pygame.Rect(0, 520, 50, 20)
blueBar = pygame.Rect(0, 550, 50, 20)
leadBar = pygame.Rect(420, 520, 50, 50)

countText = pygame.freetype.Font("Acme-Regular.ttf", 20)
countText.fgcolor = (255, 255, 255)
largeText = pygame.freetype.Font("Acme-Regular.ttf", 45)
largeText.fgcolor = (255, 255, 255)
redLargeText = pygame.freetype.Font("Acme-Regular.ttf", 45)
redLargeText.fgcolor = (255, 0, 0)
blueLargeText = pygame.freetype.Font("Acme-Regular.ttf", 45)
blueLargeText.fgcolor = (0, 0, 255)

takeover = pygame.mixer.Sound("Munch.mp3")
end = pygame.mixer.Sound("TahDah2.mp3")
redLeader = pygame.mixer.Sound("ElectricGuitarA.mp3")
blueLeader = pygame.mixer.Sound("ElectricGuitarB.mp3")

def getSides(position):
    x, y = position
    
    sides = []
    sides.append((x - 1, y))
    sides.append((x + 1, y))
    sides.append((x, y - 1))
    sides.append((x, y + 1))
    output = []
    for s in sides:
        try:
            p.getUnit(s)
            output.append(s)
        except IndexError:
            pass
    return(sides)

for y in range(p.height):
    for x in range(round(p.width/2), p.width):
        p.setUnit((x, y), blue)

print("The wars have begun!")
clock = pygame.time.Clock()
timer = 0
frames = 0
running = True
changing = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if changing:
        timer += clock.get_time()
        frames += 1
        for y in range(random.randint(1,10)):
            x = random.randint(0, p.width - 1)
            y = random.randint(0, p.height - 1)
            self = p.getUnit((x, y))
            if self == red:
                enemy = blue
            elif self == blue:
                enemy = red
            else:
                print("error")
                running = False
            sides = getSides((x, y))
            if (len(sides) > 0):
                for s in sides:
                    try:
                        if (random.randint(0, 0) == 0) and (p.getUnit(s) != self):
                            # debugging stuff: uncomment if the program has a bug in it
                            #print("Pos " + str((x, y)) + " Color " + str(p.getUnit((x, y))))
                            #print("Pos " + str(s) + " Color " + str(p.getUnit(s)))
                            #input("...")
                            sX, sY = s
                            if(sX >= 0 and sX <= p.width-1 and sY >= 0 and sY <= p.height-1):
                                p.setUnit(s, self)
                                takeover.play()
                                if(self == red):
                                    redCount += 1
                                    blueCount -= 1
                                    redTakeovers += 1
                                if(self == blue):
                                    redCount -= 1
                                    blueCount += 1
                                    blueTakeovers += 1
                                totalTakeovers += 1
                    except IndexError:
                        pass
    else:
        frames = 0
                
    redBar.width = redCount * 4
    blueBar.width = blueCount * 4
    
    if leader != red and redCount > blueCount:
        leader = red
        redLeader.play()
        leaderChanges += 1
    elif leader != blue and blueCount > redCount:
        leader = blue
        blueLeader.play()
        leaderChanges += 1
    elif leader != black and blueCount == redCount:
        leader = black
    
    win.fill((50, 50, 50))
    
    p.draw(win)
    pygame.draw.line(win, black, (0, 500),  (500, 500), 4)
    pygame.draw.line(win, black, (500, 0),  (500, 600), 4)
    pygame.draw.rect(win, red, redBar)
    pygame.draw.rect(win, blue, blueBar)
    pygame.draw.rect(win, leader, leadBar)
    countText.render_to(win, (420, 520), "Leader")
    countText.render_to(win, (0, 520), str(redCount)) # red counter
    countText.render_to(win, (0, 550), str(blueCount)) # blue counter
    largeText.render_to(win, (520, 20), "Total Takeovers: " + str(totalTakeovers))
    seconds = round(timer/1000)
    largeText.render_to(win, (520, 60), "Runtime: " + str(seconds) + "s")
    try:
        takeoverRate = round(totalTakeovers / (timer / 1000), 2)
    except ZeroDivisionError:
        takeoverRate = 0
    largeText.render_to(win, (520, 100), "Takeover Rate: " + str(takeoverRate) + "/s")
    largeText.render_to(win, (520, 140), "Leader Swaps: " + str(leaderChanges))
    
    redLargeText.render_to(win, (520, 200), "Red Takeovers: " + str(redTakeovers))
    try:
        redTakeoverRate = round(redTakeovers / (timer / 1000), 2)
    except ZeroDivisionError:
        redTakeoverRate = 0
    redLargeText.render_to(win, (520, 240), "Red Takeover Rate: " + str(redTakeoverRate) + "/s")
    
    blueLargeText.render_to(win, (520, 320), "Blue Takeovers: " + str(blueTakeovers))
    try:
        blueTakeoverRate = round(blueTakeovers / (timer / 1000), 2)
    except ZeroDivisionError:
        blueTakeoverRate = 0
    blueLargeText.render_to(win, (520, 360), "Blue Takeover Rate: " + str(blueTakeoverRate) + "/s")
    
    try:
        fps = round(frames / (timer / 1000), 2)
    except ZeroDivisionError:
        fps = 0
    largeText.render_to(win, (520, 560), str(fps) + " FPS")
    pygame.display.flip()
    
    if (redCount + blueCount) != 100:
        print("Error: there are more than 100 squares")
        print(redCount + blueCount)
        changing = False
    if (redCount == 100) and (blueCount == 0) and changing:
        print("Red wins!")
        end.play()
        changing = False
    if (redCount == 0) and (blueCount == 100) and changing:
        print("Blue wins!")
        end.play()
        changing = False
    clock.tick(5)