import pygame
import time
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
fps = 100
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("PONG")
up=0
down = 0
mup = 0
mdown = 0
change = 0
score1 = 0
score2 = 0
def show_text(msg,x,y):
    fontobj = pygame.font.SysFont("freesans",20,False)
    msgobj = fontobj.render(msg,True,(255,255,255))
    screen.blit(msgobj,(x,y))
class Ball():     
    def __init__(self):                 
        self.color = (255, 0, 0)         
        self.radius = 25         
        self.xmovement = 8         
        self.ymovement = 10
        self.cx = 250
        self.cy = 250
        self.xchange = 1
        self.ychange = 1
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.cx,self.cy),self.radius)
    def bounce(self):
        self.cx = self.cx + self.xchange
        self.cy = self.cy + self.ychange
        if self.cy>=475:
            self.ychange=-1*self.ychange
        if self.cy<=25:
            self.ychange=-1*self.ychange
        if self.cx>475:
            self.cx=250
            self.cy=250
            pygame.draw.circle(screen,self.color,(self.cx,self.cy),self.radius)
            time.sleep(1)
        if self.cx<25:
            self.cx=250
            self.cy=250
            pygame.draw.circle(screen,self.color,(self.cx,self.cy),self.radius)
            time.sleep(1)
##        if self.cx-25==p1.right and p1.top<=cx<=p1.bottom:
##            self.xchange=-1*self.xchange
##            ychange=-1*ychange
##        if self.cx+25==p2.left and p2.top<=cx<=p2.bottom:  
##            self.xchange=-1*self.xchange
##            self.ychange=-1*self.ychange
class Paddle():
    def __init__(self , color, x , y, width, height):         
        self.color = color         
        self.x = x         
        self.y = y
        self.width = width         
        self.height = height
        self.up = False         
        self.down = False         
        self.score = 0         
        self.mup = 0
        self.mdown = 0
        self.moup = 0
        self.modown = 0
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
    def move(self,change):
            self.y=self.y+change
            if self.y<=0:
                self.y=0
            if self.y>=400:
                self.y=400
        
p1 = Paddle((0,255,0),0,200, 50, 100)
p2 = Paddle((0,0,255),450,200, 50 , 100)
ball = Ball()
while True:
    #print(up, mup, down, mdown)
    #print("self.y :",p1.y)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type==KEYDOWN:
            if event.key==K_w:
                up=1       
            elif event.key==K_s:
                down = 1
            elif event.key==K_UP:
                mup = 1
            elif event.key==K_DOWN:
                mdown=1
        elif event.type==KEYUP:
            if event.key==K_w:
                up = 0
            elif event.key==K_s:
                down = 0
            elif event.key==K_UP:
                mup = 0
            elif event.key==K_DOWN:
                mdown = 0
    if up==1:
        p1.move(-5)
    if mup == 1:
        p2.move(-5)
    if down == 1:
        p1.move(5)
    if mdown == 1:
        p2.move(5)
    screen.fill((0,0,0))
    clock.tick(fps)
    ball.draw()
    ball.bounce()
    p1.draw()
    p2.draw()
    if (ball.cx + ball.radius) == p2.x and ball.cy in range (p2.y-3,p2.y+p2.height+3):      
        ball.xchange = -1 * ball.xchange
    if (ball.cx - ball.radius) == (p1.x + p1.width) and ball.cy in range (p1.y-3,p1.y+p1.height+3):
        print("Collision")  
        ball.xchange = -1*ball.xchange
    if ball.cx - ball.radius <= 0:
        score2 = score2 + 1
    if ball.cx + ball.radius >= 500:
        score1 = score1 + 1
    player1 = "P1: "+str(score1)
    player2 = "P2: "+str(score2)
    show_text(player1,55,0)
    show_text(player2,400,0)
    pygame.display.update()
  
        


