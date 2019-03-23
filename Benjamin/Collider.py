import pygame
import Entity
class Collider():
    def __init__(self, group1):
        #self.player = player
        self.obstacles = group1
    def checkAll(self, player, dx, dy):
        topCollide = False
        bottomCollide = False
        leftCollide = False
        rightCollide = False

        for wall in self.obstacles.getAll():
            left, right, top, bottom = self.collide(player, wall, dx, dy)
            if top:
                topCollide = True
            if bottom:
                bottomCollide = True
            if left:
                leftCollide = True
            if right:
                rightCollide = True

        return topCollide, bottomCollide, leftCollide, rightCollide

    def collide(self, entity1, entity2, dx, dy):
        rY = entity2.rect.height / 4
        rX = entity2.rect.width / 4
        
        sY = entity1.rect.height / 4
        sX = entity1.rect.width / 4

        rL = pygame.Rect((entity2.rect.left),(entity2.rect.top + rY),(rX),(2*rY))
        rR = pygame.Rect((entity2.rect.right - rX),(entity2.rect.top + rY),(rX),(2*rY))
        rT = pygame.Rect((entity2.rect.left + rX),(entity2.rect.top),(2*rX),(rY))
        rB = pygame.Rect((entity2.rect.left + rX),(entity2.rect.bottom - rY),(2*rX),(rY))

        sL = pygame.Rect((entity1.rect.left),(entity1.rect.top + sY),(sX),(2*sY))
        sR = pygame.Rect((entity1.rect.right - sX),(entity1.rect.top + sY),(sX),(2*sY))
        sT = pygame.Rect((entity1.rect.left + sX),(entity1.rect.top),(2*sX),(sY))
        sB = pygame.Rect((entity1.rect.left + sX),(entity1.rect.bottom - sY),(2*sX),(sY))

        nsL = pygame.Rect(sL.left + dx, sL.top + dy, sL.width, sL.height)
        nsR = pygame.Rect(sR.left + dx, sR.top + dy, sR.width, sR.height)
        nsT = pygame.Rect(sT.left + dx, sT.top + dy, sT.width, sT.height)
        nsB = pygame.Rect(sB.left + dx, sB.top + dy, sB.width, sB.height)

        bL = rL.colliderect(nsR)
        bR = rR.colliderect(nsL)
        bT = rT.colliderect(nsB)
        bB = rB.colliderect(nsT)

        if(bT):
            entity1.moveTo(entity1.rect.left, entity2.rect.top - entity1.rect.height)
        elif(bB):
            entity1.moveTo(entity1.rect.left, entity2.rect.bottom)
        elif(bL):
            entity1.moveTo(entity2.rect.left - entity2.width, entity1.rect.top)
        elif(bR):
            entity1.moveTo(entity2.rect.right, entity1.rect.top)
        return (bL, bR, bT, bB)
    def manualCollide(self, entity1, entity2):
        if(entity1.rect.bottom >= entity2.rect.top and entity1.rect.top <= entity2.rect.bottom):
            print("Collide")
