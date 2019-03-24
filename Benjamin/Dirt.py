
import pygame
import Entity
import Platform

class Dirt(Platform.Platform):
    def __init__(self, x, y, group):

        super().__init__(x ,y, group, 64, 64)
        self.loadImages()
        self.changeAnimation('Dirt')

    def loadImages(self):
        self.load_animation('Dirt',1)
    def update(self):
        return


def build(x, y, group):
    p = Dirt(x,y,group)