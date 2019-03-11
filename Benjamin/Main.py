import pygame
import Visual
import Entity
import Samurai
SIZE = WIDTH, HEIGHT = 600, 400 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 60 #Frames per second

def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    Samurai_group = pygame.sprite.Group()

    sam = Samurai.Samurai(Samurai_group)

    sam.loadAnimations()

    sam.setDirection('left')

    clock = pygame.time.Clock()
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        Samurai_group.update()
        screen.fill(BACKGROUND_COLOR)
        Samurai_group.draw(screen)#draw sam's animations
        sam.update()#update sam object

        pygame.display.update()
        clock.tick(FPS)
 
if __name__ == '__main__':
    main()
