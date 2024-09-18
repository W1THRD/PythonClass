# ARROW KEYS TO MOVE LEFT AND RIGHT, SPACE TO JUMP

import pygame, plpy, tsk

pygame.init()
win = pygame.display.set_mode((500, 500))

ground = plpy.Box((50, 400), (400, 100), (0, 200, 0))
roof = plpy.Box((50, 330), (200, 2), (0, 200, 0))
wall = plpy.Box((50, 350), (100, 50), (0, 200, 0))
wall2 = plpy.Box((250, 350), (2, 50), (0, 200, 0))
level = plpy.Level([ground, roof, wall, wall2])

player = plpy.Player((300, 350), -14, 5)

c = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # jump controls
                player.jump(level)
    
    # horizontal controls
    if tsk.get_key_pressed(pygame.K_LEFT):
        player.move(level, -1)
    if tsk.get_key_pressed(pygame.K_RIGHT):
        player.move(level, 1)
    
    player.update(level)
    
    win.fill((78, 228, 255))
    level.draw(win)
    player.draw(win)
    
    pygame.display.flip()
    c.tick(30)