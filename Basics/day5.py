# Projectile


import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
pygame.display.set_caption("Using OOP.")

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self,screen):
        if self.walkCount+1>=27:
            self.walkCount = 0
        
        if not(self.standing):

         if self.left:
           screen.blit(walkLeft[self.walkCount//3],(self.x,self.y))     
         elif per.right:
          screen.blit(walkRight[self.walkCount//3],(self.x,self.y))
          self.walkCount += 1  
        else:
          if self.left:
              screen.blit(walkLeft[0],(self.x,self.y))
          else:
              screen.blit(walkRight[0],(self.x,self.y))
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 7 * facing

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)

  
 

walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
bullets = []
run = True


def redrawGamewindow():
    screen.blit(bg,(0,0))
    per.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()

per = player(280,380,64,64)
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.x<500 and bullet.x>0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if per.left:
            facing = -1
        else:
            facing = 1
        if len(bullets)<5:
            bullets.append(projectile(round(per.x+per.width//2),round(per.y+per.height//2),8,(2,0,0),facing))                
    if keys[pygame.K_RIGHT ] and per.x <500-per.width-per.vel:
        per.x+=per.vel   
        per.left = False
        per.right = True
        per.standing = False
    elif keys[pygame.K_LEFT] and per.x > per.vel:
        per.x-=per.vel
        per.left = True
        per.right = False
        per.standing = False
    else:
        per.standing = True
        per.walkCount = 0
    if not(per.isJump):
        
        if keys[pygame.K_UP]:
            per.isJump = True
            per.right = False
            per.left = False
            per.walkCount = 0
    else:
        if per.jumpCount>=-10:
            neg = 1
            if(per.jumpCount<0):
                neg = -1
            per.y-=(per.jumpCount ** 2)*0.5*neg
            per.jumpCount-=1
        else:
            per.isJump = False
            per.jumpCount = 10
    redrawGamewindow()
pygame.quit