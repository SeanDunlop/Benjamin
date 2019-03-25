import pygame
import Visual
import Entity
import directions
import sys
import PlayerInput
#from pynput.keyboard import Key, Controller
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

        
        self.maxJumps = 3
        self.jumps = self.maxJumps
        self.groundAccel = 4
        self.maxSpeed = 12
        self.jumpPower = 14
        self.groundDecel = 8
        self.airAccel = 2
        self.slideAccel = 1

        self.slideHeight = 48
        self.standHeight = 64

        self.jumpPressed = False
        self.leftPressed = False
        self.rightPressed = False
        self.downPressed = False
        self.upPressed = False
        self.dashPressed = False

        self.EXIT = False
        self.LEVEL = 0;
        self.SKULL = False

        self.moveDirection = d.none
        self.frictionToggle = 0

        self.yVelo = 0
        self.xVelo = 0
        
        self.jumpY = 0
        self.jumpX = 0

        self.blocked = False
        self.grounded = False
        self.running = False
        self.direction = d.none
        self.trySliding = False
        self.sliding = False

        self.grabbing = False
        self.grabbed = False
        self.lastGrab = False
        self.grabTime = 60
        self.grabDirection = d.none

        self.maxEnergy = 120
        self.energy = 120
        self.dashing = False

        self.collider = collider

        self.loadAnimations()
        self.changeAnimation('Samurai_idle_right')
        
        #self.controller = PlayerInput.PlayerInput()
        #self.keyboard = Controller()
        #Look a comment
    def loadAnimations(self):
        self.load_animation('Samurai_idle_left', 15)
        self.load_animation('Samurai_idle_right', 15)
        self.load_animation('Samurai_idle_forward', 15)
        self.load_animation('Samurai_idle_backwords', 15)
        self.load_animation('Samurai_falling_left', 4)
        self.load_animation('Samurai_falling_right', 4)
        self.load_animation('Samurai_run_left', 8)
        self.load_animation('Samurai_run_right', 8)
        self.load_animation('Samurai_sliding_right', 4)
        self.load_animation('Samurai_sliding_left', 4)
        self.load_animation('Samurai_Wall_Left', 15)
        self.load_animation('Samurai_Wall_Right', 15)

    def checkController(self):
        if(self.controller.getPlayer1Up()):
            self.keyboard.press("w")
        else:
            self.keyboard.release("w")
            
        if(self.controller.getPlayer1Down()):
            self.keyboard.press("s")
        else:
            self.keyboard.release("s")
            
        if(self.controller.getPlayer1Right()):
            self.keyboard.press("d")
        else:
            self.keyboard.release("d")
            
        if(self.controller.getPlayer1Left()):
            self.keyboard.press("a")
        else:
            self.keyboard.release("a")

        if(self.controller.getPlayer1Button1()):
            self.keyboard.press(Key.space)
        else:
            self.keyboard.release(Key.space)

        if(self.controller.getPlayer1Button2()):
            self.keyboard.press("q")
        else:
            self.keyboard.release("q")

    def setMoveDirection(self, direction):
        self.moveDirection = direction
    def fixAnimation(self):

        if (self.grounded == True):
            if self.running == True:
                if(self.sliding == False):
                    if self.moveDirection == d.left:
                        self.changeHeight(self.standHeight)
                        self.changeAnimation('Samurai_run_left')
                    if self.moveDirection == d.right:
                        self.changeHeight(self.standHeight)
                        self.changeAnimation('Samurai_run_right')
                if(self.sliding == True):
                    if self.moveDirection == d.left:
                        self.changeHeight(self.slideHeight)
                        self.changeAnimation('Samurai_sliding_left')
                    if self.moveDirection == d.right:
                        self.changeHeight(self.slideHeight)
                        self.changeAnimation('Samurai_sliding_right')
            if self.running == False:
                if self.sliding == False:
                    if self.direction == d.left:
                        self.changeHeight(self.standHeight)
                        self.changeAnimation('Samurai_idle_left')
                    if self.direction == d.right:
                        self.changeHeight(self.standHeight)
                        self.changeAnimation('Samurai_idle_right')
                if self.sliding == True:
                    if self.direction == d.left:
                        self.changeHeight(self.slideHeight)
                        self.changeAnimation('Samurai_sliding_left')
                    if self.direction == d.right:
                        self.changeHeight(self.slideHeight)
                        self.changeAnimation('Samurai_sliding_right')
        if (self.grounded == False):
            if(self.sliding == False):
                if(self.grabbed == True):
                    if self.grabDirection == d.right:
                        self.changeHeight(self.standHeight)
                        self.changeAnimation('Samurai_Wall_Right')
                    if self.grabDirection == d.left:
                        self.changeHeight(self.standHeight)
                        self.changeAnimation('Samurai_Wall_Left')
                if(self.grabbed == False):
                    if self.direction == d.left:
                        self.changeHeight(self.standHeight)
                        self.changeAnimation('Samurai_falling_left')
                    if self.direction == d.right:
                        self.changeHeight( self.standHeight)
                        self.changeAnimation('Samurai_falling_right')
                if(self.sliding == True):
                    if self.direction == d.left:
                        self.changeHeight(self.slideHeight)
                        self.changeAnimation('Samurai_sliding_left')
                    if self.direction == d.right:
                        self.changeHeight(self.slideHeight)
                        self.changeAnimation('Samurai_sliding_right')
    def setDirection(self, direction): # set the direction of the samurai

        self.direction = direction
        
    def jump(self):
        if(self.grounded == True or self.grabbed == True):
            print("HOP")
            self.jumps = self.jumps - 1
            if(self.grabbed == False):
                #print("NOT GRABBED BUT JUMPING ANYWAYS")
            #self.yVelo =  -1*self.jumpPower
            #self.grounded = False
                self.jumpY = -1 * self.jumpPower
            if(self.grabbed == True):
                self.grabbed = False
                self.grabTime -= 30
                if(self.grabTime < 0):
                    self.grabTime = 0
                self.jumpY = -1 * self.jumpPower
                if(self.grabDirection == d.right):
                    print("WALLJUMP LEFT")
                    self.jumpX = -1 * self.jumpPower
                #self.setMoveDirection(d.left)
                if(self.grabDirection == d.left):
                    print("WALLJUMP RIGHT")
                    self.jumpX =  self.jumpPower
                self.grabDirection = d.none
    
    def dash(self):
        if self.dashing == False:
            if self.energy == self.maxEnergy:
                self.dashing = True
                #if(self.direction == d.left):
                    #self.jumpX = -1 * 25
                #if(self.direction == d.right):
                    #self.jumpX = 1 * 25

    def checkSliding(self):
        
        if(self.sliding == False and self.blocked == True):
            self.sliding == True
        if(self.trySliding == False):
            self.blocked = self.collider.checkHead(self, 64)
            if(self.blocked == False):
                self.sliding = False
            if(self.blocked == True):
                self.sliding = True
        if(self.trySliding == True):
            self.sliding = True

    def update(self):
        super().update()
        #self.checkController()
        self.updateKeys()
        self.doMovement()
        self.fixAnimation()

    def doMovement(self):

        if self.energy < self.maxEnergy and self.dashing == False:
            self.energy +=1
            #controller.setLightButton2(False)
        if(self.energy == self.maxEnergy):
            #controller.setLightButton2(True)
            a = 1

        dir = 0
        if self.moveDirection == d.LEFT:
            dir = -1
        if self.moveDirection == d.RIGHT:
            dir = 1

        self.checkSliding()

        if(self.grounded == True):
            if(self.sliding == False):
                accel = self.groundAccel * dir
            if(self.sliding == True):
                if self.xVelo == 0:
                    accel = 0
                else:
                    accel = 0
                    if(self.frictionToggle == 0):#make friction occur every other tick so you can slide farther
                        accel = -1 * dir * self.slideAccel
                    self.frictionToggle = (self.frictionToggle + 1)%3
                if (self.blocked == True and self.xVelo == 0):
                    accel = dir
           
        if(self.grounded == False):
            accel = self.airAccel * dir
        #determine movement conditions in x

        if(self.grabbed == False):
            if(self.grabTime < 60):
                self.grabTime = self.grabTime + 1
        if(self.grabbed == True):
            self.grabTime = self.grabTime - 1
            self.jumps = self.maxJumps
            if (self.grabTime <= 0):
                self.grabbed = False
                self.grabDirection = d.none
            if (self.moveDirection != self.grabDirection):
                self.jump()
        #determine movement conditions in y

        if(accel == 0 and self.sliding == False and self.grounded == True):
            if(self.xVelo >0):
                self.xVelo = self.xVelo - self.groundDecel
                if(self.xVelo < 0):
                    self.xVelo = 0
            if(self.xVelo < 0):
                self.xVelo = self.xVelo + self.groundDecel
                if(self.xVelo > 0):
                    self.xVelo = 0
        #decelerate if applicable

        self.xVelo = self.xVelo + accel
        if(self.jumpX != 0):
            self.xVelo = self.jumpX
            self.jumpX = 0

        if(self.dashing == False):
            if(abs(self.xVelo) > self.maxSpeed):
                if(self.xVelo <0):
                    self.xVelo = -1*self.maxSpeed
                if(self.xVelo >0):
                    self.xVelo = 1*self.maxSpeed  
        if(self.dashing == True):
            if self.direction == d.left:
                dir = -1
            if self.direction == d.right:
                dir = 1
            self.xVelo = dir * 30
            self.energy -= 10
            if(self.energy <= 0):
                self.energy = 0
                self.dashing = False
        #accelerate in x
        
        
        if(self.grounded == False and self.grabbed == False and self.dashing == False):
            self.yVelo += 1 #apply gravity
        if(self.grounded == True):
            self.jumps = self.maxJumps
            self.yVelo = 0
        if(self.grabbed == True):
            self.yVelo = 0
        if(self.jumpY != 0):
            self.yVelo = self.jumpY
            self.jumpY = 0
        #accelerate in y


        if(abs(self.yVelo) >15):# limit yVelo
            if(self.yVelo > 0):
                self.yVelo = 15
            if(self.yVelo <0):
                self.yVelo = -15


        #assume not on ground to start
        #print(self.yVelo)
        
        #if(count != 0):
            #print(count)

        if(self.xVelo != 0):
            self.move(self.xVelo, 0)#move in x first
            if self.collider.doCollision(self, self.xVelo, 0):
                groundedFlag = True
        groundedFlag = False
        if(self.yVelo != 0):
            
            self.move(0, self.yVelo)#then move in y
            if self.collider.doCollision(self, 0,self.yVelo):
              groundedFlag = True

            self.grounded = groundedFlag
        else:
            if self.collider.doCollision(self, 0,1):
              groundedFlag = True
            self.grounded = groundedFlag
    def updateKeys(self):
        pygame.event.pump()#give it a lil' pump
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.fixDirection(d.LEFT, True)
                if event.key == pygame.K_d:
                    self.fixDirection(d.RIGHT, True)
                if event.key == pygame.K_s:
                    self.trySliding = True
                    #self.fixDirection(d.DOWN, True)
                if event.key == pygame.K_w:
                    self.grabbing = True
                if event.key == pygame.K_SPACE:
                    
                    if (self.jumpPressed == False):
                        #print("S P A C E   B A R")
                        self.jump()
                    self.jumpPressed = True
                if event.key == pygame.K_q:
                    if(self.dashPressed == False):
                        self.dash()
                    self.dashPressed = True
                if event.key == pygame.K_1:
                    self.LEVEL = 1;
                if event.key == pygame.K_2:
                    self.LEVEL = 2;
                if event.key == pygame.K_3:
                    self.LEVEL = 3;
                if event.key == pygame.K_4:
                    self.LEVEL = 4;
                if event.key == pygame.K_5:
                    self.LEVEL = 5;
                if event.key == pygame.K_6:
                    self.LEVEL = 6;
                if event.key == pygame.K_ESCAPE:
                    self.EXIT = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.fixDirection(d.LEFT, False)
                if event.key == pygame.K_d:
                    self.fixDirection(d.RIGHT, False)
                if event.key == pygame.K_s:
                    self.trySliding = False
                    #self.fixDirection(d.DOWN, False)
                if event.key == pygame.K_w:
                    self.grabbing = False
                    self.grabbed = False
                    #print("LET GO")
                if event.key == pygame.K_SPACE:
                    self.jumpPressed = False
                if event.key == pygame.K_q:
                    self.dashPressed = False
    
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
        #rationalize animation variables
        
        if self.moveDirection == d.none:
            self.running = False
        else:
            self.running = True