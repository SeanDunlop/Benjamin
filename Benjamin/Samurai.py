import pygame
import Visual
import Entity
import directions

KEY_W = 119
KEY_A = 97
KEY_S = 115
KEY_D = 100
d = directions.directions


class Samurai(Entity.Entity):
    def __init__(self, group):

        super().__init__()
        self.direction = 1
        self.group = group # the group of sprites which this object's animations belong to
        self.leftPressed = False
        self.rightPressed = False
        self.moveDirection = 1
        self.speed = 10


    def loadAnimations(self):
        self.load_animation('Samurai_idle_left', 15)
        self.load_animation('Samurai_idle_right', 15)
        self.load_animation('Samurai_idle_forward', 15)


    def setDirection(self, direction): # set the direction of the samurai

        if direction == d.RIGHT:
            self.direction = d.RIGHT
            self.setAnimation('Samurai_idle_right')
            self.group.empty()
            self.group.add(self.currentAnimation)
        if direction == d.LEFT:
            self.direction = d.LEFT
            self.setAnimation('Samurai_idle_left')
            self.group.empty()
            self.group.add(self.currentAnimation)
        if direction == d.NONE:
            self.direction = d.NONE
            self.setAnimation('Samurai_idle_front')
            self.group.empty()
            self.group.add(self.currentAnimation)

    def update(self):
        super().update()
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("A Pressed")
                    if self.direction == d.RIGHT:
                        print("GO LEFT")
                        #self.setDirection('left')
                        self.leftPressed = True
                if event.key == pygame.K_d:
                    print("D Pressed")
                    if self.direction == d.LEFT:
                        print("GO RIGHT")
                        #self.setDirection('right')
                        self.rightPressed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("A Released")
                    self.leftPressed = False
                if event.key == pygame.K_d:
                    print("D Released")
                    self.rightPressed = False
    

    def fixDirection(self):
        if 