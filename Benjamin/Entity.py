import Visual
import pygame

class EntityGroup():

    def __init__(self, screen):
        self.entities = []
        self.screen = screen

    def add(self, entity):
        self.entities.append(entity)

    def updateAll(self):
        for e in self.entities:
            e.update()

    def getAll(self):
        return self.entities

    def drawAll(self):
        for e in self.entities:
            e.group.draw(self.screen)


class Entity():
    def __init__(self, x, y, width, height):
        super(Entity, self).__init__()
        self.animations = {}
        self.xpos = x
        self.ypos = y
        self.currentAnimation = None
        self.rect = pygame.Rect(self.xpos,self.ypos,width,height)
        self.group = pygame.sprite.Group()

    def load_animation(self, name, count):
        self.animations[name] = Visual.Animation(name, count, self.xpos, self.ypos, self.rect)
        return self.animations[name]

    def move(self, dx, dy): 
        self.xpos  = self.xpos + dx
        self.ypos = self.ypos + dy
        self.rect = self.rect.move(dx, dy)
        for key, a in self.animations.items():
            a.move(dx, dy)

    def changeHeight(self, height):
        if(height != self.rect.height):
            print("CHANGED HEIGHT")
            #oldHeight = self.rect.height
            #dH = (oldHeight - height)
            bot = self.rect.bottom
            self.rect.height = height
            self.rect.bottom = bot
            #self.move(0, dH)
            for key, a in self.animations.items():
                a.rect.height = height
                a.rect.bottom = bot
    def moveTo(self, x, y):
        dx = x - self.xpos
        dy = y - self.ypos
        self.move(dx, dy)

    def setAnimation(self, name):
        self.currentAnimation = self.animations[name]

    def changeAnimation(self, name):
        if(self.animations[name] != self.currentAnimation):
            self.setAnimation(name)
            self.group.empty()
            self.group.add(self.currentAnimation)

    def update(self):
        self.animations[self.currentAnimation.name].nextFrame()
    
