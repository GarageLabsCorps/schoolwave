#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys,pygame,random,math,operator

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

def ri(f):
	return f+random.choice(os.listdir(f))
def psd(objs,x,y,screen):
	for obj in objs:
		image=pygame.image.load(obj)
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
def near(x,y):
	dx=40
	dy=40
	if playerx>=x:
		if playerx-x<=dx:
			if playery>=y:
				if playery-y<=dy:
					return True
				else:
					return False
			elif playery<y:
				if y-playery<=dy:
					return True
				else:
					return False
	elif playerx<x:
		if x-playerx<=dx:
			if playery>=y:
				if playery-y<=dy:
					return True
				else:
					return False
			elif playery<y:
				if y-playery<=dy:
					return True
				else:
					return False
def talk(who,t):
	b=pygame.Surface((ww,wh))
	b.set_alpha(50)
	b.fill((0,0,0))
	screen.blit(b,(0,0))
	pygame.display.flip()

	isqh=150     # image square height
	isqw=150     # image square width
	dsqh=100     # dialog square height
	dsqw=ww-isqw # dialog square width
	br=10        # border
	pd=10        # padding
	ts=15        # txt size
	st=dsqw-pd*2 # space for one line of text
	cl=int(st/ts)# char for line

	running=True
	while running:
		pygame.draw.rect(screen,(0,0,0),(0,wh-isqh-br,isqw+br,isqh+br))
		pygame.draw.rect(screen,(255,255,255),(0,wh-isqh,isqw,isqh))
		pygame.draw.rect(screen,(0,0,0),(isqw,wh-dsqh-br,dsqw+br,dsqh+br))
		pygame.draw.rect(screen,(255,255,255),(isqw+br,wh-dsqh,dsqw,dsqh))
		if len(t)>cl and not "\n" in t:
			for i in range(len(t)/cl):
				t=t[:cl*(i+1)]+"\n"+t[cl*(i+1):]
		txt(t,ts,isqw+br+pd,wh-dsqh+pd)
		whoimg=pygame.image.load(who)
		screen.blit(whoimg,(0,wh-isqh))
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					running=False
			if event.type==pygame.QUIT:
				running=False
		pygame.display.flip()
def intro():
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
		prs=(pygame.font.Font("font/kongtext.ttf",30)).render(langr["intro"]["p"],False,(255,255,255))
		prs.set_alpha(alpha2)
		screen.blit(prs,(ww/2-(30*len(langr["intro"]["p"]))/2,wh/2-30/2))
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
							if alpha3>0:
								alpha3-=fs
							else:
								running=False
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					running=False
			if event.type==pygame.QUIT:
				global runningall;runningall=False
				running=False
		pygame.display.flip()
def menu():
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
						running=False
						game()
					if o==2:
						txt("Carica partita...",30,0,0)
						pygame.display.flip()
						pygame.time.wait(1000)
					if o==3:
						running=False
			if event.type==pygame.QUIT:
				running=False
		pygame.display.flip()
