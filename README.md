# IN200-Projet2
Dépot du projet 2 d'IN200. Groupe de Mattéo, Bryan, Sofiya, Cyrian et Antoine du BITD03

Mise en place du programme:
Téléchargez les fichiers ( dans un même dossier )  ---> couleur_AECK.py , scores.txt et scores_niveau2.txt 

Fonctionnement du jeu et utilisation du programe :

Dans ce jeu, différents noms de couleurs seront affichés avec différentes couleurs de texte.
Ici, dans ce jeu, le rôle d'un joueur est de choisir la bonne couleur du mot qui s'affiche à
l'écran. Chaque fois que le joueur choisi la bonne couleur, le score sera incrémenté de un. La
durée du jeu sera de 20 secondes et les boutons de couleurs utilisées dans ce jeu sont le
rouge, le bleu, le vert, le rose, le jaune, l’orange et le blanc.

Le jeu se décompose en plusieurs niveaux, les niveaux 1 (Un seul mot) et 2 (Trois mots à la suite).

Après avoir lancé le programme, une fenêtre Tkinter apparaîtra avec divers boutons.

Niveau 1:

-	Pour commencer le jeu niveau 1, cliquer sur le bouton GO-niveau1.
-	Un mot apparait et le compte à rebours, fixé à 20 secondes, se déclenche.
-	Il faut alors cliquer sur les boutons de couleur et sélectionner la couleur avec laquelle le mot est écrit et non pas la couleur écrite.
-	Si le choix est correct, le score ajoute un point. Sinon, le score ne change pas et un nouveau mot est présenté.
-	Le but du jeu est d’obtenir le plus haut score en 20 secondes.
-	Une fois le compteur à rebours arrivé à 0, le score est enregistré dans le fichier text scores.txt. On peu continuer de cliquer sur les boutons de couleur mais cela n’ajoutera pas de point au score.
-	Pour remettre les paramètres de score et de temps à 0, il faut cliquer sur reinitialiser niveau 1.  Cela enlèvera le mot qui était affiché. Si on clique sur des boutons, cela n’ajoutera rien au score.
-	Pour relancer une partie cliquer à nouveau sur GO-niveau1.
-	Pour afficher les 10 meilleurs scores du niveau 1, cliquer sur 10 best Niveau1 (affichage des scores dans l'espace de la console python sous forme d'une liste)

Niveau 2:

-	Pour commencer le jeu niveau 2, cliquer sur le bouton GO-niveau2.
-	3 mots apparaissent et le compte à rebours, fixé à 20 secondes, se déclenche.
-	Il faut alors cliquer sur les 3 boutons correspondant aux bonnes couleurs. Il faut donc sélectionner les bons boutons dans l'ordre correspondant à l'ordre d'affichage des couleurs à l'écran (de gauche à droite).
-	Si les 3 choix sont corrects, le score ajoute un point. Sinon, le score ne change pas et 3 nouveaux mots sont présentés.
-	Le but du jeu est d’obtenir le plus haut score en 20 secondes.
-	Une fois le compteur à rebours est arrivé à 0, le score est enregistré dans le fichier text scores_niveau2. On peu continuer de cliquer sur les boutons de couleur mais cela n’ajoutera pas de point au score.
-	Pour remettre les paramètres de score et de temps à 0, il faut cliquer sur reinitialiser niveau 2.  Cela enlèvera les 3 mots qui étaient affichés. Si on clique sur des boutons, cela n’ajoutera rien au score.
-	Pour relancer une partie cliquer à nouveau sur GO-niveau2.
-	Pour afficher les 10 meilleurs scores du niveau 2, cliquer sur 10 best Niveau2

