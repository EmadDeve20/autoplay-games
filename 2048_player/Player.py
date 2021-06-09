#!/bin/env python3

"""
this is class in the fact, champion for playing 2048 game
"""

from typing import List
import push_numbers as p


def look_matrix(mat: List[int] , focuse: str) -> int:
    """this function can see matrix and think about the best move"""

    result = 0
    cp_mat = mat.copy()

    #Player: i look in matrix and calculating for the beeter choice
    if focuse == 'left' and p.can_pushing_left(mat):
        p.pushing_left(cp_mat)
    if focuse == 'right' and p.can_pushing_right(mat):
        p.pushing_right(cp_mat)
    if focuse == 'up' and p.can_pushing_up(mat):
        p.pushing_up(cp_mat)
    if focuse == 'down' and p.can_pushing_down(mat):
        p.pushing_down(cp_mat)

    #we need calculated for all choices
    for i in range(len(cp_mat)):
        for j in range(len(cp_mat)):
            if cp_mat[i][j] != 0 and cp_mat[i][j] != 2:
                result += cp_mat[i][j]

    # Now Player can see and about think for best move!
    return result

def playing(mat: List[int]):
    """Player: Hi, i am player and i can play this esay Game!"""

    #i need looking matrix and all choices
    choice_left = look_matrix(mat,'left') #pushing to left(choice left)
    choice_right = look_matrix(mat,'right') #pushing to right(choice right)
    choice_up = look_matrix(mat,'up') #pushing to up(choice up)
    choice_down = look_matrix(mat,'down') #pushing to down(choice down)
    best_choice = max(choice_left , choice_right , choice_up , choice_down)

    if best_choice == choice_right and p.can_pushing_right(mat):
        p.pushing_right(mat)
        return
    if best_choice == choice_up and p.can_pushing_up(mat):
        p.pushing_up(mat)
        return
    if best_choice == choice_down and p.can_pushing_down(mat):
        p.pushing_down(mat)
        return
    if best_choice == choice_left and p.can_pushing_left(mat):
        p.pushing_left(mat)
        return
