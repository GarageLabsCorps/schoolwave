#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys,pygame,random,math

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

def psd(objs,x,y,screen,flipped):
	for obj in objs:
		image=pygame.image.load(obj)
		if flipped:
			image=pygame.transform.flip(image,1,0)
		screen.blit(image, (x,y))
def txt(txt,px,x,y):
	if not "\n" in txt:
		return screen.blit((pygame.font.Font("font/kongtext.ttf",px)).render(txt,False,(0,0,0)),(x,y))
	else:
		lines=txt.split("\n")
		i=0
		for line in lines:
			screen.blit((pygame.font.Font("font/kongtext.ttf",px)).render(line,False,(0,0,0)),(x,y+px*i))
			i+=1
def txtw(txt,px,x,y):
	if not "\n" in txt:
		return screen.blit((pygame.font.Font("font/kongtext.ttf",px)).render(txt,False,(255,255,255)),(x,y))
	else:
		lines=txt.split("\n")
		i=0
		for line in lines:
			screen.blit((pygame.font.Font("font/kongtext.ttf",px)).render(line,False,(255,255,255)),(x,y+px*i))
			i+=1
def near():
	global p1x;global p2x;
	if p2x-p1x<=25:
		return True
	else:
		return False
def main():
	pygame.init()
	pygame.font.init()
	logo=pygame.image.load("logo.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("SchoolWave")

	global info;info=pygame.display.Info()
	global ww;ww=info.current_w/3
	global wh;wh=info.current_h/3
	global screen;screen=pygame.display.set_mode((ww,wh))

	screen.fill((255,255,140))
	wall=pygame.image.load("texture/wall/wall001.png")
	floor=pygame.image.load("texture/floor/floor001.png")

	# walls
	minw=0
	maxw=ww-150

	p1="texture/fig/people/vincentmangiolli/";global p1x;p1x=int((ww/2)/2)-41
	p1n=p1+"fn.png"
	p1p=p1+"fp.png"
	p1k=p1+"fk.png"
	p1s=p1+"fs.png"
	p1a=p1n
	p1l=100

	p2="texture/fig/people/nicolaiavmenise/";global p2x;p2x=int((ww/2)+((ww/2)/2))
	p2n=p2+"fn.png"
	p2p=p2+"fp.png"
	p2k=p2+"fk.png"
	p2s=p2+"fs.png"
	p2a=p2n
	p2l=100

	pcy=int((wh-150)/2)

	psd([p1a],p1x,pcy,screen,1)
	psd([p2a],p2x,pcy,screen,0)

	lbl=ww/3
	pygame.draw.rect(screen,(255,0,0),(10,10,lbl,10))
	pygame.draw.rect(screen,(0,255,0),(10,10,lbl,10))
	pygame.draw.rect(screen,(255,0,0),(ww-10-lbl,10,lbl,10))
	pygame.draw.rect(screen,(0,255,0),(ww-10-lbl,10,lbl,10))

	running=True
	while running:
		#pygame.time.wait(90)

		if p1l<=0 or p2l<=0:
			if p1l<=0:
				winner="P2"
			else:
				winner="P1"
			screen.fill((255,255,140))
			txt(winner+" "+langr["fight"]["win"],30,0,0)
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RETURN:
						running=False
				if event.type==pygame.QUIT:
					running=False
		else:
			for y in range(int(math.ceil(ww/150))+1):
				screen.blit(wall,(y*150,0))
			for x in range(int(math.ceil(wh/150))+1):
				screen.blit(floor,(0,(x+1)*150))
				for y in range(int(math.ceil(ww/150))+1):
					screen.blit(floor,(y*150,(x+1)*150))

			alb1=(lbl*p1l)/100 # lbl:x=100:p1l:
			alb2=(lbl*p2l)/100

			pygame.draw.rect(screen,(255,0,0),(10,10,lbl,10))
			pygame.draw.rect(screen,(0,255,0),(10,10,alb1,10))

			pygame.draw.rect(screen,(255,0,0),(ww-10-lbl,10,lbl,10))
			pygame.draw.rect(screen,(0,255,0),(ww-10-lbl,10,alb2,10))

			p1a=p1n
			p2a=p2n

			pressed=pygame.key.get_pressed()
			if pressed[pygame.K_d]:
				if p1x<=p2x:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						p1x+=.8
					else:
						p1x+=.5
			if pressed[pygame.K_a]:
				if p1x>=0:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						p1x-=.8
					else:
						p1x-=.5
			if pressed[pygame.K_p]:
				p1a=p1p
				if random.randint(0,5)>=3:
					p2a=p2s
			if pressed[pygame.K_o]:
				p1a=p1k
			if pressed[pygame.K_s]:
				p1a=p1s

			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_p:
						if p1a!=p1s:
							p1a=p1p
							if random.randint(0,5)>=3:
								p2a=p2s
							if near() and p2a!=p2s:
								p2l-=5
								if p2x<=maxw:
									p2x+=30
					if event.key==pygame.K_o:
						if p1a!=p1s:
							p1a=p1k
							if near():
								p2l-=2
				if event.type==pygame.QUIT:
					running=False

			if not near():
				if random.randint(0,100)>=50:
					p2x-=.5
			else:
				if random.randint(0,1000)>=1000:
					if p1a!=p1s:
						p2a=p2p
						if p1a!=p1s:
							p1l-=5
							if p1x>0:
								p1x-=30
					else:
						p2a=p2k
						p1l-=2
						if p1x>0:
							p1x-=30

			psd([p1a],p1x,pcy,screen,1)
			psd([p2a],p2x,pcy,screen,0)

		pygame.display.flip()
if __name__=="__main__":
	main()