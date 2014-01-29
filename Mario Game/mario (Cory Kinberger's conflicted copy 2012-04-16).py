from pygamehelper import *
from pygame import *
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
		
		self.dir = 1
		
		self.maxvel = 3 #player's maximum running velocity
		
		self.right = 0 #check to see if player needs to accelerate
		self.left = 0
		self.rightdown = 0 #check to see if the right key is down
		self.leftdown = 0
		
		self.acceleration = .3 #the acceleration of the player
		
		self.deaccelerate = 0 #check to see if the player needs to accelerate
		self.deacceleration = .2 #the deacceleration of the player
		
		
		self.jumpvel = -10 #jump power
		self.jumpmaxtime = 5 #max time to hold the jump button
		self.jumptime = 0 #used to iterate from 1 to maxtime
		
		self.life = 100
		
		

class Starter(PygameHelper):
	#size = 256, 194
	#pygame.display.get_surface(size,pygame.RESIZABLE)#(reslolution=(w,h))#, flags=pygame.RESIZABLE, depth=0)
	def __init__(self):
		
		self.w, self.h = 256, 194
		#size = 1000, 194
		#pygame.display.set_mode(size)#(reslolution=(self.w,self.h), flags=pygame.RESIZABLE, depth=0)
		PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
		
		#self.bgpos = 0, -269
		self.bg= background()
		self.me= player()
		
		self.gravity= vec2d(0, 2)
		
		#load the mario image
		Player= pygame.image.load('big_standing1.png').convert()
		Player.set_colorkey((255,242,0))
		self.player = Player
		
	def update(self):
		self.me.pos+= self.me.vel
		
		#if accelerating
		if self.me.right==1:
			if self.me.vel.x < self.me.maxvel:
				self.me.vel.x+= self.me.acceleration
		if self.me.left==-1:
			if self.me.vel.x > -1*self.me.maxvel:
				self.me.vel.x-= self.me.acceleration
		
		#if deaccelerating
		if self.me.deaccelerate==1 and self.me.vel.y == 0:
			if self.me.vel.x > 0:
				self.me.vel.x-= self.me.deacceleration
				if self.me.vel.x < 0:
					self.me.vel.x =0
			elif self.me.vel.x < 0:
				self.me.vel.x+= self.me.deacceleration
				if self.me.vel.x > 0:
					self.me.vel.x = 0

			if self.me.vel == 0:
				self.me.deaccelerate = 0
		
		#if the player is in the air let gravity take over
		if self.me.pos.y < 119:
			
			#if the user hits jump 
			if self.me.jumptime > 0:# and (self.me.action == 0 or self.me.action == 1):
				print self.me.jumptime, self.me.jumpmaxtime, self.me.action
				if self.me.jumptime < self.me.jumpmaxtime:
					self.me.jumptime+= 1
					self.me.vel.y = self.me.jumpvel
				else:
					self.me.jumptime = 0
					
				
			else: 
				self.me.jumptime = 0
				self.me.vel+= self.gravity #else apply normal gravity
		
			#print self.me.jumptime
		
		#else if the player is standing
		elif self.me.pos.y >= 119:
			if self.me.vel.y >= 0:
				self.me.vel.y = 0
				
			if self.me.vel.x == 0 and self.me.jumptime == 0:
				self.me.action = 0
			elif self.me.jumptime == 0:
				self.me.action = 1
				
			if self.me.pos.y > 119:
				self.me.pos.y = 119
			
			if self.me.jumptime > 0:
				print self.me.action
				#print self.me.jumpmaxtime
				if self.me.jumptime < self.me.jumpmaxtime:
					self.me.jumptime+= 1
					self.me.vel.y = self.me.jumpvel
				else:
					#print self.me.jumptime
					self.me.jumptime = 0
					
		#print self.me.action
		#just print y vel
		#print self.me.vel.y
		
		#move the background#
		#move left
		if self.me.pos.x < (self.w/2)-10:
			if self.bg.pos.x >= 0: #if background is as far left as it can go
				print self.bg.pos.x, self.me.pos.x
				self.bg.pos.x = 0
				if self.me.pos.x < 0: #if player is touching the left wall
					self.me.pos.x = 0
					self.me.vel.x = 0
			else: #else if background can still scroll left
				self.me.pos.x = (self.w/2)-10
				self.bg.pos.x -= self.me.vel.x
				print self.me.pos.x, self.bg.pos.x
		#move right
		if self.me.pos.x > (self.w/2)+10:
			self.me.pos.x = (self.w/2)+10
			self.bg.pos.x -= self.me.vel.x
        
	def keyUp(self, key):
		if key==K_a:
			self.me.left = 0
			if self.me.rightdown == 1:
				self.me.right = 1
			if self.me.right == 0:
				self.me.deaccelerate = 1
			self.me.leftdown = 0
			
		if key==K_d:
			self.me.right = 0
			
			if self.me.leftdown == 1:
				print "left now equals 1"
				self.me.left = -1
				
			if self.me.left == 0:
				self.me.deaccelerate = 1
				
			self.me.rightdown = 0
			
		if key==K_x:
			self.me.jumptime = 0
			
	def keyDown(self, key):
		if key==K_a:
			self.me.left = -1
			self.me.deaccelerate = 0
			self.me.right = 0
			self.me.leftdown = 1
		if key==K_d:
			self.me.right = 1
			self.me.deaccelerate = 0
			self.me.left = 0
			self.me.rightdown = 1
			
		if key==K_x:
			#print self.me.jumptime
			if self.me.action == 0 or self.me.action == 1 or self.me.action == 2:
				self.me.jumptime = 1
				
				self.me.action = 3
				print self.me.action
				
	
	def mouseUp(self, button, pos):
		pass
        
	def mouseMotion(self, buttons, pos, rel):
		pass
        
	def draw(self):
		
		#create background
		self.screen.blit(self.bg.img,(self.bg.pos))
		
		#if self.me.dir == 1: face right
		#if self.me.dir == 0: face left
		

		self.screen.blit(self.player, self.me.pos- (self.player.get_width()/2, 0))
		
s = Starter()
s.mainLoop(60)
