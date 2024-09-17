# DO NOT RUN THIS FILE!
# This is just a library for the game
# To play the game, go to tile_game.py

import plot

symbols = {"#": (0, 0, 0),
          " ": (255, 255, 255),
          "X": (255, 0, 0),
          "G": (80, 238, 80)
}

def collideLevel(player):
    if player.x <= 50:
        return(1)
    if player.x + player.width >= 450:
        return(2)
    if player.y <= 50:
        return(3)
    if player.y + player.height >= 450:
        return(4)
    
    return(0)

levels = []

# level 1
levels.append([["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
               ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
               ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
               ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
               ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
               ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
               ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
               ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
               ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
               ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]])
              