#!/bin/env python3

"""
this is not completed!
i need time for creating better this code or you are can help me with creating better code.
we have a fun life :D
"""

import sys , random , time , dema
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
        # matrix need double this function for first run
        self.random_number()
        self.random_number()

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
           self.random_number()
           self.draw()


    def score(self):
        """This is function can calculate the score"""
        result = 0
        for i in range(4):
            for j in range(4):
                if self.numbers[i][j] != 2:
                    result += self.numbers[i][j]

        return result


    def playing_game(self):
        """i can be playing 2048 game :D"""
        #player: i need time to think :D
        #time.sleep(1)
        #Player: h3h this is Esay :^)
        dema.playing(self.numbers)

    def random_number(self):
            """this functio can be crated number in the matrix fo game""" 
            while True:
                x = random.randint(0,3)
                y = random.randint(0,3)
                if self.numbers[x][y] == 0:
                    self.numbers[x][y] = 2
                    break


if __name__ == '__main__' :
    player = player()
    player.game_manager()