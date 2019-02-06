#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys,pygame
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

	screen.fill((0,0,0))
	pygame.display.flip()

	alpha=0
	alphat=True
	alpha2=0
	alpha2t=True
	alpha3=0
	alpha3t=True

	fs=.5 # fade speed

	running=True
	while running:
		screen.fill((0,0,0))
		image=pygame.image.load("glc.png")
		image.set_alpha(alpha)
		screen.blit(image,(ww/2-150/2,wh/2-150/2))
		prs=(pygame.font.Font("font/kongtext.ttf",30)).render("Presenta:",False,(255,255,255))
		prs.set_alpha(alpha2)
		screen.blit(prs,(ww/2-(30*len("Presenta:"))/2,wh/2-30/2))
		image=pygame.image.load("logo.png")
		image.set_alpha(alpha3)
		screen.blit(image,(ww/2-300/2,wh/2-300/2))
		if alpha<255 and alphat:
			alpha+=fs
		else:
			alphat=False
			if alpha>0:
				alpha-=fs
			else:
				if alpha2<255 and alpha2t:
					alpha2+=fs
				else:
					alpha2t=False
					if alpha2>0:
						alpha2-=fs
					else:
						if alpha3<255 and alpha3t:
							alpha3+=fs
						else:
							alpha3t=False
							alpha3-=fs
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
		pygame.display.flip()
if __name__=="__main__":
	main()