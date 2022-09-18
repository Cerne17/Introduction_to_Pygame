'''This lesson teaches how to make objects move.'''
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

#Controling the frame_rate
clock = pygame.time.Clock()

#Initial Rectangle informations
rect_width  = 40
rect_height = 50
x           = screen_width/2-rect_width/2
y           = 0

while True:

    #Setting the framerate
    clock.tick(30)

    #Fills the background color, so that the objects don't stay in the screen after each iteration
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(screen, RED, (x, y, rect_width, rect_height))


    #Checks for the rectangle's y coordinate, so that it returns to the top of the screen
    if y>= screen_height:
        y=0

    #Y movement
    y += 5

    pygame.display.update()