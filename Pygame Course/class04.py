'''This lesson teaches how to control the objects'''

import pygame
from pygame.locals import *
from sys import exit

BLACK  = (0, 0, 0)
WHITE  =  (255, 255, 255)
RED    =  (255, 0, 0)
GREEN  =  (0, 255, 0)
BLUE   =  (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

screen_width  = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

rect_width  = 40
rect_height = 50
x           = screen_width/2-rect_width/2
y           = screen_height/2-rect_height/2

#Setting the rectangle velocity
rect_velocity = 10

while True:

    clock.tick(30)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        #Movement Events (Dectects the press of a button); the code for any button covered by pygame can be found in the following link: http://www.pygame.org/docs/ref/key.html
        '''
        #This code is functional, but the rectangle can only move once per key press, in other words, the user cannot continue pressing the key to get a continuous movement#
        if event.type == KEYDOWN:
            #Left move
            if event.key == K_a:
                x -= rect_velocity
            #Right move
            if event.key == K_d:
                x += rect_velocity
            #Up move
            if event.key == K_w:
                y -= rect_velocity
            #Down move
            if event.key == K_s:
                y += rect_velocity
        '''
    #The following code presents a solution to get a continuous movement by the continuous press of a button
    #Left move
    if pygame.key.get_pressed()[K_a]:
        x -= rect_velocity
    #Right move
    if pygame.key.get_pressed()[K_d]:
        x += rect_velocity
    #Up move
    if pygame.key.get_pressed()[K_w]:
        y -= rect_velocity
    #Down move
    if pygame.key.get_pressed()[K_s]:
        y += rect_velocity


    pygame.draw.rect(screen, RED, (x, y, rect_width, rect_height))

    pygame.display.update()