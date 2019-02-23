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
	minw=-50
	maxw=ww-105
	minh=35
	maxh=wh-125

	thingsdata={}

	pcpu001l="texture/fig/people/vincentmangiolli/little.png";thingsdata["pcpu001l"]=pcpu001l
	pcpu001n="texture/fig/people/vincentmangiolli/normal.png";thingsdata["pcpu001n"]=pcpu001n
	pcpu001x=random.randint(minw,maxw);thingsdata["pcpu001x"]=pcpu001x
	pcpu001y=random.randint(minh,maxh);thingsdata["pcpu001y"]=pcpu001y
	pcpu001tmpdest=["",""] # temp destination

	pcpu002l="texture/fig/people/nicolaiavmenise/little.png";thingsdata["pcpu002l"]=pcpu002l
	pcpu002n="texture/fig/people/nicolaiavmenise/normal.png";thingsdata["pcpu002n"]=pcpu002n
	pcpu002x=random.randint(minw,maxw);thingsdata["pcpu002x"]=pcpu002x
	pcpu002y=random.randint(minh,maxh);thingsdata["pcpu002y"]=pcpu002y
	pcpu002tmpdest=["",""] # temp destination

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
	psd([pcpu001l],thingsdata["pcpu001x"],thingsdata["pcpu001y"],screen)
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

		# pcpu001 destination
		if pcpu001tmpdest[0]=="":
			pcpu001tmpdest[0]=random.randint(minw,maxw) # temp X destination for pcpu001
			pcpu001tmpdest[1]=random.randint(minh,maxh) # temp Y destination for pcpu001
		# X destination
		if pcpu001tmpdest[0]-1<thingsdata["pcpu001x"]<pcpu001tmpdest[0]+1:
			pcpu001tmpdest[0]=random.randint(minw,maxw)
		else:
			if thingsdata["pcpu001x"]>pcpu001tmpdest[0]:
				thingsdata["pcpu001x"]-=.3
			else:
				thingsdata["pcpu001x"]+=.3
		# Y destination
		if pcpu001tmpdest[1]-1<thingsdata["pcpu001y"]<pcpu001tmpdest[1]+1:
			pcpu001tmpdest[1]=random.randint(minh,maxh)
		else:
			if thingsdata["pcpu001y"]>pcpu001tmpdest[1]:
				thingsdata["pcpu001y"]-=.3
			else:
				thingsdata["pcpu001y"]+=.3
		# pcpu002 destination
		if pcpu002tmpdest[0]=="":
			pcpu002tmpdest[0]=random.randint(minw,maxw) # temp X destination for pcpu001
			pcpu002tmpdest[1]=random.randint(minh,maxh) # temp Y destination for pcpu001
		# X destination
		if pcpu002tmpdest[0]-1<thingsdata["pcpu002x"]<pcpu002tmpdest[0]+1:
			pcpu002tmpdest[0]=random.randint(minw,maxw)
		else:
			if thingsdata["pcpu002x"]>pcpu002tmpdest[0]:
				thingsdata["pcpu002x"]-=.3
			else:
				thingsdata["pcpu002x"]+=.3
		# Y destination
		if pcpu002tmpdest[1]-1<thingsdata["pcpu002y"]<pcpu002tmpdest[1]+1:
			pcpu002tmpdest[1]=random.randint(minh,maxh)
		else:
			if thingsdata["pcpu002y"]>pcpu002tmpdest[1]:
				thingsdata["pcpu002y"]-=.3
			else:
				thingsdata["pcpu002y"]+=.3

		if near(thingsdata["pcpu001x"],thingsdata["pcpu001y"]):
			txt(langr["instr"]["ettalk"],30,0,0)
			if pressed[pygame.K_e]:
				talk(pcpu001n,random.choice(list(langr["vincentmangiolli"]["dialog"].items()))[1])
		if near(thingsdata["pcpu002x"],thingsdata["pcpu002y"]):
			txt(langr["instr"]["ettalk"],30,0,0)
			if pressed[pygame.K_e]:
				talk(pcpu002n,random.choice(list(langr["nicolaiavmenise"]["dialog"].items()))[1].replace("R","V").replace("r","v"))

		thingsd={"player":playery,"pcpu001":thingsdata["pcpu001y"],"pcpu002":thingsdata["pcpu002y"]}
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
if __name__=="__main__":
	main()