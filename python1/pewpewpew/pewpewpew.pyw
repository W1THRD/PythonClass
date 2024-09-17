# this is a first person shooter
# click on the brown things to shoot them
# every 5 shots, you have a chance to fire 4x as hard
# every 5 seconds, you will take damage
# click on the boxes saying "ammo" to reload
# you win when all the brown things are gone
# when you win, you can see all your stats

import pygame, random, objects, pygame.freetype

pygame.init()
window = pygame.display.set_mode((1000, 1000))

white = (255, 255, 255)
gray = (150, 150, 150)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
crosshairColor = black
bgColor = white

shots = 0
crits = 0
kills = 0
collected = 0

health = 100
maxHealth = health

ammo = 20
max_ammo = 20
HUD_rect = pygame.Rect(0, 0, 1000, 100)
bullet_rect = pygame.Rect(30, 30, 80, 40)
HUD_text = pygame.freetype.Font("Acme-Regular.ttf", 55)
healthbarGreen = pygame.Rect(860, 10, 120, 60)
healthbarRed = pygame.Rect(860, 10, 120, 60)

enemyColor = (200, 130, 0)
enemies = []
ammobox = objects.ammoBox((random.randint(0, 1000), random.randint(100, 1000)))
for i in range(random.randint(5, 10)):
    enemies.append(objects.enemy((random.randint(0, 1000), random.randint(100, 1000)), enemyColor))
enemies_amount = len(enemies)

critTexts = []

shoot = pygame.mixer.Sound("Explosion.mp3")
empty = pygame.mixer.Sound("Typewriter.mp3")
reload = pygame.mixer.Sound("WoodBreak.mp3")
winning = pygame.mixer.Sound("TahDah2.mp3")
hurt = pygame.mixer.Sound("Squelch.mp3")
death = pygame.mixer.Sound("Grunting.mp3")

def pause():
    global running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def translate(old, center):
    new = (old[0] + center[0], old[1] + center[1])
    return(new)

clock = pygame.time.Clock()
frame = 0
timer = 0
hurtTimer = 0
ammoboxTimer = 0
running = True
state = 0
while running:
    frame += 1
    timer += clock.get_time()
    hurtTimer += clock.get_time()
    ammoboxTimer += clock.get_time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            
            if (ammobox != 0) and (mouseX >= ammobox.x - 40) and (mouseX <= ammobox.x + 40) and (mouseY >= ammobox.y - 30) and (mouseY <= ammobox.y + 30):
                ammo = max_ammo
                reload.play()
                ammobox = 0
                collected += 1
            elif ammo > 0:
                shots += 1
                
                if (shots % 5 == 0) and (random.randint(1, 3) == 2):
                    for i in range(5):
                        shoot.play()
                    damage = 20
                    crits += 1
                    critTexts.append(objects.critText((mouseX, mouseY), timer))
                else:
                    shoot.play()
                    damage = 5
                crosshairColor = red
                ammo -= 1
                for e in enemies:
                    alive = e.health > 0
                    if alive and (mouseX >= e.x - 25) and (mouseX <= e.x + 25) and (mouseY >= e.y - 40) and (mouseY <= e.y + 40):
                        e.dealDamage(damage)
                        if e.health < 1:
                            kills += 1
            else:
                empty.play()
        elif event.type == pygame.MOUSEBUTTONUP:
            crosshairColor = black  
    
    
    if (hurtTimer > 5000):
        hurtTimer = 0
        health -= 5
        bgColor = (180, 0, 0)
        hurt.play()
    elif bgColor[0] > 0:
        r, g, b = bgColor
        r += 10
        if r > 255:
            r = 255 
        g += 10
        if g > 255:
            g = 255 
        b += 10
        if b > 255:
            b = 255
            
        bgColor = (r, g, b)
    
    if health < 1:
        finalTime = timer/1000
        state = 2
        running = False
    
    window.fill(bgColor)
    
    enemies = [e for e in enemies if not ((e.health < 1) and (e.y - 40 > 1000))]
    for enemy in enemies:
        enemy.move()
        enemy.draw(window)
        
    if len(enemies) == 0:
        finalTime = timer/1000
        state = 1
        running = False
    
    if ammobox != 0:
        ammobox.draw(window)
    elif (random.randint(1, 3) == 2) and (ammoboxTimer >= 5000):
        ammoboxTimer = 0
        ammobox = objects.ammoBox((random.randint(0, 1000), random.randint(100, 1000)))
    
    for c in critTexts:
        if (timer - c.createdTime) < 1000:
            c.draw(window)
    
    mousepos = pygame.mouse.get_pos()
    # right
    pygame.draw.line(window, crosshairColor, translate((10, 0), mousepos), translate((30, 0), mousepos), 10)
    # up
    pygame.draw.line(window, crosshairColor, translate((0, 10), mousepos), translate((0, 30), mousepos), 10)
    # left
    pygame.draw.line(window, crosshairColor, translate((-10, 0), mousepos), translate((-30, 0), mousepos), 10)
    # down
    pygame.draw.line(window, crosshairColor, translate((0, -10), mousepos), translate((0, -30), mousepos), 10)
    # center
    pygame.draw.circle(window, crosshairColor, mousepos, 5)
    
    # HUD
    pygame.draw.rect(window, gray, HUD_rect)
    pygame.draw.circle(window, black, (30, 50), 20)
    pygame.draw.rect(window, black, bullet_rect)
    HUD_text.render_to(window, (130, 30), str(ammo))
    HUD_text.render_to(window, (230, 25), str(kills) + "/" + str(enemies_amount) + " kills")
    HUD_text.render_to(window, (680, 10), "Health: ")
    pygame.draw.rect(window, red, healthbarRed)
    healthbarGreen.width = round((health / maxHealth) * 120)
    pygame.draw.rect(window, green, healthbarGreen)
    
    pygame.display.flip()
    clock.tick(30)

if state == 1:
    window.fill(white)
    winning.play()
    
    HUD_text.render_to(window, (50, 50), "YOU WIN!")
    HUD_text.render_to(window, (50, 150), "Total completion time: " + str(finalTime) + " seconds")
    
    HUD_text.render_to(window, (50, 650), "Remaining health: " + str(health))
elif state == 2:
    window.fill(red)
    death.play()
    
    HUD_text.render_to(window, (50, 50), "YOU DIED!")
    HUD_text.render_to(window, (50, 150), "Total death time: " + str(finalTime) + " seconds")
if state != 0:
    HUD_text.render_to(window, (50, 250), "Shots fired: " + str(shots))
    HUD_text.render_to(window, (50, 350), "Critical Hits: " + str(crits))
    HUD_text.render_to(window, (50, 450), "Collected Ammo Boxes: " + str(collected))
    HUD_text.render_to(window, (50, 550), "Kills: " + str(kills))
    
    pygame.display.flip()
    pause()