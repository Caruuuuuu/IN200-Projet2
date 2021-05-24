# informations liées au groupe: Cyrian COURCHAMP, Antoine COUSTENOBLE, Bryan AECK, Matteo COTARD, Sofiya RUGA
#Groupe: BITD03
# Github: https://github.com/uvsq22003905/IN200-Projet2


import tkinter as tk
import random as rd


#fonctions

def start():
  #démarre le jeu niveau 1 en envoyant la fonction du décompte du temps et de l'affichage des boutons de couleur et du mot
  decompte()
  affichage_boutons()


def start_niveau2():
  #démarre le jeu niveau 2 en envoyant la fonction du décompte du temps, de l'affichage des boutons de couleur et de l'affichage des 3 mots
  decompte2()
  affichage_boutons2()
  affichage_mots_multiples()


##Partie faite par Mattéo et Bryan

def reinitialiser():
  #réinitialise le jeu niveau 1 en effaçant le dernier mot et en remettant le compte à rebours au temps maximum et le score à 0
  global compteur_rebours, compteur, ScoreLabel2,timerLabel2, Mot, a, list_affich_mots
  compteur=0
  compteur_rebours=20
  Mot.destroy()
  ScoreLabel2.destroy()
  ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
  ScoreLabel2.place(x=300,y=80)
  timerLabel2.destroy()
  timerLabel2= tk.Label(racine, text=compteur_rebours,font=("papyrus",11))
  timerLabel2.place(x=360, y=110)
  a=0


def reinitialiser2():
  #réinitialise le jeu niveau 2 en effaçant les 3 mots et en remettant le compte à rebours au temps maximum et le score à 0
  global compteur_rebours, compteur, ScoreLabel2,timerLabel2, a, list_affich_mots
  compteur=0
  compteur_rebours=20
  for i in range (0,3):
     list_affich_mots[i].destroy()
  list_affich_mots = []
  ScoreLabel2.destroy()
  ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
  ScoreLabel2.place(x=300,y=80)
  timerLabel2.destroy()
  timerLabel2= tk.Label(racine, text=compteur_rebours,font=("papyrus",11))
  timerLabel2.place(x=360, y=110)
  a=0

##Partie faite par Sofiya

def affichage_boutons():
  #affiche les boutons de couleur et le mot pour le niveau 1
  global Mot, a
  Boutonred=tk.Button(racine, text=listCo[0],background="red",command=red)  #Boutons usuels
  Boutonred.place(x=118,y=280)
  Boutonblue=tk.Button(racine, text=listCo[1],background="blue",command=blue)  #Boutons usuels
  Boutonblue.place(x=158,y=280)
  Boutongreen=tk.Button(racine, text=listCo[2],background="green",command=green)  #Boutons usuels
  Boutongreen.place(x=203,y=280)
  Boutonpink=tk.Button(racine, text=listCo[3],background="pink",command=pink)  #Boutons usuels
  Boutonpink.place(x=256,y=280)
  Boutonorange=tk.Button(racine, text=listCo[4],background="orange",command=orange)  #Boutons usuels
  Boutonorange.place(x=299,y=280)
  Boutonyellow=tk.Button(racine, text=listCo[5],background="yellow",command=yellow)  #Boutons usuels
  Boutonyellow.place(x=363,y=280)
  Boutonwhite=tk.Button(racine, text=listCo[6],background="white",command=white)  #Boutons usuels
  Boutonwhite.place(x=425,y=280)
  Mot=tk.Label(racine, text=listNo[Rand2],foreground=listCo[Rand],font=("Arial",30))
  Mot.place(x=250,y=150)
  a=1

##Partie faite par Bryan

def decompte():
  #lance le compte à rebours pour le niveau 1 et quand il arrive à 0 enregistre le score dans le fichier scores
  global compteur_rebours, timerLabel2, compteur, list_scores
  if compteur_rebours!=0:
    compteur_rebours-=1
    timerLabel2.destroy()
    timerLabel2= tk.Label(racine, text=compteur_rebours,font=("papyrus",11))
    timerLabel2.place(x=360, y=110)
    canvas.after(1000,decompte)
  if compteur_rebours==0:
    fic = open ("scores.txt", "r")
    ligne = fic.readline()
    list_scores=ligne.split()
    for i in range (0,len(list_scores)):
      list_scores[i]=int(list_scores[i])
    fic.close()
    fic = open ("scores.txt", "w")
    list_scores.append(compteur)
    for i in range (0,len(list_scores)):
      fic.write(str(list_scores[i])+" ")
    fic.close()


