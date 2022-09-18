'''This lesson teaches how to draw simple shapes on the display'''

import pygame
from pygame.locals import *
from sys import exit

#Setting the colors (Standart is to name color variables in upper case)
WHITE =  (255, 255, 255)
RED   =  (255, 0, 0)
GREEN =  (0, 255, 0)
BLUE  =  (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

screen_width  = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game')

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #Drawing a rectangle -> params (where the rect is to be displayed, (R, G, B), (x_position, y_position, rectangle_width, rectangle_height))
        #In pygame, the coordinates begin on the object's top left
    pygame.draw.rect(screen, RED, (200, 300, 40, 50))

    #Drawing a circle -> params (where the circle is to be displayed, (R, G, B), (x_position, y_position), radius)
        #The x and y refered in the circle's parameters are positioned in its center
    pygame.draw.circle(screen, BLUE, (300, 260), 40)

    #Drawing a line -> params (where the line is to be displayed, (R, G, B), (initial_x_position, initial_y_position), (final_x_position, final_y_position), thickness)
    pygame.draw.line(screen, YELLOW, (390, 0), (390, 600), 5)
    
    pygame.display.update()