#memory_game
#exemplaire

from tkinter import *
from random import randrange #pour afficher des images aléatoirement dans le menu (line 12--line16)
from random import shuffle
import pygame



#declaration
COTE=120 #dimensions
PAD=5 #padding entre les images
side=COTE+2*PAD #pour créer un ensemble des carreaux qui comporte les images
nb_lgn=4
nb_cl=5
nb_cartes=nb_lgn*nb_cl//2
LANG=['naruto','saski','kakashi','obito','conan','pain','hidan','itachi','zetso','diedra']
l=nb_cl*side
h=nb_lgn*side
X0=Y0=side/2



#fonction de mélange du grille
def melange_grille():
	Cartes=list(range(nb_cartes))*2
	shuffle(Cartes)

	p=[]
	k=0

	for lig in range(nb_lgn):
		L=[]
		for col in range(nb_cl):
			L.append(Cartes[k])
			k+=1
		p.append(L)
	return p



#fonction creation_logos
def creation_logos():
	logos=[]
	for lang in LANG:
		fichier="./images/" +lang+ ".gif"
		lg=PhotoImage(file=fichier)
		logos.append(lg)
	return logos



#fonction remplir
def remplir(plateau):
	ids_cover=[]
	#placement des images
	for lig in range(nb_lgn):
		m=[]
		for col in range(nb_cl):
			c=(col*side+X0,lig*side+Y0)
			num=plateau[lig][col]
			lg=logos[num]
			cnv.create_image(c,image=lg)
			id_cover=cnv.create_image(c,image=logo)
			m.append(id_cover)
		ids_cover.append(m)
	return ids_cover


#fonction click
def click(event):
	if move[1] is not None:
		return

	X=event.x
	Y=event.y
	col=X//side
	lig=Y//side

	if plateau[lig][col]!=-1:
		traiter_click(lig,col)


#fonction traiter_click
def traiter_click(lig,col):
	global cpt,couples
	item=ids_cover[lig][col]
	cnv.delete(item)
	if move[0] is None:
		move[0]=(lig,col)
	else:
		if move[0]==(lig,col):
			return
		cpt+=1
		lb['text']=cpt
		move[1]=(lig,col)
		i,j=move[0]
		if plateau[i][j]==plateau[lig][col]:
			plateau[i][j]=plateau[lig][col]=-1
			move[0]=move[1]=None

			#tester couples et applaudir
			couples+=couples
			if couples==nb_cartes:
				cnv.after(500,applaudir)
		else:
			cnv.after(400,cacher,i,j,lig,col)


#fonction cacher
def cacher(i,j,lig,col):
	c=(j*side+X0,i*side+Y0)
	ids_cover[i][j]=cnv.create_image(c,image=logo)
	c=(col*side+X0,lig*side+Y0)
	ids_cover[lig][col]=cnv.create_image(c,image=logo)
	move[0]=move[1]=None

#fonction applaudir
def applaudir():
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play(-1)




#fonction init
def init():
	global plateau,ids_cover,move,cpt,couples
	plateau=melange_grille() #appel du fonction melange_grille
	ids_cover=remplir(plateau)		#appel du fonction remplir
	move=[None,None]        #traiter_click
	cpt=0
	lb['text']=0
	couples=0

	pygame.mixer.music.stop()



#menu & appelle des fonction
fen=Tk()
fen.title('memory')
cnv=Canvas(fen,width=l,height=h,bg="gray")
cnv.pack(side=LEFT) #padx=20,pady=10
logo=PhotoImage(file="cover.gif")

#creation de label
lb=Label(fen,text=0,font="courier 20 bold")
lb.pack(padx=20,pady=20)

#initialisation de pygame
pygame.mixer.init()
pygame.mixer.music.load("applause.wav")


logos=creation_logos()	#appel du fonction creation_logos
init() #appel du fonction init


#creation du button
btn=Button(fen,text="Nouveau",command=init)
btn.pack(padx=10,pady=10)



cnv.bind('<Button>',click) #click

fen.mainloop()