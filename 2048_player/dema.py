#!/bin/env python3

"""
this is class in the fact, champion for playing 2048 game
"""

import push_numbers as p

def copy_numbers(mat , cp_mat):
    """this function can copy numbers list in the other list"""
    for i in range(len(mat)):
        cp_mat[i] = mat[i].copy()

def look_matrix(mat , focuse):
    """this function can see matrix and think about the best move"""

    result = 0
    cp_mat = [[],[],[],[]]
    copy_numbers(mat , cp_mat)

    #Player: i look in matrix and calculating for the beeter choice
    if focuse == 'lef' and p.can_pushing_left(mat):
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

def playing(mat):
    """Player: Hi, i am player and i can play this esay Game!"""

    #i need looking matrix and all choices
    cl = look_matrix(mat,'left') #pushing to left(choice left)
    cr = look_matrix(mat,'right') #pushing to right(choice right)
    cu = look_matrix(mat,'up') #pushing to up(choice up)
    cd = look_matrix(mat,'down') #pushing to down(choice down)
    best_choice = max(cl , cr , cu , cd)

    if best_choice == cr and p.can_pushing_right(mat):
        p.pushing_right(mat)
        return 1
    if best_choice == cu and p.can_pushing_up(mat):
        p.pushing_up(mat)
        return 1
    if best_choice == cd and p.can_pushing_down(mat):
        p.pushing_down(mat)
        return 1
    if best_choice == cl and p.can_pushing_left(mat):
        p.pushing_left(mat)
        return 1
