import pygame
import Visual
import Entity
import directions
import sys

false = False
true = True

KEY_W = 119
KEY_A = 97
KEY_S = 115
KEY_D = 100
d = directions.directions


class Samurai(Entity.Entity):
    def __init__(self, x, y, collider):

        super().__init__(x ,y, 64, 64)

        
        self.maxJumps = 30
        self.jumps = self.maxJumps
        self.speed = 8
        self.jumpPower = -13

        self.jumpPressed = False
        self.leftPressed = False
        self.rightPressed = False
        self.downPressed = False
        self.upPressed = False
        self.EXIT = False

        self.moveDirection = d.none

        self.yVelo = 0
        self.xVelo = 0

        self.grounded = False
        self.moving = False
        self.direction = d.none

        self.collider = collider

        self.loadAnimations()
        self.changeAnimation('Samurai_idle_right')
        
        
    def loadAnimations(self):
        self.load_animation('Samurai_idle_left', 15)
        self.load_animation('Samurai_idle_right', 15)
        self.load_animation('Samurai_idle_forward', 15)
        self.load_animation('Samurai_idle_backwords', 15)
        self.load_animation('Samurai_falling_left', 4)
        self.load_animation('Samurai_falling_right', 4)
        self.load_animation('Samurai_run_left', 8)
        self.load_animation('Samurai_run_right', 8)

    def setMoveDirection(self, direction):
        self.moveDirection = direction
    def fixAnimation(self):

        if (self.grounded == True):
            if self.moving == True:
                if self.moveDirection == d.left:
                    self.changeAnimation('Samurai_run_left')
                if self.moveDirection == d.right:
                    self.changeAnimation('Samurai_run_right')
            if self.moving == False:
                if self.direction == d.left:
                    self.changeAnimation('Samurai_idle_left')
                if self.direction == d.right:
                    self.changeAnimation('Samurai_idle_right')

        if (self.grounded == False):
            if self.direction == d.left:
                self.changeAnimation('Samurai_falling_left')
            if self.direction == d.right:
                self.changeAnimation('Samurai_falling_right')
                
    def setDirection(self, direction): # set the direction of the samurai

        self.direction = direction
        
    def jump(self):

        self.yVelo = self.jumpPower
        self.grounded = False
        

    def update(self):
        super().update()
        self.updateKeys()
        self.doMovement()
        self.fixAnimation()

    def doMovement(self):

        dir = 0
        if self.moveDirection == d.LEFT:
            dir = -1
        if self.moveDirection == d.RIGHT:
            dir = 1
        self.xVelo = self.speed * dir

        
        
        groundedFlag = False
        if(self.xVelo != 0):
            self.move(self.xVelo, 0)#move in x first
            if self.collider.doCollision(self, self.xVelo, 0):
                groundedFlag = True

        if(self.yVelo != 0):
            self.move(0, self.yVelo)#then move in y
            if self.collider.doCollision(self, 0,self.yVelo):
              groundedFlag = True

        self.grounded = groundedFlag
        
        if(self.grounded == False):
            self.yVelo += 1 #apply gravity
        if(self.grounded == True):
                self.jumps = self.maxJumps
                #self.yVelo = 0
        print(self.grounded)

        if(self.yVelo >15):
            self.yVelo = 15
    
    def updateKeys(self):
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.fixDirection(d.LEFT, True)
                if event.key == pygame.K_d:
                    self.fixDirection(d.RIGHT, True)
                if event.key == pygame.K_s:
                    a=1
                    #self.fixDirection(d.DOWN, True)
                if event.key == pygame.K_w:
                    a=1
                    #self.fixDirection(d.UP, True)
                if event.key == pygame.K_SPACE:
                    if (self.jumpPressed == False):
                        if(self.jumps > 0):
                            self.jump()
                            self.jumps = self.jumps - 1
                    self.jumpPressed = True
                if event.key == pygame.K_ESCAPE:
                    self.EXIT = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.fixDirection(d.LEFT, False)
                if event.key == pygame.K_d:
                    self.fixDirection(d.RIGHT, False)
                if event.key == pygame.K_s:
                    a=1
                    #self.fixDirection(d.DOWN, False)
                if event.key == pygame.K_w:
                    a=1
                    #self.fixDirection(d.UP, False)
                if event.key == pygame.K_SPACE:
                    self.jumpPressed = False

    
    
    def fixDirection(self, direction, down):
        if down == True:
            self.setDirection(direction)
            
            if direction == d.LEFT:
                self.leftPressed = True
                self.setMoveDirection(direction)
            if direction == d.RIGHT:
                self.rightPressed = True
                self.setMoveDirection(direction)
            if direction == d.DOWN:
                self.downPressed = True
            if direction == d.UP:
                self.upPressed = True
        if down == False:
            if direction == d.LEFT:
                self.leftPressed = False
                self.setMoveDirection(d.NONE)
                if self.rightPressed == True:
                    self.setDirection(d.RIGHT)
                    self.setMoveDirection(d.RIGHT)
            if direction == d.RIGHT:
                self.rightPressed = False
                self.setMoveDirection(d.NONE)
                if self.leftPressed == True:
                    self.setDirection(d.LEFT)
                    self.setMoveDirection(d.LEFT)
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
                        a = 1
        if self.moveDirection == d.none:
            self.moving = False
        else:
            self.moving = True