def game():
	screen.fill((255,255,140))
	wall=pygame.image.load("texture/wall/wall001.png")
	floor=pygame.image.load("texture/floor/floor001.png")

	# walls
	minw=-50
	maxw=ww-105
	minh=35
	maxh=wh-125

	thingsdata={}

	pcpu001l="texture/fig/people/vincentmangiolli/little.png";thingsdata["pcpu001l"]=pcpu001l
	pcpu001n="texture/fig/people/vincentmangiolli/normal.png";thingsdata["pcpu001n"]=pcpu001n
	pcpu001x=random.randint(minw,maxw);thingsdata["pcpu001x"]=pcpu001x
	pcpu001y=random.randint(minh,maxh);thingsdata["pcpu001y"]=pcpu001y

	pcpu002l="texture/fig/people/nicolaiavmenise/little.png";thingsdata["pcpu002l"]=pcpu002l
	pcpu002n="texture/fig/people/nicolaiavmenise/normal.png";thingsdata["pcpu002n"]=pcpu002n
	pcpu002x=random.randint(minw,maxw);thingsdata["pcpu002x"]=pcpu002x
	pcpu002y=random.randint(minh,maxh);thingsdata["pcpu002y"]=pcpu002y

	pbodyl=ri("texture/bodylittle/")
	pfacel=ri("texture/facelittle/")
	peyel=ri("texture/eyelittle/")
	phairl=ri("texture/hairlittle/")
	pmouthl=ri("texture/mouthlittle/")
	ppants=ri("texture/pants/")
	pshoe=ri("texture/shoe/")
	for y in range(int(math.ceil(ww/150))+1):
		screen.blit(wall,(y*150,0))
	for x in range(int(math.ceil(wh/150))+1):
		screen.blit(floor,(0,(x+1)*150))
		for y in range(int(math.ceil(ww/150))+1):
			screen.blit(floor,(y*150,(x+1)*150))
	global playerx;playerx=120
	global playery;playery=160
	l=0
	psd([pcpu001l],pcpu001x,pcpu001y,screen)
	psd([pbodyl,pfacel,peyel,phairl,pmouthl,ppants,pshoe],playerx,playery,screen)
	pygame.display.flip()

	thingsd={"player":playery,"pcpu001":pcpu001y,"pcpu002":pcpu002y}
	thingsd=dict(sorted(thingsd.items(),key=operator.itemgetter(1)))
	things=thingsd

	music=False#music=True
	pygame.mixer.music.load("music/shootingstarsmidi.mid")
	if music:
		pygame.mixer.music.play()

	running=True
	while running:
		#pygame.time.wait(1)
		for y in range(int(math.ceil(ww/150))+1):
			screen.blit(wall,(y*150,0))
		for x in range(int(math.ceil(wh/150))+1):
			screen.blit(floor,(0,(x+1)*150))
			for y in range(int(math.ceil(ww/150))+1):
				screen.blit(floor,(y*150,(x+1)*150))

		pressed=pygame.key.get_pressed()
		if pressed[pygame.K_w]:
			if playery>=35:
				if pygame.key.get_mods() & pygame.KMOD_SHIFT:
					playery-=.5
				else:
					playery-=.3
		if pressed[pygame.K_a]:
			if playerx>=-50:
				if pygame.key.get_mods() & pygame.KMOD_SHIFT:
					playerx-=.5
				else:
					playerx-=.3
		if pressed[pygame.K_s]:
			if playery<=wh-125:
				if pygame.key.get_mods() & pygame.KMOD_SHIFT:
					playery+=.5
				else:
					playery+=.3
		if pressed[pygame.K_d]:
			if playerx<=ww-105:
				if pygame.key.get_mods() & pygame.KMOD_SHIFT:
					playerx+=.5
				else:
					playerx+=.3

		if pressed[pygame.K_r]:
			pbodyl=ri("texture/bodylittle/")
			pfacel=ri("texture/facelittle/")
			peyel=ri("texture/eyelittle/")
			phairl=ri("texture/hairlittle/")
			pmouthl=ri("texture/mouthlittle/")
			ppants=ri("texture/pants/")
			pshoe=ri("texture/shoe/")

		if pressed[pygame.K_n]:
			if music:
				pygame.mixer.music.stop()
				music=False
			else:
				pygame.mixer.music.play()
				music=True

		if near(pcpu001x,pcpu001y):
			txt(langr["instr"]["ettalk"],30,0,0)
			if pressed[pygame.K_e]:
				talk(pcpu001n,random.choice(list(langr["vincentmangiolli"]["dialog"].items()))[1])
		if near(pcpu002x,pcpu002y):
			txt(langr["instr"]["ettalk"],30,0,0)
			if pressed[pygame.K_e]:
				talk(pcpu002n,random.choice(list(langr["nicolaiavmenise"]["dialog"].items()))[1].replace("R","V").replace("r","v"))

		thingsd={"player":playery,"pcpu001":pcpu001y,"pcpu002":pcpu002y}
		thingsd=sorted(thingsd.items(),key=operator.itemgetter(1))
		things=list(thingsd)

		for objr in things:
			obj=objr[0]
			if obj=="player":
				psd([pbodyl,pfacel,peyel,phairl,pmouthl,ppants,pshoe],playerx,playery,screen)
			else:
				psd([thingsdata[str(obj)+"l"]],thingsdata[str(obj)+"x"],thingsdata[str(obj)+"y"],screen)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
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

	global runningall;runningall=True

	intro()
	if runningall:
		menu()
if __name__=="__main__":
	main()