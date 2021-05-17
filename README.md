# Everbright's Contenders

Bonjour et bienvenue dans le dossier du jeu EVERBRIGHT'S CONTENDERS.

C'est un jeu de joute verbale 2 joueurs en python opposant plusieurs héros s'affrontant pour gagner du pouvoir et de l'influence.

L'histoire se passe en parallèle de l'histoire du prince démon ( disponible ici https://github.com/Eyvve/Le-prince-demon-DEMO/releases/tag/DEMO-1.4 )

Le jeu comporte à ce jour :
- 4 champions avec leur cartes uniques
- 77 mots plus ou moins efficaces en fonction de l'adversaire
- 36 cartes à 3 niveau de rareté (Argent, Bronze et Acier)
- Un système de confiance pouvant retourner n'importe quelle situation
- Une carte de rareté Cosmique pouvant déterminer instantanément l'issue du round


## INSTALLATION

### VERSION IDE / CMD

L'installation de l'interpréteur Python (3.9 de préférence) est obligatoire et est disponible à cette adresse https://www.python.org/downloads/

Vous devez ensuite installer la librairie PyGame dont le processus d'installation est résumé ici https://www.pygame.org/wiki/GettingStarted

Pour lancer le jeu, vous devez entrer dans votre powershell le chemin de votre dossier de jeu : 
pour vous y rendre faites cd .\"votre chemin "\ par exemple, sur mon pc j'entre :

          cd .\PycharmProjects\Everbright_Contenders\

Une fois dans mon dossier de jeu, lancez le script main.py, pour cela entrez:

          py .\main.py

Vous pouvez aussi le lancer via votre IDE favori en lançant le fichier "main.py"

### VERSION .EXE
double cliquez simplement sur "Everbright's Contenders.exe"
          
Bon jeu à vous.

## À PROPOS

### Le jeu
Everbright's Contenders est un jeu de joute verbale à 2 joueurs en local.

Les règles du jeu sont simples : 
La partie se déroule en 3 rounds, chaque round est dévisé en tours. Un round comporte au minimum 10 tours. Le premier joueur à remporter 2 rounds gagne.

### SYSTÈME DE CONFIANCE
Chaque joueur a une jauge, la jauge de confiance va représenter un multiplicateur en fin de partie qui va influer sur la puissance de la phrase. Des cartes peuvent booster la confiance du joueur ou faire baisser celle de l'adversaire. Chaque mot efficace rapporte 5 pts de confiance, les mots super efficaces rapportent 10pts.

Chaque joueur commence avec 0 pts de confiance par défaut (15 si faveurs de la foule)

La composition de la foule est alors révélée aux joueurs (voir ***Système de foule***)

### ROUNDS ET CARTES
Au début de chaque round, les joueurs se voient attribué 3 cartes d'avantage aléatoirement, l'une d'elle est une carte unique.

Le premier à jouer est **toujours** le joueur 1.

Au milieu de l'écran se trouve la liste de mots, chaque mot retiré est remplacé par un nouveau du même type. Il y en a donc toujours 10 parmis lesquels choisir:
- 3 Groupes nominaux
- 3 Groupes verbaux
- 2 compléments
- 2 conjonctions de coordination

Un "mot" est un mot seul ou groupe / brique de mots faisant partie d'une phrase.

Durant le tour, le joueur a le choix entre jouer une carte avantage ou choisir un mot. Le premier à atteindre 4 mots peut verouiller la partie, il reste donc 1 tour à l'adversaire. Il y à donc un avantage à finir sa phrase en premier. Une phrase peut comporter au maximum 8 mots.

### SYSTÈME DE FOULE
La foule fait partie d'un des plus gros aspects du jeu, selon le déroulement de la partie, son influence peut être décisive pour un joueur.

Au début de la partie, la composition de la foule est déterminée au hasard et est composée de plusieurs type de personnes :

- Soldats : supportent Liam et blâment Ambre  (conflit de style de vie)
- Erudits : supportent Ambre et blâment Crystal (conflit d'idées)
- Nobles : Supportent Alfred et blâment Liam (conflit de classe)
- Hors la loi : Supportent Crystal et blâment Alfred (conflit de justice)

Seuls les 2 type de personnes ayant les plus grandes des 4 parts pèsent dans la partie, cela va donc définir la tendance de la partie.

Si un personnage tombe sur une foule lui étant favorable, il aura un gain de confiance et pourra utiliser les cartes de foule.


Admettons que la foule est composée en grande majoritée de soldats et d'érudits et que les jouteurs sont Liam et Ambre :

- Les soldats supportent Liam et les érudits ne blament pas Liam : Bonus de foule
- Les soldats blâment Ambre et les érudits supportent Ambre : Rien car compensation

Si un personnage tombe sur une foule lui étant défavorable, il aura un malus de confiance et ne pourra pas utiliser les cartes de foule sauf si il utilise une carte lui permettant de changer ses attributs de foule.

### CALCUL DES POINTS
A la fin du round les points sont calculés, entrent en compte :

- La longueur de la phrase (+ long = + de points) :
    - chaque mot rapporte 50 points.
    - Un mot efficace (qui heurte l'age, la classe sociale ou le sexe) rapporte 50pts supplémentaires.
    - Un mot très efficace (unique à l'adversaire) rapporte 100pts supplémentaires.
    - un mot innefficace rapporte 25.
- les points de confiance (/100) + 1 -> 30 points de confiance donnent un multiplicateur final de 1,3.

# BON JEU !
