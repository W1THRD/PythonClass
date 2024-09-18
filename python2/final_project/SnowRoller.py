# SNOW ROLLER: MAIN FILE
# Documentation link: https://docs.google.com/document/d/1tFVGDH__pBo6-1TWrTlzSx7WaFAuZUD75sGkEQtDjQk/edit?usp=sharing
# INSTRUCTIONS:
# - Arrow keys to move
# - Press P to pause
# - Don't touch trees or rocks
# - Use campfires to shrink

# import modules
import pygame, objects, utils, scroll, menu

# initiate window
pygame.init()
win_size = (500, 500)
window = pygame.display.set_mode(win_size)

# debug stuff & UI
# uncomment this next line to enable debug text:
#debugger = utils.Debugger((0, 245, 0), 22)
UI = menu.UIManager()
counter = menu.ScoreCounter(450) 

# create player & scroller
player = None
scroller = None
# restarts main game
def restart():
    global player, scroller
    player = objects.Player((250, 120))
    scroller = scroll.Scroller((0, 0), win_size)
restart()

# start the timers
c = pygame.time.Clock()
running = True

# main loop
while running:
    # event loop
    for event in pygame.event.get():
        # quit the game if the player wants to
        if event.type == pygame.QUIT:
            running = False
        # notify the UI manager if the user clicked their mouse or pressed P
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if UI.state != 1:
                UI.clicked(pygame.mouse.get_pos(), restart)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                UI.pause()
    
    # main game
    if UI.state == 1:
        UI._oldstate = 1
        
        # update the player & scroller
        update_time = c.get_time()
        if scroller.failcode == 0:
            player.update(update_time, utils.control(utils.horizontal_mode))
        #uncomment this next line to enable debug text for failcode:
        #debugger.add("Failcode: " + str(scroller.failcode))
        scroller.update(update_time, player, UI, utils.control(utils.vertical_mode))
        
        # draw everything
        window.fill((228, 228, 228))
        scroller.drawDetails(window)
        player.draw(window)
        scroller.drawObjects(window)
        counter.draw(window, player, win_size)
        scroller.drawFailText(window, player, win_size)
        # uncomment this next line to draw debugger:
        #debugger.draw(window)
    else:
        UI.draw(window, win_size, c.get_time())
    
    # update the screen and wait
    pygame.display.flip()
    c.tick(30)