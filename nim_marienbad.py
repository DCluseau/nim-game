#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Constants
MATCH_MIN = 1
MATCH_MAX = 4
NUMBER_OF_MATCHES = 16
PILES = [1, 3, 5, 7]

# Variables
piles_grid = list(PILES)
nb_pile_remove = 0
nb_matches_left = 16
# Players' scores (users and/or computer)
player_1 = {"name": "", "score": "Gagné !"}
player_2 = {"name": "", "score": "Gagné ! "}
# List of players
players_piles_list = [player_1, player_2]

# Display piles
def display_piles(grid):
    """
    Display grid of piles
    :param grid:
    :return:
    """
    for pile in range(len(grid)):
        display = ""
        for match in range(grid[pile]):
            display += f" | "
        print(f"{display}")

# Name players
def name_player(player):
    """

    :param player:
    :return:
    """
    player["name"] = str(input("Please input player 1's name : \n"))
    return player

# Choose number of matches to remove
def player_choose_matches(player, pile):
    nb_matches_to_remove = 0
    while nb_matches_to_remove not in range(1, pile + 1):
        try:
            # print(f"{player["name"]}'s turn")
            # print(f"Number of matches left : {pile}")
            nb_matches_to_remove = int(input(f"{player["name"]}, how many matches do you want to remove ? "))
        except ValueError:
            nb_matches_to_remove = 0
            print(f"Error : value must be a number between 1 and {pile}.")
    return nb_matches_to_remove

# Choose pile to modify
def player_choose_pile(piles_left):
    pile_number = -1
    while pile_number == -1:
        try:
            pile_number = int(input("Which pile do you want to choose ?\n")) - 1
        except ValueError:
            print("Error : number must be between 1 and 4 and has to have at least one match left.")
        if pile_number not in range(0, 4):
            print("Error : number must be between 1 and 4 and has to have at least one match left.")
            pile_number = -1
        elif piles_left[pile_number] == 0:
                print("Error : 0 matches left in this pile.")
                pile_number = -1
    return pile_number

# Computer removes matches
def computer_choice(tab_pile):
    computer_pile_choice = -1
    for j in range(4):
        if tab_pile[j] > 0 and computer_pile_choice == -1:
            computer_pile_choice = j
    return computer_pile_choice

# Remove matches
def remove_pile_matches(arr_piles, pile_number, matches_number):
    arr_piles[pile_number] -= matches_number
    return arr_piles

# Choose game mode
def choose_pile_game_mode():
    """
    usage : choose if the user plays against the computer or against another user

    :return:
    """
    try:
        choice = int(input("Please enter which type of game you want to play : \n1 - Against the computer \n2 - Against another player\n"))
    except ValueError:
        choice = 0

    return choice

display_piles(piles_grid)

players_piles_list[0] = name_player(players_piles_list[0])

players_piles_list[1] = name_player(players_piles_list[1])

while nb_matches_left > 0:
    for i in (0, 1):
        display_piles(piles_grid)
        print(f"{players_piles_list[i]["name"]}'s turn")
        print(f"Number of matches left : {nb_matches_left}")
        pile_nb = player_choose_pile(piles_grid)
        nb_pile_remove = player_choose_matches(players_piles_list[i], piles_grid[pile_nb])
        piles_grid = remove_pile_matches(piles_grid, pile_nb, nb_pile_remove)
        nb_matches_left -= nb_pile_remove
        if nb_matches_left == 0:
            players_piles_list[i]["score"] = "Perdu !"

print("Terminé !")
print("Scores :")
for i in range(2):
    print(f"{players_piles_list[i]["name"]} : {players_piles_list[i]["score"]}")
