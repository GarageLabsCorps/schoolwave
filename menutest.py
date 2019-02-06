#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys,pygame,random
def txt(txt,px,x,y):
	return screen.blit((pygame.font.Font("font/kongtext.ttf",px)).render(txt,False,(0,0,0)),(x,y))
def main():
	pygame.init()
	pygame.font.init()
	logo=pygame.image.load("logo.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("VaporSchool")

	info=pygame.display.Info()
	ww=info.current_w/3
	wh=info.current_h/3
	global screen
	screen=pygame.display.set_mode((ww,wh))

	screen.fill((255,255,255))
	txt("MENU'",30,ww/2-15,0)
	txt("Nuova partita",20,ww/2-15,35)
	txt("Carica partita",20,ww/2-15,60)
	txt("Esci",20,ww/2-15,85)
	pygame.display.flip()

	o=1

	running=True
	while running:
		#pygame.time.wait(90)
		if o>3:
			o=1
		elif o<1:
			o=3
		screen.fill((255,255,255))
		pygame.draw.rect(screen,(255,255,145),(ww/2-15,o*25+10,300,20))
		txt("MENU'",30,ww/2-15,0)
		txt("Nuova partita",20,ww/2-15,35)
		txt("Carica partita",20,ww/2-15,60)
		txt("Esci",20,ww/2-15,85)
		pygame.display.flip()
		pressed=pygame.key.get_pressed()
		#if pressed[pygame.K_w]:
		#	o-=1
		#if pressed[pygame.K_s]:
		#	o+=1
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_w or event.key==pygame.K_a or event.key==pygame.K_UP or event.key==pygame.K_LEFT:
					o-=1
				if event.key==pygame.K_s or event.key==pygame.K_d or event.key==pygame.K_DOWN or event.key==pygame.K_RIGHT:
					o+=1
				if event.key==pygame.K_RETURN:
					if o==1:
						txt("Nuova partita...",30,0,0)
						pygame.display.flip()
						pygame.time.wait(1000)
					if o==2:
						txt("Carica partita...",30,0,0)
						pygame.display.flip()
						pygame.time.wait(1000)
					if o==3:
						running=False
			if event.type==pygame.QUIT:
				running=False
		pygame.display.flip()
if __name__=="__main__":
	main()