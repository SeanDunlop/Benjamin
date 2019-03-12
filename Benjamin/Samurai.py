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
        self.downPressed = False
        self.upPressed = False
        self.moveDirection = 1
        self.speed = 10


    def loadAnimations(self):
        self.load_animation('Samurai_idle_left', 15)
        self.load_animation('Samurai_idle_right', 15)
        self.load_animation('Samurai_idle_forward', 15)
        self.load_animation('Samurai_idle_backwords', 15)

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
        if direction == d.DOWN:
            self.direction = d.DOWN
            self.setAnimation('Samurai_idle_forward')
            self.group.empty()
            self.group.add(self.currentAnimation)
        if direction == d.UP:
            self.direction = d.UP
            self.setAnimation('Samurai_idle_backwords')
            self.group.empty()
            self.group.add(self.currentAnimation)

    def update(self):
        super().update()
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("A Pressed")
                    print("GO LEFT")
                    self.fixDirection(d.LEFT, True)
                if event.key == pygame.K_d:
                    print("D Pressed")
                    print("GO RIGHT")
                    self.fixDirection(d.RIGHT, True)
                if event.key == pygame.K_s:
                    print("S Pressed")
                    print("GO DOWN")
                    self.fixDirection(d.DOWN, True)
                if event.key == pygame.K_w:
                    print("W Pressed")
                    print("GO UP")
                    self.fixDirection(d.UP, True)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    print("A Released")
                    self.fixDirection(d.LEFT, False)
                if event.key == pygame.K_d:
                    print("D Released")
                    self.fixDirection(d.RIGHT, False)
                if event.key == pygame.K_s:
                    print("S Released")
                    self.fixDirection(d.DOWN, False)
                if event.key == pygame.K_w:
                    print("W Released")
                    self.fixDirection(d.UP, False)
    def fixDirection(self, direction, down):
        if down == True:
            self.setDirection(direction)
            if direction == d.LEFT:
                self.leftPressed = True
            if direction == d.RIGHT:
                self.rightPressed = True
            if direction == d.DOWN:
                self.downPressed = True
            if direction == d.UP:
                self.upPressed = True
        if down == False:
            if direction == d.LEFT:
                self.leftPressed = False
                if self.rightPressed == True:
                    self.setDirection(d.RIGHT)
            if direction == d.RIGHT:
                self.rightPressed = False
                if self.leftPressed == True:
                    self.setDirection(d.LEFT)
            if direction == d.UP:
                self.upPressed = False
                if self.downPressed == True:
                    self.setDirection(d.DOWN)
            if direction == d.DOWN:
                self.downPressed = False
                if self.upPressed == True:
                    self.setDirection(d.UP)
        if self.leftPressed == False:
            if self.rightPressed == False:
                if self.upPressed == False:
                    if self.downPressed == False:
                        self.setDirection(d.down)