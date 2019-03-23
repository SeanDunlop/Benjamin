import pygame
import Visual
import Entity
import Samurai
import directions
import Platform
import Collider

SIZE = WIDTH, HEIGHT = 1200, 400 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 60 #Frames per second

def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    d = directions.directions

    #Samurai_group = pygame.sprite.Group()
    #Platform_group = pygame.sprite.Group()

    

    platform2 = Platform.Platform( 60, 250)
    platform1 = Platform.Platform( 150, 150)
    platforms = Entity.EntityGroup(screen)
    players = Entity.EntityGroup(screen)

    platforms.add(platform1)
    platforms.add(platform2)


    sam = Samurai.Samurai(50, 50, Collider.Collider(platforms))
    sam.loadAnimations()
    players.add(sam)
    sam.setDirection(d.LEFT)

    clock = pygame.time.Clock()
 
    while True:
        
 
        #Samurai_group.update()
        screen.fill(BACKGROUND_COLOR)
        #Samurai_group.draw(screen)#draw sam's animations
        #Platform_group.draw(screen)
        #collider.checkAll()
        #sam.update()#update sam object
        platforms.updateAll()
        platforms.drawAll()
        players.updateAll()
        players.drawAll()
        if(sam.EXIT):
            break
        pygame.display.update()
        clock.tick(FPS)
 
if __name__ == '__main__':
    main()