def decompte2():
  #lance le compte à rebours pour le niveau 2 et quand il arrive à 0 enregistre le score dans le fichier scores_niveau2
  global compteur_rebours, timerLabel2, compteur, list_scores2
  if compteur_rebours!=0:
    compteur_rebours-=1
    timerLabel2.destroy()
    timerLabel2= tk.Label(racine, text=compteur_rebours,font=("papyrus",11))
    timerLabel2.place(x=360, y=110)
    canvas.after(1000,decompte2)
  if compteur_rebours==0:
    fic2 = open ("scores_niveau2.txt", "r")
    ligne = fic2.readline()
    list_scores2=ligne.split()
    for i in range (0,len(list_scores2)):
      list_scores2[i]=int(list_scores2[i])
    fic2.close()
    fic2 = open ("scores_niveau2.txt", "w")
    list_scores2.append(compteur)
    for i in range (0,len(list_scores2)):
      fic2.write(str(list_scores2[i])+" ")
    fic2.close()

##Partie faite par Cyrian

def red():
  #niveau 1: ajoute un point au score si le mot était rouge et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, a
  if Rand==0 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
  changement_mot()

def blue():
  #niveau 1: ajoute un point au score si le mot était bleu et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, compteur_rebours, a
  if Rand==1 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
    Mot.destroy()
  changement_mot()

def green():
  #niveau 1: ajoute un point au score si le mot était vert et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, a
  if Rand==2 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
  changement_mot()

def pink():
  #niveau 1: ajoute un point au score si le mot était rose et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, a
  if Rand==3 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
  changement_mot()

def orange():
  #niveau 1: ajoute un point au score si le mot était orange et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, a
  if Rand==4 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
  changement_mot()

def yellow():
  #niveau 1: ajoute un point au score si le mot était jaune et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, a
  if Rand==5 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
  changement_mot()

def white():
  #niveau 1: ajoute un point au score si le mot était blanc et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, a
  if Rand==6 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
  changement_mot()

##Partie faite par Mattéo

def changement_mot():
  #efface le mot du niveau 1 et en remet un nouveau de texte et couleur au hasard
  global Mot, Rand, Rand2, a
  if compteur_rebours!="STOP" and a==1:
    Mot.destroy()
    Rand=rd.randint(0,6)
    Rand2=rd.randint(0,6)
    Mot= tk.Label(racine, text=listNo[Rand2],foreground=listCo[Rand],font=("Arial",30))
    Mot.place(x=250,y=150)

##Partie faite par Antoine et Cyrian

def meilleurs():
  #affiche les 10 meilleurs scores du niveau 1
  fic = open ("scores.txt", "r")
  ligne = fic.readline()
  list=ligne.split()
  for i in range (0,len(list)):
    list[i]=int(list[i])
  list.sort()
  print(list[-10:])
  fic.close()

def meilleurs2():
  #affiche les 10 meilleurs scores du niveau 2
  fic2 = open ("scores_niveau2.txt", "r")
  ligne = fic2.readline()
  list=ligne.split()
  for i in range (0,len(list)):
    list[i]=int(list[i])
  list.sort()
  print(list[-10:])
  fic2.close()

##Partie faite par Mattéo

def affichage_mots_multiples():
  #affiche 3 mots pour le niveau 2
  global a, list_mots, listCo, listNo, list_affich_mots
  for i in range (0, 3):
    Rand=rd.randint(0,6)
    Rand2=rd.randint(0,6)
    Mot=tk.Label(racine, text=listNo[Rand2],foreground=listCo[Rand],font=("Arial",20))
    Mot.place(x=(100+i*150),y=150)
    list_affich_mots.append(Mot)
    list_mots.append(listCo[Rand])
  a=1

##Partie faite par Sofiya

def affichage_boutons2():
  #affiche les boutons de couleur pour le niveau 2
  Boutonred=tk.Button(racine, text=listCo[0],background="red",command=red2)  #Boutons usuels
  Boutonred.place(x=118,y=280)
  Boutonblue=tk.Button(racine, text=listCo[1],background="blue",command=blue2)  #Boutons usuels
  Boutonblue.place(x=158,y=280)
  Boutongreen=tk.Button(racine, text=listCo[2],background="green",command=green2)  #Boutons usuels
  Boutongreen.place(x=203,y=280)
  Boutonpink=tk.Button(racine, text=listCo[3],background="pink",command=pink2)  #Boutons usuels
  Boutonpink.place(x=256,y=280)
  Boutonorange=tk.Button(racine, text=listCo[4],background="orange",command=orange2)  #Boutons usuels
  Boutonorange.place(x=299,y=280)
  Boutonyellow=tk.Button(racine, text=listCo[5],background="yellow",command=yellow2)  #Boutons usuels
  Boutonyellow.place(x=363,y=280)
  Boutonwhite=tk.Button(racine, text=listCo[6],background="white",command=white2)  #Boutons usuels
  Boutonwhite.place(x=425,y=280)


##Partie faite par Cyrian et Antoine

