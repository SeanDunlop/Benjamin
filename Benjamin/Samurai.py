import pygame
import Visual
import Entity

KEY_W = 119
KEY_A = 97
KEY_S = 115
KEY_D = 100

class Samurai(Entity.Entity):
    def __init__(self, group):
        super().__init__()
        self.direction = 1
        self.group = group # the group of sprites which this object's animations belong to
    def loadAnimations(self):
        self.load_animation('Samurai_idle_left', 15)
        self.load_animation('Samurai_idle_right', 15)
    def setDirection(self, direction): # set the direction of the samurai
        if direction == 'right':
            self.direction = 1
            self.setAnimation('Samurai_idle_right')
            self.group.empty()
            self.group.add(self.currentAnimation)
        if direction == 'left':
            self.direction = 0
            self.setAnimation('Samurai_idle_left')
            self.group.empty()
            self.group.add(self.currentAnimation)
    def update(self):
        super().update()
        keys = pygame.key.get_pressed()

        if(keys[KEY_D]):
            
            if self.direction == 0:
                print("GO RIGHT")
                self.setDirection('right')

        if(keys[KEY_A]):

            if self.direction == 1:
                print("GO LEFT")
                self.setDirection('left')
        
