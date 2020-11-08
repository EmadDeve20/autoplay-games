#!/bin/env python3

"""
this is not completed!
i need time for creating better this code or you are can help me with creating better code.
we have a fun life :D
"""

import sys , random , time
import push_numbers as p

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
        # this is while can created play_ground in the run code in the first run
        while i < 2:
            x = random.randint(0,3)
            y = random.randint(0,3)
            if self.numbers[x][y] == 0:
                self.numbers[x][y] = 2
                i += 1

        self.draw()
    def draw(self):
        """draw play-ground"""
        #first, i need a clear screen for the playground
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
        while p.matrix_is_alive(self.numbers):
           self.playing_game()


    def score(self , move=None):
        """This is function can calculate the score"""
        result = 0
        num = [[],[],[],[]]
        self.copy_numbers(self.numbers , num)
        
        if move == 'left':
            p.pushing_left(num)
        
        if move == 'right':
            p.pushing_right(num)

        if move == 'up':
            p.pushing_up(num)

        if move == 'down':
            p.pushing_down(num)


        for i in range(4):
            for j in range(4):
                if num[i][j] != 2:
                    result += num[i][j]

        return result


    def playing_game(self):
        """i can be playing 2048 game :D"""
        score_left = self.score('left')
        score_right = self.score("right")
        score_up = self.score("up")
        score_down = self.score("down")

        max_score = max(score_left , score_right , score_up , score_down)

        #player: i need time to think :D
        time.sleep(1)

        if max_score == score_right and p.can_pushing_right(self.numbers):
            self.right_move()
            return 1
        if max_score == score_up and p.can_pushing_up(self.numbers):
            self.up_move()
            return 1
        if max_score == score_left and p.can_pushing_left(self.numbers):
            self.left_move()
            return 1
        if max_score == score_down and p.can_pushing_down(self.numbers):
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
        """this function can be moving numbers to left just like the 2048 game"""
        p.pushing_left(self.numbers)
        self.random_number()
        self.draw()

    def right_move(self):
        """this function can be moving numbers to right just like the 2048 game"""
        p.pushing_right(self.numbers)
        self.random_number()
        self.draw()

    def up_move(self):
        """this function can be moving up numbers just like the 2048 game"""
        p.pushing_up(self.numbers)
        self.random_number()
        self.draw()

    def down_move(self):
        """this function can be moving down numbers just like the 2048 game"""
        p.pushing_down(self.numbers)
        self.random_number()
        self.draw()

    def copy_numbers(self , numbers , cp_numbers):
        """this function can copy numbers list in the other list"""
        for i in range(len(numbers)):
            cp_numbers[i] = numbers[i].copy()

if __name__ == '__main__' :
    player = player()
    player.game_manager()
