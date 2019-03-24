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

    def Collide(self, player, wall, dx, dy):
        flag = False

        nextSam = pygame.Rect(player.rect.left + dx, player.rect.top + dy, player.rect.width, player.rect.height)
        if(nextSam.colliderect(wall.rect)):
            
            if(dx > 0):
                #player.rect.right = wall.rect.left
                player.moveTo(wall.rect.left - player.rect.width ,player.rect.top)
                if(player.grabbing == True and player.grabTime >= 60):
                    player.grabbed = True
                    player.grabDirection = directions.directions.right
            if(dx < 0):
                #player.rect.left = wall.rect.right
                player.moveTo(wall.rect.right, player.rect.top)
                if(player.grabbing == True and player.grabTime >= 60):
                    player.grabbed = True
                    player.grabDirection = directions.directions.left
            if(dy > 0):
                #player.rect.bottom = wall.rect.top
                player.moveTo(player.rect.left, wall.rect.top - player.rect.height)
                flag = True
            if(dy < 0):
                #player.rect.top = wall.rect.bottom
                player.moveTo(player.rect.left, wall.rect.bottom)
                player.yVelo = 0
        
        return flag
