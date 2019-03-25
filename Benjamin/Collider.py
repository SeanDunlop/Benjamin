import pygame
import directions
import Entity
class Collider():
    def __init__(self, group1):
        self.obstacles = group1

    def doCollision(self, player, dx, dy):
        flag = False
        for wall in self.obstacles.getAll():
            if(self.Collide(player, wall, dx, dy)):
                flag = True
        return flag

    def checkHead(self, player, diff):
        initalCount = self.countCollide(player.rect)
        tallPlayer = pygame.Rect(player.rect.left, player.rect.top - diff, player.rect.width, player.rect.height)
        finalCount = self.countCollide(tallPlayer)
        return (finalCount > initalCount)
    def countCollide(self, rect):
        count = 0
        for wall in self.obstacles.getAll():
            if rect.colliderect(wall.rect):
                count +=1
        return count

    def Collide(self, player, wall, dx, dy):
        flag = False
        nextSam = pygame.Rect(player.rect.left + dx, player.rect.top + dy, player.rect.width, player.rect.height)
        if(nextSam.colliderect(wall.rect)):
            
            if(dx > 0):
                #player.rect.right = wall.rect.left
                player.moveTo(wall.rect.left - player.rect.width ,player.rect.top)
                player.xVelo = 0
                if(player.yVelo >= -5):
                    if(player.grabbing == True and player.grabTime >= 60 and player.grounded == False):
                        player.grabbed = True
                        player.grabDirection = directions.directions.right
                        #print("GRABBED RIGHT")
                        player.lastGrab = True
                    elif(player.grabbing == True and player.lastGrab == False and player.grounded == False):
                        player.grabTime = 60
                        player.grabbed = True
                        player.grabDirection = directions.directions.right
                        #print("GRABBED RIGHT")
                        player.lastGrab = True
            if(dx < 0):
                #player.rect.left = wall.rect.right
                player.moveTo(wall.rect.right, player.rect.top)
                player.xVelo = 0
                if(player.yVelo >= -5):
                    if(player.grabbing == True and player.grabTime >= 60 and player.grounded == False):
                        player.grabbed = True
                        player.grabDirection = directions.directions.left
                        #print("GRABBED LEFT")
                        player.lastGrab = False
                    elif(player.grabbing == True and player.lastGrab == True and player.grounded == False):
                        player.grabTime = 60
                        player.grabbed = True
                        player.grabDirection = directions.directions.left
                        #print("GRABBED LEFT")
                        player.lastGrab = False
            if(dy > 0):
                #player.rect.bottom = wall.rect.top
                player.moveTo(player.rect.left, wall.rect.top - player.rect.height - 1)
                flag = True
            if(dy < 0):
                #player.rect.top = wall.rect.bottom
                player.moveTo(player.rect.left, wall.rect.bottom)
                player.yVelo = 0
                print("My HEAD")
            if(dy == 0):
                print("OOF")
        return flag
