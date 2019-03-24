import pygame
import Entity

class Platform(Entity.Entity):
    def __init__(self, x, y, group, width, height):

        super().__init__(x ,y, width, height)
        group.add(self)
    def loadImages(self):
        return
    def update(self):
        return