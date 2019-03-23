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
            #self.collide(player, wall, dx, dy)
            #left, right, top, bottom = self.manualCollide(player, wall, dx, dy)
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
            print("HitTop")
        elif(bB):
             entity1.moveTo(entity1.rect.left, entity2.rect.bottom)
        elif(bL):
            entity1.moveTo(entity2.rect.left - entity2.width, entity1.rect.top)
        elif(bR):
            entity1.moveTo(entity2.rect.right, entity1.rect.top)
        return (bL, bR, bT, bB)

    def manualCollide(self, player, wall, dx, dy):

        playerBox = player.rect
        widthAdjust = 25
        heightAdjust = 15
        wallBox = wall.rect

        bottomCollide = False
        topCollide = False
        leftCollide = False
        rightCollide = False

        if(playerBox.bottom + dy >= wallBox.top and playerBox.top + dy + heightAdjust <= wallBox.bottom):
            if(playerBox.right + dx - widthAdjust>= wallBox.left and playerBox.left + dx + widthAdjust <= wallBox.right):
                if (dy > 0):#if player is moving down
                    topCollide = True
                    if (dx > 0):#if player is moving right
                        a = 1
                        #leftCollide = True
                    if (dx < 0):#if player is moving left
                        a = 1
                        #rightCollide = True
                if (dy < 0):#if player is moving up
                    bottomCollide = True
                    if (dx > 0):#if player is moving right
                        a = 1
                        #leftCollide = True
                    if (dx < 0):#if player is moving left
                        #rightCollide = True
                        a = 1 

        return (leftCollide, rightCollide, topCollide, bottomCollide)