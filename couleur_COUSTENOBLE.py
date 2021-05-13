# informations liées au groupe: Cyrian COURCHAMP, Antoine COUSTENOBLE, Bryan AECK, Matteo COTARD, Sofiya RUGA
#Groupe: BITD03
# Github: https://github.com/uvsq22003905/IN200-Projet2


# import des librairies
import tkinter as tk
import random as rd


#fonctions

def start():
  #démarre le jeu en envoyant la fonction du décompte du temps et de l'affichage des boutons de couleur et du mot
  decompte()
  affichage_boutons()

def reinitialiser():
  #réinitialise le jeu en effaçant le dernier mot et en remettant le compte à rebours au temps maximum et le score à 0
  global compteur_rebours, compteur, ScoreLabel2,timerLabel2, Mot, a
  compteur=0
  compteur_rebours=5
  Mot.destroy()
  ScoreLabel2.destroy()
  ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
  ScoreLabel2.place(x=300,y=80)
  timerLabel2.destroy()
  timerLabel2= tk.Label(racine, text=compteur_rebours,font=("papyrus",11))
  timerLabel2.place(x=360, y=110)
  a=0

def affichage_boutons():
  #affiche les boutons de couleur et le mot
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

def decompte():
  #lance le compte à rebours et quand il arrive à 0 enregistre le score dans un fichier
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
    #compteur_rebours="STOP"

def red():
  #ajoute un point au score si le mot était rouge et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, a
  if Rand==0 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
  changement_mot()

def blue():
  #ajoute un point au score si le mot était bleu et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, compteur_rebours, a
  if Rand==1 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
    Mot.destroy()
  changement_mot()

def green():
  #ajoute un point au score si le mot était vert et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, a
  if Rand==2 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
  changement_mot()

def pink():
  #ajoute un point au score si le mot était rose et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, a
  if Rand==3 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
  changement_mot()

def orange():
  #ajoute un point au score si le mot était orange et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, a
  if Rand==4 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
  changement_mot()

def yellow():
  #ajoute un point au score si le mot était jaune et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, a
  if Rand==5 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
  changement_mot()

def white():
  #ajoute un point au score si le mot était blanc et lance la fonction du changement de mot
  global compteur, ScoreLabel2, Rand, a
  if Rand==6 and compteur_rebours!=0 and compteur_rebours!="STOP" and a==1:
    compteur+=1
    ScoreLabel2.destroy()
    ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
    ScoreLabel2.place(x=300,y=80)
  changement_mot()

def changement_mot():
  #efface le mot et en remet un nouveau de texte et couleur au hasard
  global Mot, Rand, Rand2, a
  if compteur_rebours!="STOP" and a==1:
    Mot.destroy()
    Rand=rd.randint(0,6)
    Rand2=rd.randint(0,6)
    Mot= tk.Label(racine, text=listNo[Rand2],foreground=listCo[Rand],font=("Arial",30))
    Mot.place(x=250,y=150)

def meilleurs():
  #affiche les 3 meilleurs scores
  fic = open ("scores.txt", "r")
  ligne = fic.readline()
  list=ligne.split()
  for i in range (0,len(list)):
    list[i]=int(list[i])
  list.sort()
  print(list[-10:])
  fic.close()


#programme principal

a=0
compteur=0
compteur_rebours=5
list_scores=[]
listCo=["red","blue","green","pink","orange","yellow","white"]
listNo=['RED','BLUE','GREEN','PINK','ORANGE','YELLOW','WHITE']
Rand=rd.randint(0,6)
Rand2=rd.randint(0,6)

racine=tk.Tk()
canvas = tk.Canvas(racine, width=600, height=400) #creation de la fenetre

ScoreLabel= tk.Label(racine, text="Score:",font=("papyrus",11)).place(x=260,y=80)
ScoreLabel2= tk.Label(racine, text=compteur,font=("papyrus",11))
ScoreLabel2.place(x=300,y=80)

timerLabel= tk.Label(racine, text="Temps restant:",font=("papyrus",11)).place(x=260,y=110)
timerLabel2= tk.Label(racine, text=compteur_rebours,font=("papyrus",11))
timerLabel2.place(x=360, y=110)

text= tk.Label(racine, text="Cliquez sur le bouton correspondant à la couleur des mots, et pas au texte des mots!!!", font=("papyrus",11)).place(x=25,y=45)

Boutonrereinitialiser=tk.Button(racine, text="Reinitialiser",background="light grey",command=reinitialiser)  #Boutons usuels
Boutonrereinitialiser.place(x=485,y=350)

Boutongo=tk.Button(racine, text="GO",background="light grey",command=start)
Boutongo.place(x=25,y=350)

Bouton_meilleurscore=tk.Button(racine, text="10 Meilleurs Scores",background="light grey",command=meilleurs)  #Boutons usuels
Bouton_meilleurscore.place(x=250,y=380)

rectangle1=canvas.create_rectangle(0,0,20,400,fill="green", outline="green")
rectangle2=canvas.create_rectangle(0,0,600,20,fill="green", outline="green")
rectangle3=canvas.create_rectangle(580,0,600,400,fill="green", outline="green")
rectangle4=canvas.create_rectangle(0,380,600,400,fill="green", outline="green")


canvas.grid()


#fin programme
canvas.mainloop()




