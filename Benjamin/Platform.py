import pygame
import Entity

class Platform(Entity.Entity):
    def __init__(self, x, y, group):

        super().__init__(x ,y, 32, 32)
        self.loadImages()
        self.changeAnimation('Platform')
        self.height = 32
        self.width = 32
        group.add(self)
    def loadImages(self):
        self.load_animation('Platform',1)
    def update(self):
        a = 1


def build(x, y, group):
    p = Platform(x,y,group)