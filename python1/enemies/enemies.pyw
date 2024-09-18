# HOW TO PLAY:
# Use arrow keys to move pac-man
# Pacman will start out invincible, but as soon as he moves, his invisibility will be stopped
# Avoid the red squares and ellipses, they are enemies
# The enemies will change every 5 seconds
# Try and collect the coins
# If you die, click the screen to start over


# import libraries
import pygame, plot, random, pygame.freetype, tsk

# setup window
pygame.init()
win = pygame.display.set_mode((500, 500))
grid = pygame.Surface((500, 500))

# define player data
yellow = (200, 200, 0)
gray = (100, 100, 100)
immune = True
player = plot.Player((75, 75), 20, gray, 8, 0.45)
state = 0
# game states:
# 0 - playing
# 1 - dead

# define coin
coin = plot.Coin()
coins = 0

# fonts
loadFont = pygame.freetype.Font("CourierPrime-Bold.ttf", 60)
loadFont.fgcolor = (128, 0, 0)
deathFont = pygame.freetype.Font("CourierPrime-Bold.ttf", 80)
deathFont.fgcolor = (255, 0, 0)
smallDeathFont = pygame.freetype.Font("CourierPrime-Bold.ttf", 20)
smallDeathFont.fgcolor = (255, 0, 0)
coinFont = pygame.freetype.Font("CourierPrime-Bold.ttf", 60)
coinFont.fgcolor = (255, 255, 0)

# sounds
death = pygame.mixer.Sound("ExcitedScream.mp3")
music = pygame.mixer.Sound("MountainKing.mp3")
collect = pygame.mixer.Sound("Click.mp3")

# loading screen
win.fill((0, 0, 0))
loadFontRect = loadFont.get_rect("Loading...")
loadFont.render_to(win, (250 - (loadFontRect.width / 2), 250 - (loadFontRect.height / 2)), "Loading...")
pygame.display.flip()

# draw level
p = plot.Plot(0, 0, 50, 50, 0)
p.draw(grid)

# define obstacle
enemy_spacing = (400 / 3)
enemies = []
enemies.append(plot.BadEllipse((250, 250), (random.randint(-1, 0), random.randint(-1, 0))))

# setup time data
c = pygame.time.Clock()
time = 0
frame = 0

# function to pause the game if the player dies
enemyTimer = 0
running = True
def pause():
    global running, player, state, enemies, enemyTimer, immune, coins

    deathFont.render_to(win, (20, 300), "YOU DIED!")
    smallDeathFont.render_to(win, (20, 380), "Click the screen to play again, or close ")
    smallDeathFont.render_to(win, (20, 400), "the window to quit")
    pygame.display.flip()
    paused = True
    while paused:
        for event in pygame.event.get():
            # quit if the user wants to
            if event.type == pygame.QUIT:
                running = False
                paused = False
            
            # keep on going if the user wants
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.xv = 0
                player.yv = 0
                player.x = 75
                player.y = 75
                enemyTimer = 0
                coins = 0
                immune = True
                enemies = []
                enemies.append(plot.BadEllipse((250, 250), (random.randint(-1, 0), random.randint(-1, 0))))
                player.update(p.matrix)
                state = 0
                paused = False

music.play()
musicTimer = 0
# start main loop
while running:
    # keep track of time
    time += c.get_time()
    enemyTimer += c.get_time()
    musicTimer += c.get_time()
    frame += 1
    
    # event loop
    for event in pygame.event.get():
        # quit if the user wants to
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            immune = False
            
    # loop music
    if musicTimer >= 153000:
        music.play()
        musicTimer = 0
            
    # switch enemies
    if enemyTimer >= 5000:
        enemyTimer = 0
        enemies = []
        for i in range(random.randint(1, 3)):
            if random.randint(1, 2) == 1:
                enemies.append(plot.BadEllipse((int(enemy_spacing * (i + 1)), 250), (random.randint(-1, 0), random.randint(-1, 0))))
            else:
                enemies.append(plot.BadRect((int(enemy_spacing * (i + 1)), 250), (random.randint(-1, 0), random.randint(-1, 0))))
    
    # check for user input
    if tsk.get_key_pressed(pygame.K_RIGHT):
        player.applyForce((1, 0))
    if tsk.get_key_pressed(pygame.K_LEFT):
        player.applyForce((-1, 0))
    if tsk.get_key_pressed(pygame.K_UP):
        player.applyForce((0, -1))
    if tsk.get_key_pressed(pygame.K_DOWN):
        player.applyForce((0, 1))
    
    # move player
    player.update(p.matrix)
    
    # check for collisions with obstacles and coin
    if not immune:
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect) and state == 0:
                state = 1
        if player.rect.colliderect(coin.rect) and state == 0:
            collect.play()
            coin = plot.Coin()
            coins += 1

    # draw screen
    win.fill((128, 128, 128))
    win.blit(grid, (0, 0))
    
    # draw coin
    coin.draw(win)
    
    # draw player
    if immune:
        player.color = gray
    else:
        player.color = yellow
    player.draw(win)
    
    # draw obstacles
    for enemy in enemies:
        enemy.draw(win, frame)
        
    # draw score text
    coinFont.render_to(win, (0, 0), str(coins))
    
    if state == 1:
        death.play()
        state = 0
        pause()
    pygame.display.flip()
    c.tick(30)
