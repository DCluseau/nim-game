#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nim_functions

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




player_1["name"] = str(input("Please input player 1's name : \n"))

# Choosing type of game and who begins
who_begins = 0
while play_mode not in range(1,3):
    play_mode = nim_functions.choose_play_mode()
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
nim_functions.display_grid(21)
if who_begins == 2:
    if play_mode == 1:
        nb_of_remaining_matches = nim_functions.update_nb_matches(4, nb_of_remaining_matches)
        print("Computer's turn")
    else:
        nb_to_remove = nim_functions.player_choose_matches(players_list[1])
        nb_of_remaining_matches = nim_functions.update_nb_matches(nb_to_remove, nb_of_remaining_matches)
while nb_of_remaining_matches > 0:
    for i in range(0, 2):
        nim_functions.display_grid(nb_of_remaining_matches)
        if nb_of_remaining_matches > 0:
            if play_mode == 1:
                if  i == 1:
                    print("Computer's turn")
                    nb_of_remaining_matches = nim_functions.update_nb_matches(5 - nb_matches_removed, nb_of_remaining_matches)
                else:
                    nb_to_remove = nim_functions.player_choose_matches(players_list[i])
                    nb_matches_removed = nb_to_remove
                    nb_of_remaining_matches = nim_functions.update_nb_matches(nb_to_remove, nb_of_remaining_matches)
                if nb_of_remaining_matches < 1:
                    players_list[i]["score"] = "Perdu !"
            else:
                nb_to_remove = nim_functions.player_choose_matches(players_list[i])
                nb_of_remaining_matches = nim_functions.update_nb_matches(nb_to_remove, nb_of_remaining_matches)
                if nb_of_remaining_matches < 1:
                    players_list[i]["score"] = "Perdu !"
        if i == 1:
            i = 0
        else:
            i = 1
print("Scores : ")
print(f"{player_1["name"]} : {player_1["score"]}")
print(f"{player_2["name"]} : {player_2["score"]}")

