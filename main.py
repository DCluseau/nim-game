#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Jeu de Nim ##

# Deux joueurs s’affrontent dans ce jeu en se partageant un tas d’allumettes composé au départ de 21 allumettes.
# Chaque joueur à son tour enlève entre une et quatre allumettes du tas. Celui qui enlève la dernière allumette a perdu.
# Le programme doit arbitrer une partie se déroulant entre deux joueurs humains, dont leur nom est demandé au démarrage,
# ainsi que le joueur qui commence.

# Optionnel : donner la possibilité à un joueur humain de jouer contre l'ordinateur appliquant la stratégie suivante :
# • premier cas : le joueur démarre la partie : quand le joueur enlève k allumettes, l'ordinateur en enlève 5 - k, ce
# qui entraîne fatalement le joueur à enlever la dernière allumette ;
# • deuxième cas : l'ordinateur démarre la partie : se ramener dès que possible au cas précédent (ce qui ne sera bien
# sûr possible que si le joueur ne connait pas la stratégie gagnante exposée dans le premier cas).

# Optionnel : ajouter la variante du jeu de Marienbad1, dans laquelle il y a au départ quatre tas, avec respectivement
# 1, 3, 5 et 7 allumettes. À chaque tour, le joueur (dont c'est le tour) prend le nombre d'allumettes qu'il veut, au
# moins une et dans un même tas. Celui qui prend la dernière allumette perd.
# Permettre dans un premier temps d’arbitrer une telle partie entre deux joueurs humains, puis proposer de pouvoir
#  jouer contre l’ordinateur appliquant une stratégie de votre cru (peu importe s’il ne joue pas très bien).

###

game_variant = 0
while game_variant == 0:
    try:
        game_variant = int(input("Please choose the variant of the Nim game you want to play : \n 1 - Normal variant\n 2 - Marienbad variant\n"))
    except ValueError:
        print("Error : choice must be a number between 1 and 2")
        game_variant = 0
    if game_variant not in range (1, 3):
        print("Error : choice must be a number between 1 and 2")
        game_variant = 0
if game_variant == 1:
    import nim_games
else:
    import nim_marienbad