def red2():
  #niveau 2: ajoute rouge à la liste list_couleur et lance la fonction score2
  global compteur_rebours, a, list_couleurs
  if compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    list_couleurs.append("red")
    score2()
def blue2():
  #niveau 2: ajoute blue à la liste list_couleur et lance la fonction score2
  global compteur_rebours, a, list_couleurs
  if compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    list_couleurs.append("blue")
    score2()
def green2():
  #niveau 2: ajoute green à la liste list_couleur et lance la fonction score2
  global compteur_rebours, a, list_couleurs
  if compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    list_couleurs.append("green")
    score2()
def pink2():
  #niveau 2: ajoute pink à la liste list_couleur et lance la fonction score2
  global compteur_rebours, a, list_couleurs
  if compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    list_couleurs.append("pink")
    score2()
def orange2():
  #niveau 2: ajoute orange à la liste list_couleur et lance la fonction score2
  global compteur_rebours, a, list_couleurs
  if compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    list_couleurs.append("orange")
    score2()
def yellow2():
  #niveau 2: ajoute yellow à la liste list_couleur et lance la fonction score2
  global compteur_rebours, a, list_couleurs
  if compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    list_couleurs.append("yellow")
    score2()
def white2():
  #niveau 2: ajoute white à la liste list_couleur et lance la fonction score2
  global compteur_rebours, a, list_couleurs
  if compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    list_couleurs.append("white")
    score2()


def score2():
  #niveau 2: ajoute un poin au score si les couleurs des 3 mots ont été correctement choisies puis efface ces 3 mots et envoie vers affichage_mots_multiples pour en afficher 3 nouveaux
  global list_mots, list_couleurs, nb_clics, compteur, ScoreLabel2, list_affich_mots
  nb_clics+=1
  if nb_clics == 3:
    if list_mots == list_couleurs:
      compteur+=1
      ScoreLabel2.destroy()
      ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
      ScoreLabel2.place(x=300,y=80)
    for i in range (0,3):
     list_affich_mots[i].destroy()
    list_affich_mots = []
    nb_clics=0
    list_couleurs = []
    list_mots = []
    affichage_mots_multiples()


#programme principal fait par Antoine et Sofiya

score=0
nb_clics=0
a=0
compteur=0
compteur_rebours=20
list_couleurs=[]
list_scores=[]
list_scores2=[]
list_affich_mots=[]
listCo=["red","blue","green","pink","orange","yellow","white"]
listNo=['RED','BLUE','GREEN','PINK','ORANGE','YELLOW','WHITE']
Rand=rd.randint(0,6)
Rand2=rd.randint(0,6)
list_mots=[]

racine=tk.Tk()
canvas = tk.Canvas(racine, width=600, height=400) #creation de la fenetre

ScoreLabel= tk.Label(racine, text="Score:",font=("papyrus",11)).place(x=260,y=80)
ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
ScoreLabel2.place(x=300,y=80)

timerLabel= tk.Label(racine, text="Temps restant:",font=("papyrus",11)).place(x=260,y=110)
timerLabel2= tk.Label(racine, text=compteur_rebours,font=("papyrus",11))
timerLabel2.place(x=360, y=110)

text= tk.Label(racine, text="Cliquez sur le bouton correspondant à la couleur des mots, et pas au texte des mots!!!", font=("papyrus",11)).place(x=25,y=45)

Boutonrereinitialiser=tk.Button(racine, text="Reinitialiser Niveau1",background="light grey",command=reinitialiser)  #Boutons usuels
Boutonrereinitialiser.place(x=425,y=350)
Boutonrereinitialiser=tk.Button(racine, text="Reinitialiser Niveau2",background="light grey", command=reinitialiser2)  #Boutons usuels
Boutonrereinitialiser.place(x=425,y=320)

Boutongo=tk.Button(racine, text="GO-niveau1",background="light grey",command=start)
Boutongo.place(x=25,y=350)
Boutongo2=tk.Button(racine, text="GO-niveau2",background="light grey", command=start_niveau2)
Boutongo2.place(x=25,y=320)

Bouton_meilleurscore=tk.Button(racine, text="10 best Niveau1",background="light grey",command=meilleurs)  #Boutons usuels
Bouton_meilleurscore.place(x=140,y=350)
Bouton_meilleurscore=tk.Button(racine, text="10 best Niveau2",background="light grey",command=meilleurs2)  #Boutons usuels
Bouton_meilleurscore.place(x=280,y=350)

rectangle1=canvas.create_rectangle(0,0,20,400,fill="green", outline="green")
rectangle2=canvas.create_rectangle(0,0,600,20,fill="green", outline="green")
rectangle3=canvas.create_rectangle(580,0,600,400,fill="green", outline="green")
rectangle4=canvas.create_rectangle(0,380,600,400,fill="green", outline="green")

canvas.grid()


#fin programme
canvas.mainloop()




