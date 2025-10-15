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

# Players' scores (users and/or computer)
player_1 = {"name": "", "score": "Gagné !"}
player_2 = {"name": "", "score": "Gagné ! "}
# List of players
players_list = [player_1, player_2]
# Number of remaining matches
nb_of_remaining_matches = 21
# Number of matches the user just removed (for calculating of many matches the computer removes)
nb_matches_removed = 0
play_mode = 0


def display_grid(nb_matches):
    """
    usage : displaying grid

    :param nb_matches:
        Total number of matches to display
    :return:
    """
    grid = ""
    for diff_matches in range(NUMBER_OF_MATCHES - nb_matches):
        grid += f" "
    for diff_matches in range(nb_matches):
        grid += f" | "
    print(f"{grid}")

def update_nb_matches(removed_matches, remaining_matches):
    """
    usage : update the number of remaining matches

    :param removed_matches:
        number of matches to remove
    :param remaining_matches:
        number of remaining matches before removing the other number
    :return:
    """
    remaining_matches -= removed_matches
    return remaining_matches

def choose_play_mode():
    """
    usage : choose if the user plays against the computer or against another user

    :return:
    """
    try:
        choice = int(input("Please enter which type of game you want to play : \n1 - Against the computer \n2 - Against another player\n"))
    except ValueError:
        choice = 0

    return choice

def player_choose_matches(player):
    nb_matches = 0
    while nb_matches not in range(1, 5):
        try:
            print(f"{player["name"]}'s turn")
            nb_matches = int(input(f"{player["name"]}, how many matches do you want to remove ? "))
        except ValueError:
            nb_matches = 0
            print("Error : value must be a number between 1 and 4.")
    return nb_matches

player_1["name"] = str(input("Please input player 1's name : \n"))

# Choosing type of game and who begins
who_begins = 0
while play_mode not in range(1,3):
    play_mode = choose_play_mode()
    if play_mode == 1:
        player_2["name"] = "computer"
        while who_begins not in range(1, 3):
            try:
                who_begins = int(input("Please choose which player will begin : (1 or 2) \n"))
            except ValueError:
                print("Error : choice must be a number between 1 and 2.")
    elif play_mode == 2:
        player_2["name"] = str(input("Please input player 2's name : \n"))
        while who_begins not in range(1, 3):
            try:
                who_begins = int(input("Please choose which player will begin : (1 or 2) \n"))
            except ValueError:
                print("Error : choice must be a number between 1 and 2.")
    else:
        print("Error : choice must be a number between 1 and 2.")

# Beginning game
display_grid(21)
if who_begins == 2:
    if play_mode == 1:
        nb_of_remaining_matches = update_nb_matches(4, nb_of_remaining_matches)
        print("Computer's turn")
    else:
        nb_to_remove = player_choose_matches(players_list[1])
        nb_of_remaining_matches = update_nb_matches(nb_to_remove, nb_of_remaining_matches)
while nb_of_remaining_matches > 0:
    for i in range(0, 2):
        display_grid(nb_of_remaining_matches)
        if nb_of_remaining_matches > 0:
            if play_mode == 1:
                if  i == 1:
                    print("Computer's turn")
                    nb_of_remaining_matches = update_nb_matches(5 - nb_matches_removed, nb_of_remaining_matches)
                else:
                    nb_to_remove = player_choose_matches(players_list[i])
                    nb_matches_removed = nb_to_remove
                    nb_of_remaining_matches = update_nb_matches(nb_to_remove, nb_of_remaining_matches)
                if nb_of_remaining_matches < 1:
                    players_list[i]["score"] = "Perdu !"
            else:
                nb_to_remove = player_choose_matches(players_list[i])
                nb_of_remaining_matches = update_nb_matches(nb_to_remove, nb_of_remaining_matches)
                if nb_of_remaining_matches < 1:
                    players_list[i]["score"] = "Perdu !"
        if i == 1:
            i = 0
        else:
            i = 1
print("Scores : ")
print(f"{player_1["name"]} : {player_1["score"]}")
print(f"{player_2["name"]} : {player_2["score"]}")

