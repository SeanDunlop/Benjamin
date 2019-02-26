
import pygame
 
 
SIZE = WIDTH, HEIGHT = 600, 400 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 5 #Frames per second
 
KEY_W = 119
KEY_A = 97
KEY_S = 115
KEY_D = 100

def getImageByName(name, count):
    return pygame.image.load(name + str(count) + '.png')



class Animation(pygame.sprite.Sprite):
    def __init__(self, name, count):
        super(Animation, self).__init__()
        self.count = count
        self.name = name
        self.image = getImageByName(name, 0)
        self.images = []
        self.loadImages()
        self.rect = pygame.Rect(0,0,32, 32)
        self.index = 0
        self.frameCount = 0;
        
    def loadImages(self):
        for i in range(self.count):
            self.images.append(getImageByName(self.name, self.count))

    def nextFrame(self):
        self.frameCount +=1
        if(self.frameCount >= 2):
            self.index += 1
            if(self.index> self.count):
                self.index = 0
            self.image = self.images[self.index]
            self.frameCount = 0

    def nextFrame2(self):
        self.frameCount = (self.frameCount + 1)%2
        if(self.frameCount == 0):
            self.index = (self.index + 1) % self.count
            self.image = self.images[self.index]

class Entity():
    def __init__(self):
        super(Entity, self).__init__()
        self.xpos = 0
        self.ypos = 0
        self.animations = []
        self.currentAnimation = 0
        self.rect = pygame.Rect(0,0,32,32)
        
    def load_animation(self, name, count):
        self.animations.append(Animation(name, count))
    
    def move(dx, dy):
        self.animations[0].rect.move(dx, dy)

    def setAnimation(self, newIndex):
        self.currentAnimation = newIndex
    def update(self):
        self.animations[self.currentAnimation].nextFrame2()

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        
        self.images = []
        self.images.append(pygame.image.load('sunflower_00.png'))
        self.images.append(pygame.image.load('sunflower_01.png'))
        self.images.append(pygame.image.load('sunflower_02.png'))
        self.images.append(pygame.image.load('sunflower_03.png'))
        self.images.append(pygame.image.load('sunflower_04.png'))
        self.images.append(pygame.image.load('sunflower_05.png'))
        self.images.append(pygame.image.load('sunflower_06.png'))
        self.images.append(pygame.image.load('sunflower_07.png'))
        self.images.append(pygame.image.load('sunflower_08.png'))
        self.images.append(pygame.image.load('sunflower_09.png'))
        self.images.append(pygame.image.load('sunflower_10.png'))
        self.images.append(pygame.image.load('sunflower_11.png'))
        self.images.append(pygame.image.load('sunflower_12.png'))
        self.images.append(pygame.image.load('sunflower_13.png'))
        self.images.append(pygame.image.load('sunflower_14.png'))
        self.images.append(pygame.image.load('sunflower_15.png'))
        self.images.append(pygame.image.load('sunflower_16.png'))
        self.images.append(pygame.image.load('sunflower_17.png'))
 
        self.index = 0
 
        self.image = self.images[self.index]
 
        self.rect = pygame.Rect(300, 300, 32, 32)
 
    def update(self):

        keys = pygame.key.get_pressed()

        if (keys[KEY_W]):
            self.rect = self.rect.move(0,-2)
        if(keys[KEY_D]):
            self.rect = self.rect.move(2,0)
        if(keys[KEY_S]):
            self.rect = self.rect.move(0,2);
        if(keys[KEY_A]):
            self.rect = self.rect.move(-2, 0)
                        

        self.index += 1
 
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
 
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    #entity1 = Entity()
    #entity1.load_animation('sunflower_', 17)
    #entity1.setAnimation(0)
    my_group = pygame.sprite.Group()
    #my_group.add(entity1.animations[0])
    #my_group.add(my_sprite.animations[0])
    
    ani = Animation('sunflower_', 17)
    my_group.add(ani)
    clock = pygame.time.Clock()
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        my_group.update()
        ani.nextFrame2()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
 
if __name__ == '__main__':
    main()
