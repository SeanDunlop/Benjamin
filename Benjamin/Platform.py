import pygame
import Entity

class Platform(Entity.Entity):
    def __init__(self, x, y, group, width, height):

        super().__init__(x ,y, width, height)
        #self.loadImages()
        #self.changeAnimation('Platform')
        #self.height = 32
        #self.width = 32
        group.add(self)
    def loadImages(self):
        return
        #self.load_animation('Platform',1)
    def update(self):
        return