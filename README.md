# Jeu de Nim

- [But du jeu](#but-du-jeu)
- [Règles](#regles)
- [Variantes](#variantes)
- [Utilisation](#utilisation)

## But du jeu
Deux jouers s'affrontent en enlevant des allumettes d'un tas. Le perdant est celui qui enlève la dernière allumette.

## Règles
- Le jeu se joue à deux ou bien contre l'ordinateur
- Chaque joueur enlève de 1 à 4 allumettes du ou des tas, selon les variantes
- Il n'est pas possible d'enlever moins de 1 allumette et plus de 4 allumettes
- Il n'est pas possible de passer son tour
- La partie s'arrête lorsque la dernière allumette a été enlevée

## Variantes
- Variante classique : Deux joueurs s’affrontent dans ce jeu en se partageant un tas d’allumettes composé au départ de 21 allumettes. Chaque joueur à son tour enlève entre une et quatre allumettes du tas. Celui qui enlève la dernière allumette a perdu.

- Variante dite de Marienbad : il y a au départ quatre tas, avec respectivement 1, 3, 5 et 7 allumettes. À chaque tour, le joueur (dont c'est le tour) prend le nombre d'allumettes qu'il veut, au moins une et dans un même tas. Celui qui prend la dernière allumette perd. Permettre dans un premier temps d’arbitrer une telle partie entre deux joueurs humains, puis proposer de pouvoir jouer contre l’ordinateur appliquant une stratégie de votre cru (peu importe s’il ne joue pas très bien).

## Utilisation
- Installer Python v3
- Lancer le fichier main.py dans une console
- Sélectionner la variante à laquelle vous voulez jouer
- Indiquez contre quel adversaire vous voulez jouer
- Entrer le ou les noms des joueurs
- Choisissez qui commence
- Selon les variantes :
  - Classique : chacun attend son tour puis entre combien d'allumettes il veut enlever
  - Marienbad : chacun attend son tour puis indique dans quelle pile il veut enlever des allumettes ainsi que combien il en enlève
