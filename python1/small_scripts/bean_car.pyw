"""
LESSON: 3.5 - Mouse & Keyboard
TECHNIQUE 4: Move With Arrow Keys
DEMO
"""

import pygame, tsk
pygame.init()

window = pygame.display.set_mode([800, 600])

bg_color = (30, 190, 30)
track_color = (120, 110, 110)
outline_color = (220, 220, 220)

car_rect = pygame.Rect(350, 80, 40, 30)
track_rect = pygame.Rect(50, 50, 700, 500)
inner_rect = pygame.Rect(150, 150, 500, 300)

car_speed = 0.1
friction = 0.01
car_x = 350.0
car_y = 80.0
car_vx = 0.0
car_vy = 0.0
car_max_v = 20
car_min_v = car_max_v * -1

clock = pygame.time.Clock()

# --- Main loop --- #
drawing = True
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # --- Character Movement ---
    if tsk.is_key_down(pygame.K_LEFT):
        car_vx -= car_speed
    if tsk.is_key_down(pygame.K_RIGHT):
        car_vx += car_speed
    if tsk.is_key_down(pygame.K_UP):
        car_vy -= car_speed
    if tsk.is_key_down(pygame.K_DOWN):
        car_vy += car_speed
        
    if car_vx > car_max_v:
        car_vx = car_max_v
    if car_vx < car_min_v:
        car_vx = car_min_v
    
    if car_vy > car_max_v:
        car_vy = car_max_v
    if car_vy < car_min_v:
        car_vy = car_min_v
        
    if car_vx > -0.1 and car_vx < 0.1:
        car_vx = 0
    elif car_vx > 0:
        car_vx = car_vx - friction
        if car_vx < 0:
            car_vx = 0
    elif car_vx < 0:
        car_vx = car_vx + friction
        if car_vx > 0:
            car_vx = 0
    
    if car_vy > -0.1 and car_vy < 0.1:
        car_vy = 0
    elif car_vy > 0:
        car_vy -= friction
        if car_vy < 0:
            car_vy = 0
    elif car_vy < 0:
        car_vy += friction
        if car_vy > 0:
            car_vy = 0
    
    car_x += car_vx
    car_y += car_vy
    car_rect.x = int(car_x)
    car_rect.y = int(car_y)


    # --- Draw --- #
    window.fill(bg_color)
    pygame.draw.ellipse(window, track_color, track_rect)
    pygame.draw.ellipse(window, outline_color, track_rect, 5)
    pygame.draw.ellipse(window, bg_color, inner_rect)
    pygame.draw.ellipse(window, outline_color, inner_rect, 5)
    pygame.draw.line(window, outline_color, (400, 50), (400, 150), 10)
    pygame.draw.ellipse(window, (230, 0, 20), car_rect)
    pygame.draw.ellipse(window, (20, 0, 0), car_rect, 3)
    pygame.display.flip()

    clock.tick(30)
