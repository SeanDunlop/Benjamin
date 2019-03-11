import Visual
import pygame
class Entity():
    def __init__(self):
        super(Entity, self).__init__()
        self.xpos = 0
        self.ypos = 0
        self.animations = {}
        self.currentAnimation = None
        self.rect = pygame.Rect(0,0,32,32)
        
    def load_animation(self, name, count):
        #self.animations.append(Visual.Animation(name, count))
        self.animations[name] = Visual.Animation(name, count)
        return self.animations[name]
    def move(dx, dy):
        self.animations[0].rect.move(dx, dy)

    def setAnimation(self, name):
        self.currentAnimation = self.animations[name]
    def update(self):
        a = 1
        #self.animations[self.currentAnimation].update()
  
