import pygame
import Visual
import Entity
import Samurai
import directions
import Platform
import Collider
import Bricks
import Dirt
import Background

SIZE = WIDTH, HEIGHT = 1280, 640 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 60 #Frames per second

def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    d = directions.directions

    Terrain = Entity.EntityGroup(screen)
    players = Entity.EntityGroup(screen)
    background = Entity.EntityGroup(screen)
    
    level = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W       WWWWWWW    W",
    "W         WWW      W",
    "W           V      W",
    "WWWWW   WWWWWWWWW  W",
    "W               W  W",
    "W               W  W",
    "W      WWWW     W  W",
    "WS    WWWWWW       W",
    "DDDDDDDDDDDDDDDDDDDD"
        ]
    x = y = 0
    samx = samy = 0
    for row in level:
        for col in row:
            if col == "W":
                Bricks.build(x, y, Terrain)
            if col == "D":
                Dirt.build(x, y, Terrain)
            if col == "S":
                samx = x
                samy = y
            if col == "V":
                Bricks.build(x, y-48, Terrain)
            x += 64
        y += 64
        x = 0
#    for x in range(0, 30):
#        Dirt.build(64*x, 368, Terrain)
#
#
#    for x in range(15, 20):
#        Bricks.build(64*x, 208, Terrain)
#    
#    for y in range(1, 5):
#        Bricks.build(672, 64*y, Terrain)
#
#    for y in range(4, 8):
#        Bricks.build(0, 64*y, Terrain)
#
#    for x in range(0, 25):
#        Background.build(128*x, 0, background)
#
    sam = Samurai.Samurai(samx, samy, Collider.Collider(Terrain))

    players.add(sam)
    sam.setDirection(d.LEFT)

    clock = pygame.time.Clock()
 
    Terrain.reverse()# LOOK I REVERSED IT

    while True:
        
        screen.fill(BACKGROUND_COLOR)
        background.drawAll()
        background.updateAll()
        Terrain.updateAll()
        Terrain.drawAll()
        
        players.updateAll()
        players.drawAll()
        if(sam.EXIT):
            break
        pygame.display.update()
        clock.tick(FPS)
 
if __name__ == '__main__':
    main()
