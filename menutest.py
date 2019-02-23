#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys,pygame,random

def x2d(file):
	xmlf=open(file,"r")
	xml=xmlf.read()
	xmlf.close()
	di={}
	xml=xml.replace("    ","").replace("	","").replace("\n","").replace("\t","")
	xmlr=xml.split("<")
	da=["di"]
	for e in xmlr:
		if not e.startswith("?") and e!="":
			if not e.startswith("/"):
				n=e[:[pos for pos,char in enumerate(e) if char==">"][-1]]
				if len(e)>[pos for pos,char in enumerate(e) if char==">"][-1]+1:
					tmp=e[[pos for pos,char in enumerate(e) if char==">"][-1]+1:len(e)]
					w=da[0]
					for d in da:
						if d!=da[0]:
							w=w+"['"+d+"']"
					exec("%s[n]=tmp"%w)
				else:
					w=da[0]
					for d in da:
						if d!=da[0]:
							w=w+"['"+d+"']"
					tmp={}
					exec("%s[n]=tmp"%w)
					da.append(n)
			else:
				if e[1:[pos for pos,char in enumerate(e) if char==">"][-1]] in da:
					da.remove(e[1:[pos for pos,char in enumerate(e) if char==">"][-1]])
	return di

options=x2d("options-test.xml")
langf="lang/"+options["lang"]+"-test.xml"
langr=x2d(langf)

def txt(txt,px,x,y):
	return screen.blit((pygame.font.Font("font/kongtext.ttf",px)).render(txt,False,(0,0,0)),(x,y))
def txtw(txt,px,x,y):
	return screen.blit((pygame.font.Font("font/kongtext.ttf",px)).render(txt,False,(255,255,255)),(x,y))
def main():
	pygame.init()
	pygame.font.init()
	logo=pygame.image.load("logo.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("SchoolWave")

	info=pygame.display.Info()
	ww=info.current_w/3
	wh=info.current_h/3
	global screen
	screen=pygame.display.set_mode((ww,wh))

	screen.fill((255,255,255))
	screen.blit(pygame.transform.scale(pygame.image.load("menu.png"),(ww,wh)),(0,0))
	b=pygame.Surface((ww,wh))
	b.set_alpha(180)
	b.fill((0,0,0))
	screen.blit(b,(0,0))
	txtw(langr["menu"]["tit"],30,0,0)
	txtw(langr["menu"]["new"],20,ww-len(langr["menu"]["new"])*20,35)
	txtw(langr["menu"]["load"],20,ww-len(langr["menu"]["load"])*20,60)
	txtw(langr["menu"]["exit"],20,ww-len(langr["menu"]["exit"])*20,85)
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
		screen.blit(pygame.transform.scale(pygame.image.load("menu.png"),(ww,wh)),(0,0))
		screen.blit(b,(0,0))
		pygame.draw.rect(screen,(255,255,145),(ww,o*25+10,-300,20))
		txtw(langr["menu"]["tit"],30,0,0)
		if o==1:
			txt(langr["menu"]["new"],20,ww-len(langr["menu"]["new"])*20,35)
		else:
			txtw(langr["menu"]["new"],20,ww-len(langr["menu"]["new"])*20,35)
		if o==2:
			txt(langr["menu"]["load"],20,ww-len(langr["menu"]["load"])*20,60)
		else:
			txtw(langr["menu"]["load"],20,ww-len(langr["menu"]["load"])*20,60)
		if o==3:
			txt(langr["menu"]["exit"],20,ww-len(langr["menu"]["exit"])*20,85)
		else:
			txtw(langr["menu"]["exit"],20,ww-len(langr["menu"]["exit"])*20,85)
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