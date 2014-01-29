from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform

class player:
	def __init__(self):
		self.pos = vec2d(0,0)
		self.vel = vec2d(0,0)
		self.life = 100
		self.maxvel = 4
		self.acceleration = 1
		self.deaccelerate = 0
		self.jump = 4

class Starter(PygameHelper):
	def __init__(self):
		self.w, self.h = 800, 600
		PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
        
		self.me= player()
		
		self.gravity= vec2d(0, 0.3)
		
	def update(self):
		self.me.pos+= self.me.vel
		self.me.vel+= self.gravity
		
		#if the player is standing on the ground they have no y vel
		if self.me.pos.y > 600:
			self.me.vel.y = 0
		
		if self.me.deaccelerate==1:
			if self.me.vel.x > 0:
				self.me.vel.x-= 1
			else:
				self.me.vel.x-= 1
			if self.me.vel == 0:
				self.me.deaccelerate = 0
		
		self.me.pos= self.me.pos + self.me.vel #move the particle
		self.me.vel += self.gravity #make the velocity more along direction of gravity
        
	def keyUp(self, key):
		if key==K_a:
			self.me.deaccelerate = 1
		if key==K_d:
			self.me.deaccelerate = 1
        
	
	def keyDown(self, key):
		if key==K_a:
			self.deaccelerate = 0
			if self.me.vel.x<self.me.maxvel:
				self.me.vel.x-=self.me.acceleration
			else:
				self.me.vel.x-=self.me.maxvel
		if key==K_d:
			self.deaccelerate = 0
			if self.me.vel.x<self.me.maxvel:
				self.me.vel.x+=self.me.acceleration
			else:
				self.me.vel.x+=self.me.maxvel
        if key==K_SPACE:
			if self.me.y==0:
				self.me.vel.y= -self.me.jump
	
	def mouseUp(self, button, pos):
		pass
        
	def mouseMotion(self, buttons, pos, rel):
		pass
        
	def draw(self):
		pass
        
s = Starter()
s.mainLoop(40)
