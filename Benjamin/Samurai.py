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

        if direction == d.RIGHT:
            self.direction = d.RIGHT
            #self.changeAnimation('Samurai_idle_right')
        if direction == d.LEFT:
            self.direction = d.LEFT
            #self.changeAnimation('Samurai_idle_left')
        if direction == d.DOWN:
            self.direction = d.DOWN
            #self.changeAnimation('Samurai_idle_forward')
        if direction == d.UP:
            self.direction = d.UP
            #self.changeAnimation('Samurai_idle_backwords')
        if direction == d.NONE:
            self.direction = d.NONE
        
    def jump(self):

        self.yVelo = self.jumpPower
        self.grounded = False
        

    def update(self):
        super().update()
        self.updateKeys()
        self.doOtherMovement()
        self.fixAnimation()
    def doOtherMovement(self):

        dir = 0
        if self.moveDirection == d.LEFT:
            dir = -1
        if self.moveDirection == d.RIGHT:
            dir = 1
        self.xVelo = self.speed * dir

        if(self.grounded == False):
            if (self.yVelo < 10):
                self.yVelo += 1 #apply gravity
        if(self.grounded == True):
            self.jumps = self.maxJumps
            self.yVelo = 0
            print("grounded")

        #self.grounded = False

        if(self.xVelo != 0):
            self.move(self.xVelo, 0)#move in x first
            self.collider.doCollision(self, self.xVelo, 0)

        if(self.yVelo != 0):
            self.move(0, self.yVelo)#then move in y
            self.collider.doCollision(self, 0,self.yVelo)


    def doMovement(self):

        dir = 0
        if self.moveDirection == d.LEFT:
            dir = -1
        if self.moveDirection == d.RIGHT:
            dir = 1
        self.xVelo = self.speed * dir

        if(self.grounded == False):
            self.yVelo = self.yVelo + 1
        if(self.grounded == True):
            self.jumps = self.maxJumps
            self.yVelo = 0

        top, bottom, left, right = self.collider.checkAll(self, self.xVelo, self.yVelo)
        
        if (bottom == True and self.grounded == False):#Collided upwards
            self.yVelo = 0
            print("Collided Upwards")
        
        
        if (top == True):#Collided downwards
            self.yVelo = 0
            self.grounded = True
            print("Collided Downwards")
            falling == False
        if (top == False):
            if(falling == True):
                self.grounded = False
            falling == True

        if (right == True):#Collided on the left
            self.xVelo = 0
            print("Collided on left")
        if (left == True):#Collided on the player
            self.xVelo = 0
            print("Collided on right")
        
        self.move(self.xVelo, self.yVelo)

    def updateKeys(self):
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.fixDirection(d.LEFT, True)
                if event.key == pygame.K_d:
                    self.fixDirection(d.RIGHT, True)
                if event.key == pygame.K_s:
                    self.fixDirection(d.DOWN, True)
                if event.key == pygame.K_w:
                    self.fixDirection(d.UP, True)
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
                    self.fixDirection(d.DOWN, False)
                if event.key == pygame.K_w:
                    self.fixDirection(d.UP, False)
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