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
import Scull

SIZE = WIDTH, HEIGHT = 1312, 670 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 60 #Frames per second

def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    d = directions.directions

    Terrain = Entity.EntityGroup(screen)
    players = Entity.EntityGroup(screen)
    background = Entity.EntityGroup(screen)
    
    level = 1

    FRAME = [
    "WWWWWWWWWWWWWWWWWWWWWW",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "WWWWWWWWWWWWWWWWWWWWWW"
        ]

    level0 = [
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWW            WWWWW",
    "WWWWW            WWWWW",
    "WWWWW S        O WWWWW",
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
    "WWWWWWWWW       WWWWWW",
    "W                    W",
    "W                  O W",
    "W   WWWWWW    WWWWWWWW",
    "WW             WWWWWWW",
    "WWW              SWWWW",
    "WWWW           WWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW"
        ]

    level2 = [
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWW    WWW    WWWWWW",
    "WWWWW     W     WWWWWW",
    "WWWWW S   V   O WWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW"
        ]

    level3 = [
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    "W                   WW",
    "W                 O WW",
    "W   WWWWWWWWWWWWWWWWWW",
    "W   W   V      WWWWWWW",
    "W       WWWW   W   WWW",
    "WWWWWWWWWWWWW      WWW",
    "WWWWWWWS    WWWWW  WWW",
    "WWWWWWWWW          WWW",
    "WWWWWWWWWWWWWWWWWWWWWW"
        ]

    levels = [level0, level1, level2, level3]

    Terrain, players, background, sam, scullx, scully = loadMap(levels[0], screen)

    
    

    clock = pygame.time.Clock()
 
    Terrain.reverse() #LOOK I REVERSED IT
    while True:
        
        screen.fill(BACKGROUND_COLOR)
        background.drawAll()
        #background.updateAll()
        Terrain.updateAll()
        Terrain.drawAll()
        
        players.updateAll()
        players.drawAll()
        if(sam.EXIT):
            break
        if(sam.LEVEL != 0):
            Terrain, players, background, sam, scullx, scully = loadMap(levels[sam.LEVEL - 1], screen)
        if(sam.rect.colliderect(pygame.Rect(scullx,scully,64,64))):
            Terrain, players, background, sam, scullx, scully = loadMap(levels[level], screen)
            level += 1
        pygame.display.update()
        clock.tick(FPS)
def loadMap(level, screen):
    Terrain = Entity.EntityGroup(screen)
    players = Entity.EntityGroup(screen)
    background = Entity.EntityGroup(screen)

    x = y = -48
    samx = samy = 0
    scullx = scully = 0
    for row in level:
        for col in row:
            if col == "W":
                Bricks.build(x, y, Terrain)
            if col == "S":
                samx = x
                samy = y
            if col == "V":
                Bricks.build(x, y-48, Terrain)
            if col == "O":
                scullx = x
                scully = y
            x += 64
        y += 64
        x = -48

    DarkBricks.build(0,0,background)
    sam = Samurai.Samurai(samx, samy, Collider.Collider(Terrain))
    sam.setDirection(directions.directions.LEFT)
    scull = Scull.build(scullx, scully, background)
    players.add(sam)
    return Terrain, players, background, sam, scullx, scully
if __name__ == '__main__':
    main()
