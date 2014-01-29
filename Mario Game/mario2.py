from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform

class background:
    def __init__(self):
        
        self.pos = vec2d(0,-269)
        self.img = pygame.image.load("world 1-1 2816x432.png")

class player:
    def __init__(self):
        
        self.pos = vec2d(0,0)
        self.vel = vec2d(0,0)
        
        self.action = 0 #0 = standing, 1 = running, 2 = ducking, 3 = jumping
                        #(also to implement: 4 = flying, 5 = swimming)
         
        self.maxvel = 3 #player's maximum running velocity
        
        self.movingright = True #check to see if player needs to accelerate
        self.rightdown = 0 #check to see if the right key is down
        self.leftdown = 0
        
        self.accelerate = True #check to see if the player needs to accelerate
        self.acceleration = 1 #the acceleration of the player
        self.friction = .2 #the deacceleration of the player
        
        
        self.jumpvel = -10 #jump power
        self.jumpmaxtime = 5 #max time to hold the jump button
        self.jumptime = 0 #used to iterate from 1 to maxtime
        
        self.life = 100
        
		self.sprites = None
		if self.sprites = None:
            sprites = pygame.image.load('Sprites.png').convert()
             
		self
		
class main(PygameHelper):
    def __init__(self):
        self.w, self.h = 256, 194
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
        
        self.bg = background()
        self.me = player()
        
        self.gravity= vec2d(0, 2)

m = main()
m.mainLoop(30)