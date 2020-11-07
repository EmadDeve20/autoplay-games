#!/bin/env python3

import pygame , random

pygame.init()

#first step created form
frame_x = 500
frame_y = 500
frame = pygame.display.set_mode((frame_x,frame_y))
pygame.display.set_caption("Ball")

#secound we need logic and play ground(play space)
speed = 60
clock = pygame.time.Clock()
background = (250,250,250)

def Close():
    pygame.quit()
    quit()

def Bull(color,x = 100 , y = 100 , w = 0):
    """this function can created a ball"""
    bull =  pygame.draw.circle(frame , color , (x , y) , 50 ,w)
    frame.blit(frame , bull)

# we need random x and y for ball in the play ground
x = random.randrange(50,200)
y = random.randrange(50,200)

# first run , ball moving up or down? this is random (up or down)
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

# this is ball can be faster or lower. but this is a random
i = random.randrange(2)
if i == 0:
    speed_change = -1
else:
    speed_change = 1

w = 0 ; w_change = 1
color = (random.randrange(256) , random.randrange(256) , random.randrange(256))
exiting = False

# this is logic ball (Game)
while not exiting:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            Close()
        if eve.type == pygame.KEYDOWN:
            if eve.key == pygame.K_ESCAPE or eve.key == pygame.K_q:
                Close()

    # events
    frame.fill(background)
    Bull(color , x , y , w)
    y +=y_change
    x +=x_change
    w += w_change

    #print(w)
    if w == 50:
        w_change = -1
    if w == 0:
        w_change = 1

    # now ball is crashed on the up wall
    if y-55 < 0 and y_change == -1:
        # ball need moveing down
        y_change = 1
        # ball can bie changed speed if crashed on the wall 
        # if speed is fast , speed can bie faster
        # if speed is slow , speed can bie slower
        if (speed_change == 1 and speed < 1000) or (speed_change == -1 and speed > 2):
            speed += speed_change
        # color can be changed if ball crashed on the wall
        color = (random.randrange(256) , random.randrange(256) , random.randrange(256))
    
    # now ball is crashed on the down wall
    if y+55 > frame_y - 200 and y_change == 1:
        # ball need moving up
        y_change = -1
        # ball can bie changed speed if crashed on the wall 
        # if speed is fast , speed can bie faster
        # if speed is slow , speed can bie slower
        if (speed_change == 1 and speed < 1000) or (speed_change == -1 and speed > 2):
            speed += speed_change
        # color can bie changed if ball crashed on the wall
        color = (random.randrange(256) , random.randrange(256) , random.randrange(256))
    
    # now ball is crashed on the right wall
    if x+55 > frame_x - 200 and x_change == 1:
        # ball need moving left
        x_change = -1
        # ball can bie changed speed if crashed on the wall 
        # if speed is fast , speed can bie faster
        # if speed is slow , speed can bie slower
        if (speed_change == 1 and speed < 1000) or (speed_change == -1 and speed > 2):
            speed += speed_change
        # color can bie changed if ball crashed on the wall
        color = (random.randrange(256) , random.randrange(256) , random.randrange(256))

    # now ball is crashed on the left wall
    if x - 55 < 0 and x_change == -1:
        x_change = 1
        # ball can bie changed speed if crashed on the wall 
        # if speed is fast , speed can bie faster
        # if speed is slow , speed can bie slower
        if (speed_change == 1 and speed < 1000) or (speed_change == -1 and speed > 2):
            speed += speed_change
        # color can bie changed if ball crashed on the wall
        color = (random.randrange(256) , random.randrange(256) , random.randrange(256))

    # this is time of world game
    clock.tick(speed)
    # updating screen
    pygame.display.update()
