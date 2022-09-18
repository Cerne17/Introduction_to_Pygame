'''This lesson teaches how to properly initialize a window in pygame'''


import pygame
#Import the sub lib locals -> library that contains some interesting consts and functions
from pygame.locals import *
#Import the sys function exit -> function that is able to close our application
from sys import exit
#Initialize the pygame library
pygame.init()

#Create the window and set its properties
screen_width  = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#Changing the window names
pygame.display.set_caption('Game')

#Main game loop
while True:
    #Now the game begins

    #Events loop
    for event in pygame.event.get():
        #Quit event
        if event.type == QUIT:
            pygame.quit()
            exit()
    

    #Display update
    pygame.display.update()