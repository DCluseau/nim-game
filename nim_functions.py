#!/usr/bin/env python
# -*- coding: utf-8 -*-

MATCH_MIN = 1
MATCH_MAX = 4
NUMBER_OF_MATCHES = 21

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