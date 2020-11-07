#!/bin/env python3
""" 
this is hard code and not complated!
i need time for creating beter this code or you are can help me for creating beter code.
we have fun life :D
"""

import sys , random , time

class player:
    """this is class can solve 2048 game"""
    def __init__(self):
        """crated numbers for player"""
        random.seed()
        #we need this is numbers for showing and playing
        self.numbers = [[0,0,0,0],
                        [0,0,0,0],
                        [0,0,0,0],
                        [0,0,0,0]]

        self.nativ_numbers = [[],[],[],[]]
        i = 0
        # this is while can created play_ground in the run code
        while i < 2:
            x = random.randint(0,3)
            y = random.randint(0,3)
            if self.numbers[x][y] == 0:
                self.numbers[x][y] = 2
                i += 1

        self.draw()
    def draw(self):
        """draw play-ground"""
        #first i need clear screen for play ground
        #print("\033[0H")
        space = '    '
        for i in range(4):
            for j in range(4):
                if self.numbers[i][j] == 0:
                    sys.stdout.write(space + ".")
                else:
                    sys.stdout.write(space +str(self.numbers[i][j]))
            sys.stdout.write("\n")
        print(f"Score: {self.score()}")

    def game_manager(self):
        """this function for managing game"""
        while self.player_is_not_loser(self.numbers):
            self.playing_game()
            

    def score(self , move=None):
        """This is function can calculated score"""
        result = 0
        num = [[],[],[],[]]
        self.copy_numbers(self.numbers , num)
        if move == 'left':
            have_zero = False
            for i in range(4):
                for j in range(4):
                    if num[i][j] == 0:
                        have_zero = True
                    if have_zero:
                        for i in range(4):
                            left = False
                            while not left:
                                for j in range(4):
                                    n = 0
                                    if num[i][j] != 0 and num[i][j-1] == 0 and j != 0:
                                        num[i][j-1] = num[i][j]
                                        num[i][j] = 0

                                if num[i][j] == 0:
                                    n += 1

                                if n == 0:
                                    left = True
                                if n == 1 and num[i][3] == 0:
                                        left = True
                                if n == 2 and num[i][2] == 0 and num[3] == 0:
                                    left = True
                                if n == 3 and num[i][0] != 0:
                                    left = True
            
            for i in range(4):
                for j in range(3):
                    if num[i][j] == num[i][j+1]:
                        num[i][j] *= 2
                        num[i][j+1] = 0
                    
        if move == 'right':
            have_zero = False
            for i in range(3,-1,-1):
                for j in range(3,-1,-1):
                    if num[i][j] == 0:
                        have_zero = True
                    if have_zero:
                        for i in range(3,-1,-1):
                            right = False
                            while not right:
                                for j in range(3,-1,-1):
                                    n = 0
                                    if num[i][j] == 0 and num[i][j-1] != 0 and j != 0:
                                        num[i][j] = num[i][j-1]
                                        num[i][j-1] = 0

                                    if num[i][j] == 0:
                                        n += 1

                                if n == 0:
                                    right = True
                                if n == 1 and num[i][0] == 0:
                                        right = True
                                if n == 2 and num[i][1] == 0 and num[3] == 0:
                                    right = True
                                if n == 3 and num[i][3] != 0:
                                    right = True
            
            for i in range(3,-1,-1):
                for j in range(3,-1,-1):
                    if num[i][j] == num[i][j-1]:
                        num[i][j] *= 2
                        num[i][j-1] = 0
                    
        if move == 'up':
            have_zero = False
            for i in range(4):
                for j in range(4):
                    if num[j][i] == 0:
                        have_zero = True
                    if have_zero:
                        for i in range(4):
                            up = False
                            while not up:
                                for j in range(3):
                                    n = 0
                                    if num[j][i] == 0 and num[j+1][i] != 0:
                                        num[j][i] = num[j+1][i]
                                        num[j+1][i] = 0

                                    if num[j][i] == 0:
                                        n += 1

                                if n == 0:
                                    up = True
                                if n == 1 and num[3][i] == 0:
                                        up = True
                                if n == 2 and num[2][i] == 0 and num[3] == 0:
                                    up = True
                                if n == 3 and num[0][i] != 0:
                                    up = True
            
            for i in range(4):
                for j in range(3):
                    if num[j][i] == num[j+1][i]:
                        num[j][i] *= 2
                        num[j+1][i] = 0
                    
        if move == 'down':
            have_zero = False
            for i in range(3,-1,-1):
                for j in range(3,-1,-1):
                    if num[j][i] == 0:
                        have_zero = True
                    if have_zero:
                        for i in range(3,-1,-1):
                            down = False
                            while not down:
                                for j in range(3,-1,-1):
                                    n = 0
                                    if num[j][i] == 0 and num[j-1][i] != 0 and j != 0:
                                        num[j][i] = num[j-1][i]
                                        num[j-1][i] = 0

                                    if num[j][i] == 0:
                                        n += 1

                                if n == 0:
                                    down = True
                                if n == 1 and num[0][i] == 0:
                                        down = True
                                if n == 2 and num[1][i] == 0 and num[3] == 0:
                                    down = True
                                if n == 3 and num[2][i] != 0:
                                    down = True
            
            for i in range(3,-1,-1):
                for j in range(3,-1,-1):
                    if num[j][i] == num[j-1][i]:
                        num[j-1][i] *= 2
                        num[j][i] = 0
                    
        
        for i in range(4):
            for j in range(4):
                if num[i][j] != 2:
                    result += num[i][j]

        return result


    def playing_game(self):
        """i can playing 2048 game :D"""
        score_left = self.score('left')
        score_right = self.score("right")
        score_up = self.score("up")
        score_down = self.score("down")

        max_score = max(score_left , score_right , score_up , score_down)

        # i need think :D
        time.sleep(1)

        if max_score == score_right:
            self.right_move()
            return 1
        if max_score == score_up:
            self.up_move()
            return 1
        if max_score == score_left:
            self.left_move()
            return 1
        if max_score == score_down:
            self.down_move()
            return 1

    def random_number(self):
        have_zero = False
        for i in range(4):
            for j in range(4):
                if self.numbers[i][j] == 0:
                    have_zero = True
                    break
            if have_zero:
                break
        
        while have_zero:
            x = random.randint(0,3)
            y = random.randint(0,3)
            if self.numbers[x][y] == 0:
                self.numbers[x][y] = 2
                break

    def left_move(self):
        """this function can moving numbers left just like 2048 game"""
        self.copy_numbers(self.numbers , self.nativ_numbers)
        have_zero = False
        for i in range(4):
            for j in range(4):
                if self.numbers[i][j] == 0:
                    have_zero = True
                if have_zero:
                    for i in range(4):
                        left = False
                        while not left:
                            for j in range(4):
                                n = 0
                                if self.numbers[i][j] != 0 and self.numbers[i][j-1] == 0 and j != 0:
                                    self.numbers[i][j-1] = self.numbers[i][j]
                                    self.numbers[i][j] = 0

                            if self.numbers[i][j] == 0:
                                n += 1

                            if n == 0:
                                left = True
                            if n == 1 and self.numbers[i][3] == 0:
                                    left = True
                            if n == 2 and self.numbers[i][2] == 0 and self.numbers[3] == 0:
                                left = True
                            if n == 3 and self.numbers[i][0] != 0:
                                left = True
        
        for i in range(4):
            for j in range(3):
                if self.numbers[i][j] == self.numbers[i][j+1]:
                    self.numbers[i][j] *= 2
                    self.numbers[i][j+1] = 0
        
        have_zero = False
        for i in range(4):
            for j in range(4):
                if self.numbers[i][j] == 0:
                    have_zero = True
                if have_zero:
                    for i in range(4):
                        left = False
                        while not left:
                            for j in range(4):
                                n = 0
                                if self.numbers[i][j] != 0 and self.numbers[i][j-1] == 0 and j != 0:
                                    self.numbers[i][j-1] = self.numbers[i][j]
                                    self.numbers[i][j] = 0

                                if self.numbers[i][j] == 0:
                                    n += 1

                            if n == 0:
                                left = True
                            if n == 1 and self.numbers[i][3] == 0:
                                    left = True
                            if n == 2 and self.numbers[i][2] == 0 and self.numbers[3] == 0:
                                left = True
                            if n == 3 and self.numbers[i][0] != 0:
                                left = True
        self.random_number()
        self.draw()

    def right_move(self):
        """this function can moving right just like 2048 game"""
        self.copy_numbers(self.numbers , self.nativ_numbers)
        have_zero = False
        for i in range(3,-1,-1):
            for j in range(3,-1,-1):
                if self.numbers[i][j] == 0:
                    have_zero = True
                if have_zero:
                    for i in range(3,-1,-1):
                        right = False
                        while not right:
                            for j in range(3,-1,-1):
                                n = 0
                                if self.numbers[i][j] == 0 and self.numbers[i][j-1] != 0 and j != 0:
                                    self.numbers[i][j] = self.numbers[i][j-1]
                                    self.numbers[i][j-1] = 0

                                if self.numbers[i][j] == 0:
                                    n += 1

                            if n == 0:
                                right = True
                            if n == 1 and self.numbers[i][0] == 0:
                                    right = True
                            if n == 2 and self.numbers[i][1] == 0 and self.numbers[3] == 0:
                                right = True
                            if n == 3 and self.numbers[i][3] != 0:
                                right = True
        
        for i in range(3,-1,-1):
            for j in range(3,-1,-1):
                if self.numbers[i][j] == self.numbers[i][j-1]:
                    self.numbers[i][j] *= 2
                    self.numbers[i][j-1] = 0
                
        have_zero = False
        for i in range(3,-1,-1):
            for j in range(3,-1,-1):
                if self.numbers[i][j] == 0:
                    have_zero = True
                if have_zero:
                    for i in range(3,-1,-1):
                        right = False
                        while not right:
                            for j in range(3,-1,-1):
                                n = 0
                                if self.numbers[i][j] == 0 and self.numbers[i][j-1] != 0 and j != 0:
                                    self.numbers[i][j] = self.numbers[i][j-1]
                                    self.numbers[i][j-1] = 0

                                if self.numbers[i][j] == 0:
                                    n += 1

                            if n == 0:
                                right = True
                            if n == 1 and self.numbers[i][0] == 0:
                                    right = True
                            if n == 2 and self.numbers[i][1] == 0 and self.numbers[3] == 0:
                                right = True
                            if n == 3 and self.numbers[i][3] != 0:
                                right = True
        self.random_number()
        self.draw()

    def up_move(self):
        """this function can moving up numbers just like 2048 game"""
        self.copy_numbers(self.numbers , self.nativ_numbers)
        have_zero = False
        for i in range(4):
            for j in range(4):
                if self.numbers[j][i] == 0:
                    have_zero = True
                if have_zero:
                    for i in range(4):
                        up = False
                        while not up:
                            for j in range(3):
                                n = 0
                                if self.numbers[j][i] == 0 and self.numbers[j+1][i] != 0:
                                    self.numbers[j][i] = self.numbers[j+1][i]
                                    self.numbers[j+1][i] = 0

                                if self.numbers[j][i] == 0:
                                    n += 1

                            if n == 0:
                                up = True
                            if n == 1 and self.numbers[3][i] == 0:
                                    up = True
                            if n == 2 and self.numbers[2][i] == 0 and self.numbers[3] == 0:
                                up = True
                            if n == 3 and self.numbers[0][i] != 0:
                                up = True
        
        for i in range(4):
            for j in range(3):
                if self.numbers[j][i] == self.numbers[j+1][i]:
                    self.numbers[j][i] *= 2
                    self.numbers[j+1][i] = 0
                
        have_zero = False
        for i in range(4):
            for j in range(4):
                if self.numbers[j][i] == 0:
                    have_zero = True
                if have_zero:
                    for i in range(4):
                        up = False
                        while not up:
                            for j in range(3):
                                n = 0
                                if self.numbers[j][i] == 0 and self.numbers[j+1][i] != 0:
                                    self.numbers[j][i] = self.numbers[j+1][i]
                                    self.numbers[j+1][i] = 0

                                if self.numbers[j][i] == 0:
                                    n += 1

                            if n == 0:
                                up = True
                            if n == 1 and self.numbers[3][i] == 0:
                                    up = True
                            if n == 2 and self.numbers[2][i] == 0 and self.numbers[3] == 0:
                                up = True
                            if n == 3 and self.numbers[0][i] != 0:
                                up = True
        self.random_number()
        self.draw()

    def down_move(self):
        """this function can moving bot numbers just like 2048 game"""
        self.copy_numbers(self.numbers , self.nativ_numbers)
        have_zero = False
        for i in range(3,-1,-1):
            for j in range(3,-1,-1):
                if self.numbers[j][i] == 0:
                    have_zero = True
                if have_zero:
                    for i in range(3,-1,-1):
                        down = False
                        while not down:
                            for j in range(3,-1,-1):
                                n = 0
                                if self.numbers[j][i] == 0 and self.numbers[j-1][i] != 0 and j != 0:
                                    self.numbers[j][i] = self.numbers[j-1][i]
                                    self.numbers[j-1][i] = 0

                                if self.numbers[j][i] == 0:
                                    n += 1

                            if n == 0:
                                down = True
                            if n == 1 and self.numbers[0][i] == 0:
                                    down = True
                            if n == 2 and self.numbers[1][i] == 0 and self.numbers[3] == 0:
                                down = True
                            if n == 3 and self.numbers[2][i] != 0:
                                down = True
        
        for i in range(3,-1,-1):
            for j in range(3,-1,-1):
                if self.numbers[j][i] == self.numbers[j-1][i]:
                    self.numbers[j-1][i] *= 2
                    self.numbers[j][i] = 0
                
        have_zero = False
        for i in range(3,-1,-1):
            for j in range(3,-1,-1):
                if self.numbers[j][i] == 0:
                    have_zero = True
                if have_zero:
                    for i in range(3,-1,-1):
                        down = False
                        while not down:
                            for j in range(3,-1,-1):
                                n = 0
                                if self.numbers[j][i] == 0 and self.numbers[j-1][i] != 0 and j != 0:
                                    self.numbers[j][i] = self.numbers[j-1][i]
                                    self.numbers[j-1][i] = 0

                                if self.numbers[j][i] == 0:
                                    n += 1

                            if n == 0:
                                down = True
                            if n == 1 and self.numbers[0][i] == 0:
                                    down = True
                            if n == 2 and self.numbers[1][i] == 0 and self.numbers[3] == 0:
                                down = True
                            if n == 3 and self.numbers[2][i] != 0:
                                down = True
        self.random_number()
        self.draw()

    def player_is_not_loser(self,mat):
        """
           this is fucntion can spach we loser or not.
           i using (github.com > 2048-python > logic.py > def game_state) code for this function.
           this is power of opne source.
        """
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 2048:
                    return True
        for i in range(len(mat)-1):
            # intentionally reduced to check the row on the right and below
            # more elegant to use exceptions but most likely this will be their solution
            for j in range(len(mat[0])-1):
                if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                    return True
        for i in range(len(mat)):  # check for any zero entries
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    return True
        for k in range(len(mat)-1):  # to check the left/right entries on the last row
            if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
                return True
        for j in range(len(mat)-1):  # check up/down entries on last column
            if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
                return True
        return False
    
    def copy_numbers(self , numbers , cp_numbers):
        """This function can bie copy numbers list in the other list"""
        for i in range(len(numbers)):
            cp_numbers[i] = numbers[i].copy()

if __name__ == '__main__' :
    player = player()
    player.game_manager()