import pygame
import Entity
import Platform

class Background(Platform.Platform):
    def __init__(self, x, y, group):

        super().__init__(x ,y, group, 64, 64)
        self.loadImages()
        self.changeAnimation('Background')

    def loadImages(self):
        self.load_animation('Background',1)
    def update(self):
        return


def build(x, y, group):
    p = Background(x,y,group)
