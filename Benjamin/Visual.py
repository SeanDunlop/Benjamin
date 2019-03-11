import pygame

def getImageByName(name, count):
    filename = getPath(name, count)
    return pygame.image.load(filename)
def getPath(name, index):
    filename = name + '/' + name + str(index) + '.png'
    return filename
class Animation(pygame.sprite.Sprite):
    def __init__(self, name, count):
        super(Animation, self).__init__()
        self.count = count
        self.name = name
        #super().image = getImageByName(name, 0)
        self.images = []
        self.imagepaths = []
        self.index = 0
        self.loadImages()
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0,0,32, 32)
        self.frameCount = 0
        
    def loadImages(self):
        #self.images.append(getImageByName(self.name, self.index))
        for i in range(1, self.count + 1):
            self.images.append(getImageByName(self.name, i))
            self.imagepaths.append(getPath(self.name, i))
    def otherUpdate(self):
        self.frameCount += 1
        if self.frameCount == 3:
            self.nextFrame()
            self.frameCount = 0
    def update(self):
        self.frameCount += 1
        if self.frameCount == 3:
            self.nextFrame()
            self.frameCount = 0
    def nextFrame(self):
        #print("heyyy")
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #print(self.imagepaths[self.index])

    def draw(self):
        pygame.sprite.Sprite.draw(self)

