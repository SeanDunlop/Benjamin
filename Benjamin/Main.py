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
import DarkBricks

SIZE = WIDTH, HEIGHT = 1312, 670 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 24 #Frames per second

def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    d = directions.directions

    Terrain = Entity.EntityGroup(screen)
    players = Entity.EntityGroup(screen)
    background = Entity.EntityGroup(screen)
    
    level0 = [
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWW            WWWWW",
    "WWWWW            WWWWW",
    "WWWWW S          WWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW"
        ]

    level1 = [
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWW      WWWWWWW",
    "W                    W",
    "W                    W",
    "W   WWWWWW    WWWWWWWW",
    "WW             WWWWWWW",
    "WWW              SWWWW",
    "WWWW           WWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW"
        ]

    levels = [level0, level1]

    Terrain, players, background, sam = loadMap(levels[0], screen)

    
    

    clock = pygame.time.Clock()
 
    Terrain.reverse() #LOOK I REVERSED IT
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
        if(sam.LEVEL == 1):
            Terrain, players, background, sam = loadMap(levels[0], screen)
        if(sam.LEVEL == 2):
            Terrain, players, background, sam = loadMap(levels[1], screen)
        pygame.display.update()
        clock.tick(FPS)
def loadMap(level, screen):
    Terrain = Entity.EntityGroup(screen)
    players = Entity.EntityGroup(screen)
    background = Entity.EntityGroup(screen)

    x = y = -48
    samx = samy = 0
    for row in level:
        for col in row:
            if col == "W":
                Bricks.build(x, y, Terrain)
            if col == "S":
                samx = x
                samy = y
            if col == "V":
                Bricks.build(x, y-32, Terrain)
            x += 64
        y += 64
        x = -48

    DarkBricks.build(0,0,background)
    sam = Samurai.Samurai(samx, samy, Collider.Collider(Terrain))
    sam.setDirection(directions.directions.LEFT)
    players.add(sam)
    return Terrain, players, background, sam
if __name__ == '__main__':
    main()
