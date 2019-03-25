import pygame
import Entity
import Platform

class Scull(Platform.Platform):
    def __init__(self, x, y, group):

        super().__init__(x ,y, group, 64, 64)
        self.loadImages()
        self.changeAnimation('Scull')

    def loadImages(self):
        self.load_animation('Scull',1)
    def update(self):
        return


def build(x, y, group):
    return Scull(x,y,group)