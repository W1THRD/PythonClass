
import pygame, random

pygame.init()
w = pygame.display.set_mode((500, 500))

bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
circle_x = 250
circle_y = 250

triangle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
triangle_x = 150
triangle_y = 250

lines = []
line_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
for i in range(40):
    lines.append((random.randint(0, 500), random.randint(0, 500)))
    
f = 0

clock = pygame.time.Clock()
drawing = True
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
    
    if(random.randint(1, 20) != 1):
        w.fill(bg_color)
        
    if(random.randint(1, 20) == 1):
        bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        triangle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        line_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
    if(random.randint(1, 20) == 2):
        del lines[:]
        for i in range(40):
            lines.append((random.randint(0, 500), random.randint(0, 500)))
   
        
    for i in range(40):
        if i == 1:
            pygame.draw.line(w, line_color, lines[len(lines)-1], lines[i], 5)
        if i == 40:
            pygame.draw.line(w, line_color, lines[i-1], lines[0], 5)
        else:
            pygame.draw.line(w, line_color, lines[i-1], lines[i], 5)
    
    for i in range(40):
        x = random.randint(-1, 1) * 10
        y = random.randint(-1, 1) * 10
        lines[i-1] = (lines[i-1][0] + x, lines[i-1][1] + y)
    
    pygame.draw.circle(w, circle_color, (circle_x, circle_y), 20)
    pygame.draw.circle(w, circle_color, (circle_x - 40, circle_y), 20)
    pygame.draw.circle(w, circle_color, (circle_x + 40, circle_y), 20)
    pygame.draw.circle(w, circle_color, (circle_x, circle_y - 40), 20)
    pygame.draw.circle(w, circle_color, (circle_x, circle_y + 40), 20)
    pygame.draw.circle(w, circle_color, (circle_x - 40, circle_y - 40), 20)
    pygame.draw.circle(w, circle_color, (circle_x + 40, circle_y + 40), 20)
    pygame.draw.circle(w, circle_color, (circle_x - 40, circle_y + 40), 20)
    pygame.draw.circle(w, circle_color, (circle_x + 40, circle_y - 40), 20)
    
    triangle = [(triangle_x, triangle_y), (triangle_x + 80, triangle_y), (triangle_x + 80, triangle_y - 90)]
    pygame.draw.polygon(w, triangle_color, triangle)
    
    tx = random.randint(-500, 500)
    ty = random.randint(-500, 500)
    triangle2 = [(triangle_x + tx, triangle_y + ty), (triangle_x + 80 + tx, triangle_y + ty), (triangle_x + 80 + tx, triangle_y - 90 + ty)]
    pygame.draw.polygon(w, triangle_color, triangle2)
    
    
    pygame.display.flip()
    clock.tick(30)
    
    if(random.randint(0, 1) == 1):
        circle_x += 10
    else:
        circle_x -= 10 
    if(random.randint(0, 1) == 1):
        circle_y += 10
    else:
        circle_y -= 10
        
    if(random.randint(0, 1) == 1):
        triangle_x += 30
    else:
        triangle_x -= 30 
    if(random.randint(0, 1) == 1):
        triangle_y += 30
    else:
        triangle_y -= 30
        
    f += 1.0
