#Trying to make my own Breakout game. Having problems with flipping my animation to make it go right.
#Also having some trouble with collitionDetection between Mario/blocks and the fireball. Anyone help me? :D
 
 
import pygame, sys, glob
from pygame.locals import *
import random
import time
import math
 
pygame.init()
 
width = 600
height = 380
 
screen = pygame.display.set_mode((width,height),0,32)
 
Fireball_Image = "ball.png"
mario_still = "mario_walk1.png"
Supermario_breakout_world  = "world.png"
Supermario_breakout_menu = "world4.jpg"
 
supermario = pygame.image.load(mario_still).convert_alpha()
fireball = pygame.image.load(Fireball_Image).convert_alpha()
Background  = pygame.image.load(Supermario_breakout_world).convert()
Background2 = pygame.image.load(Supermario_breakout_menu).convert()
 
clock = pygame.time.Clock()
 
pygame.mouse.set_visible(0)
 
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
 
block_width = 25
block_height = 15
 
class Block(pygame.sprite.Sprite):
    def __init__ (self,color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([block_width,block_height])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
blocks = pygame.sprite.RenderPlain()
allsprites = pygame.sprite.RenderPlain()
 
top = 0
blockcount = 36    
 
for row in range(5):
    for column in range(0,blockcount):
        block = Block(blue,column*(block_width+2)+1,top)
        blocks.add(block)
        allsprites.add(block)
    top += block_height+2
 
 
 
class FireballObject(object):
    def __init__ (self):
        self.x = random.random() * width
        self.y = random.random() * height
        self.speed = 400
        self.dy = self.speed
        self.dx = self.speed
 
    def collisionDetection(self):
        if self.x > 590:          
            self.dx = -self.speed
        if self.y > 315:
            self.dy = -self.speed
        if self.x < 0:
            self.dx = self.speed
        if self.y < 0:            
            self.dy = self.speed
   
    def move(self, time_passed_secs):
        self.x = self.x + self.dx * time_passed_secs
        self.y = self.y + self.dy * time_passed_secs
        self.collisionDetection()
 
class Ball(FireballObject):
    def draw(self):
        screen.blit(Background, (0,0))
        screen.blit(fireball, (self.x, self.y))
       
objects = [
    Ball()
    ]
 
class mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
       
        self.x = 300
        self.y = 292
        self.animasjon_speed_init = 5
        self.animasjon_speed = self.animasjon_speed_init
        self.animasjon = glob.glob("running\mario_walk*.png")
        self.animasjon.sort()
        self.animasjon_pos = 0
        self.animasjon_max = len(self.animasjon) -1
        self.img = pygame.image.load(self.animasjon[0]).convert_alpha()
        self.update(0)
           
    def update(self, pos):
        if pos != 0:
            self.animasjon_speed-=1
            self.x+=pos
            if self.animasjon_speed == 0:
                self.img = pygame.image.load(self.animasjon[self.animasjon_pos]).convert_alpha()
                self.animasjon_speed = self.animasjon_speed_init
                if self.animasjon_pos == self.animasjon_max:
                    self.animasjon_pos = 0
                else:
                    self.animasjon_pos+=1
        screen.blit(self.img,(self.x,self.y))
       
     
   
mario1 = mario()
pos = 0
 
while True:
   
    clock.tick(60)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            pos = 6
        elif event.type == KEYUP and event.key == K_RIGHT:
            pos = 0
        elif event.type == KEYDOWN and event.key == K_LEFT:
            pos = -6
        elif event.type == KEYUP and event.key == K_LEFT:
            pos = 0
    time_passed = clock.tick(200)
    time_passed_secs = time_passed/ 1000.0
 
    for obj in objects:
        obj.move(time_passed_secs)
 
    for obj in objects:
        obj.draw()
 
 
    allsprites.draw(screen)
           
    mario1.update(pos)
 
    pygame.display.update()