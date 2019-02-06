#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys,random,pygame
def rn(max):
	n=random.randint(1,max)
	n=("0"*(3-len(str(n))))+str(n)
	return n
def ri(f):
	return f+random.choice(os.listdir(f))
def main():
	# initialize the pygame module
	pygame.init()
	# load and set the logo
	logo = pygame.image.load("logo.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("VaporSchool")
	
	# create a surface on screen that has the size of 240 x 180
	screen = pygame.display.set_mode((150,150))
	
	screen.fill((255,255,140))
	image=pygame.image.load(ri("texture/body/"))
	screen.blit(image, (0,0))
	image=pygame.image.load(ri("texture/face/"))
	screen.blit(image, (0,0))
	image=pygame.image.load(ri("texture/eye/"))
	screen.blit(image, (0,0))
	image=pygame.image.load(ri("texture/brow/"))
	screen.blit(image, (0,0))
	image=pygame.image.load(ri("texture/hair/"))
	screen.blit(image, (0,0))
	image=pygame.image.load(ri("texture/nose/"))
	screen.blit(image, (0,0))
	image=pygame.image.load(ri("texture/mouth/"))
	screen.blit(image, (0,0))
	pygame.display.flip()

	pygame.mixer.music.load("music/shootingstarsmidi.mid")
	pygame.mixer.music.play()
	
	# define a variable to control the main loop
	running = True
	
	# main loop
	while running:
		pygame.time.wait(300)
		screen.fill((255,255,140))
		image=pygame.image.load(ri("texture/body/"))
		screen.blit(image, (0,0))
		image=pygame.image.load(ri("texture/face/"))
		screen.blit(image, (0,0))
		image=pygame.image.load(ri("texture/eye/"))
		screen.blit(image, (0,0))
		image=pygame.image.load(ri("texture/brow/"))
		screen.blit(image, (0,0))
		image=pygame.image.load(ri("texture/hair/"))
		screen.blit(image, (0,0))
		image=pygame.image.load(ri("texture/nose/"))
		screen.blit(image, (0,0))
		image=pygame.image.load(ri("texture/mouth/"))
		screen.blit(image, (0,0))
		pygame.display.flip()
		# event handling, gets all event from the event queue
		for event in pygame.event.get():
			# only do something if the event is of type QUIT
			if event.type == pygame.QUIT:
				# change the value to False, to exit the main loop
				running = False
	 
	 
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
	# call the main function
	main()