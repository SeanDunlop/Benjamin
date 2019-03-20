import Visual
import pygame

class EntityGroup():
    def __init__(self):
        self.entities = []
    def add(self, entity):
        self.entities.append(entity)
    def updateAll(self):
        for e in self.entities:
            e.update()
    def getAll(self):
        return self.entities

class Entity():
    def __init__(self, group, x, y):
        super(Entity, self).__init__()
        self.animations = {}
        self.xpos = x
        self.ypos = y
        self.currentAnimation = None
        self.rect = pygame.Rect(self.xpos,self.ypos,32,32)
        self.group = group
    def load_animation(self, name, count):
        #self.animations.append(Visual.Animation(name, count))
        self.animations[name] = Visual.Animation(name, count)
        return self.animations[name]
    def move(self, dx, dy):
        self.xpos  = self.xpos + dx
        self.ypos = self.ypos + dy
        for key, a in self.animations.items():
            a.move(dx, dy)
    def moveTo(self, x, y):
        dx = x - self.xpos
        dy = y - self.ypos
        self.move(dx, dy)
    def setAnimation(self, name):
        self.currentAnimation = self.animations[name]
    def changeAnimation(self, name):
        self.setAnimation(name)
        self.group.empty()
        self.group.add(self.currentAnimation)
    def update(self):
        a = 1
        #self.animations[self.currentAnimation].update()
    
