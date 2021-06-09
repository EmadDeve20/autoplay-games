#!/bin/env python3

import pygame, random

class Room:
    def __init__(self, width: int=500, height: int=500, speed=60, ):
        """
        init room
        """
        pygame.init()
        #the first step creating a form
        self.width = width
        self.height = height
        self.form = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ball")
        #second, we need logic and a playground(play space)
        self.speed = speed
        self.clock = pygame.time.Clock()
        self.background = (250, 250, 250)
        # We need a random coordinate to make the ball in the first run
        self.x_location = random.randrange(50, 200)
        self.y_location = random.randrange(50, 200)
        # first, run the ball moving up or down? this is random (up or down)
        self.y_changer = self.__up_or_down()
        # first run , ball moving left or right? this is random (left or right)
        self.x_changer = self.__left_or_right()
        # This ball can be faster or slower.
        # But this is a coincidence and remains the same until the end.
        # That is, it either gets faster or slower!
        self.speed_changer = self.__faster_or_slower()
        self.width_ball = 0
        self.width_ball_changer = 1

    def ball(self, color, x_location=100, y_location=100, width=0):
        """this function can created a ball"""
        bull = pygame.draw.circle(self.form, color, (x_location, y_location), 50, width)
        self.form.blit(self.form, bull)

    def __up_or_down(self):
        """return up(-1) or down(1)"""
        if random.randrange(2) == 1:
            return 1
        return -1

    def __left_or_right(self):
        """return left(-1) or right(1)"""
        if random.randrange(2) == 1:
            return 1
        return -1

    def __faster_or_slower(self):
        """return faster(1) or lower(-1)"""
        if random.randrange(2) == 1:
            return 1
        return -1

    def run(self):
        """RUN!"""
        color = (random.randrange(256), random.randrange(256), random.randrange(256))
        exit = False

        # This is the logic of the game
        while not exit:
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    exit = True
                if eve.type == pygame.KEYDOWN:
                    if eve.key == pygame.K_ESCAPE or eve.key == pygame.K_q:
                        exit = True

            # Changes take shape here
            self.form.fill(self.background)
            self.ball(color, self.x_location, self.y_location, self.width_ball)
            self.y_location += self.y_changer
            self.x_location += self.x_changer
            self.width_ball += self.width_ball_changer

            if self.width_ball == 50:
                self.width_ball_changer = -1
            if self.width_ball == 0:
                self.width_ball_changer = 1

            # i Got this numbers with Test!
            # Now the ball has hit the top wall
            if self.y_location-55 < 0 and self.y_changer == -1:
                # the ball need moving down
                self.y_changer = 1
                # If the ball hits the wall, its speed changes
                # If the speed of the ball is fast, it will be faster
                # If the ball is slow, it will be slower
                if (self.speed_changer == 1 and self.speed < 1000) or \
                    (self.speed_changer == -1 and self.speed > 2):
                    self.speed += self.speed_changer
                # If the ball hits the wall, its color can change
                color = (random.randrange(256), random.randrange(256), random.randrange(256))

            # Now the ball has hit the down wall
            if self.y_location+55 > self.height - 200 and self.y_changer == 1:
                # the ball need moving up
                self.y_changer = -1
                # If the ball hits the wall, its speed changes
                # If the speed of the ball is fast, it will be faster
                # If the ball is slow, it will be slower
                if (self.speed_changer == 1 and self.speed < 1000) or \
                    (self.speed_changer == -1 and self.speed > 2):
                    self.speed += self.speed_changer
                # If the ball hits the wall, its color can change
                color = (random.randrange(256), random.randrange(256), random.randrange(256))

            # Now the ball has hit the right wall
            if self.x_location+55 > self.width - 200 and self.x_changer == 1:
                # ball need moving left
                self.x_changer = -1
                # If the ball hits the wall, its speed changes
                # If the speed of the ball is fast, it will be faster
                # If the ball is slow, it will be slower
                if (self.speed_changer == 1 and self.speed < 1000) or \
                (self.speed_changer == -1 and self.speed > 2):
                    self.speed += self.speed_changer
                # If the ball hits the wall, its color can change
                color = (random.randrange(256), random.randrange(256), random.randrange(256))

            # Now the ball has hit the left wall
            if self.x_location - 55 < 0 and self.x_changer == -1:
                self.x_changer = 1
                # If the ball hits the wall, its speed changes
                # If the speed of the ball is fast, it will be faster
                # If the ball is slow, it will be slower
                if (self.speed_changer == 1 and self.speed < 1000) or \
                (self.speed_changer == -1 and self.speed > 2):
                    self.speed += self.speed_changer
                # If the ball hits the wall, its color can change
                color = (random.randrange(256), random.randrange(256), random.randrange(256))

            # This is the passage of time
            self.clock.tick(self.speed)
            # updating screen
            pygame.display.update()

if __name__ == "__main__":
    ROOM = Room()
    ROOM.run()
