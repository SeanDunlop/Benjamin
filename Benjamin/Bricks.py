import pygame
import Entity
import Platform

class Bricks(Platform.Platform):
    def __init__(self, x, y, group):

        super().__init__(x ,y, group, 64, 64)
        self.loadImages()
        self.changeAnimation('Bricks')

    def loadImages(self):
        self.load_animation('Bricks',1)
    def update(self):
        return


def build(x, y, group):
    p = Bricks(x,y,group)