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

# Number of matches the player can take
MATCH_MIN = 1
MATCH_MAX = 4
NUMBER_OF_MATCHES = 21

# Players' scores (user and computer)
player_1 = {"name": "", "score": 0}
player_2 = {"name": "", "score": 0}
players_list = [player_1, player_2]
nb_of_remaining_matches = 21

def display_grid():
    """
    usage : displaying grid
    :return:
    """
    grid = []
    print(grid)

def remove_match(match_to_remove, rest_nb_matches):
    """

    :param rest_nb_matches:
    :param match_to_remove:
    :return:
    """
    match_to_remove = 1
    rest_nb_matches -= match_to_remove

    return nb_of_remaining_matches


