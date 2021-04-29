#!/bin/env python3

import pygame , random

class Room:
    def __init__(self):
        """
        init room
        """
        pygame.init()

        #the first step creating a form
        self.width = 500
        self.height = 500
        self.form = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ball")

        #second, we need logic and a playground(play space)
        self.speed = 60
        self.clock = pygame.time.Clock()
        self.background = (250, 250, 250)

    def close(self):
        """
            from need close for user
        """
        pygame.quit()
        quit()

    def ball(self, color, x = 100 , y = 100 , w = 0):
        """this function can created a ball"""
        bull =  pygame.draw.circle(self.form , color , (x , y) , 50 ,w)
        self.form.blit(self.form , bull)

    def run(self):
        # We need a random coordinate to make the ball in the first run
        x = random.randrange(50,200)
        y = random.randrange(50,200)

        # first, run the ball moving up or down? this is random (up or down)
        i = random.randrange(2)
        if i == 0:
            y_change = -1
        else:
            y_change = 1

        # first run , ball moving left or right? this is random (left or right)
        i = random.randrange(2)
        if i == 0:
            x_change = 1
        else:
            x_change = -1

        # This ball can be faster or slower. 
        # But this is a coincidence and remains the same until the end.
        # That is, it either gets faster or slower!
        i = random.randrange(2)
        if i == 0:
            speed_change = -1
        else:
            speed_change = 1

        w = 0 ; w_change = 1
        color = (random.randrange(256) , random.randrange(256) , random.randrange(256))
        exiting = False

        # This is the logic of the game
        while not exiting:
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    self.close()
                if eve.type == pygame.KEYDOWN:
                    if eve.key == pygame.K_ESCAPE or eve.key == pygame.K_q:
                        self.close()

            # Changes take shape here
            self.form.fill(self.background)
            self.ball(color , x , y , w)
            y +=y_change
            x +=x_change
            w += w_change

            #print(w)
            if w == 50:
                w_change = -1
            if w == 0:
                w_change = 1

            # Now the ball has hit the top wall
            if y-55 < 0 and y_change == -1:
                # the ball need moving down
                y_change = 1
                # If the ball hits the wall, its speed changes
                # If the speed of the ball is fast, it will be faster
                # If the ball is slow, it will be slower
                if (speed_change == 1 and self.speed < 1000) or \
                    (speed_change == -1 and self.speed > 2):
                    self.speed += speed_change
                # If the ball hits the wall, its color can change
                color = (random.randrange(256) , random.randrange(256) , random.randrange(256))
            
            # Now the ball has hit the down wall
            if y+55 > self.height - 200 and y_change == 1:
                # the ball need moving up
                y_change = -1
                # If the ball hits the wall, its speed changes
                # If the speed of the ball is fast, it will be faster
                # If the ball is slow, it will be slower
                if (speed_change == 1 and self.speed < 1000) or \
                    (speed_change == -1 and self.speed > 2):
                    self.speed += speed_change
                # If the ball hits the wall, its color can change
                color = (random.randrange(256) , random.randrange(256) , random.randrange(256))
            
            # Now the ball has hit the right wall
            if x+55 > self.width - 200 and x_change == 1:
                # ball need moving left
                x_change = -1
                # If the ball hits the wall, its speed changes
                # If the speed of the ball is fast, it will be faster
                # If the ball is slow, it will be slower
                if (speed_change == 1 and self.speed < 1000) or (speed_change == -1 and self.speed > 2):
                    self.speed += speed_change
                # If the ball hits the wall, its color can change
                color = (random.randrange(256) , random.randrange(256) , random.randrange(256))

            # Now the ball has hit the left wall
            if x - 55 < 0 and x_change == -1:
                x_change = 1
                # If the ball hits the wall, its speed changes
                # If the speed of the ball is fast, it will be faster
                # If the ball is slow, it will be slower
                if (speed_change == 1 and self.speed < 1000) or (speed_change == -1 and self.speed > 2):
                    self.speed += speed_change
                # If the ball hits the wall, its color can change
                color = (random.randrange(256) , random.randrange(256) , random.randrange(256))

            # This is the passage of time
            self.clock.tick(self.speed)
            # updating screen
            pygame.display.update()

if __name__ == "__main__":
    ROOM = Room()
    ROOM.run()