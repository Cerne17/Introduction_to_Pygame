'''This lesson teaches to write text on the screen'''

import pygame
from pygame.locals import *
from sys import exit
from random import randint

BLACK  = (0, 0, 0)
WHITE  =  (255, 255, 255)
RED    =  (255, 0, 0)
GREEN  =  (0, 255, 0)
BLUE   =  (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

screen_width  = 640
screen_height = 480
screen        = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game')
clock         = pygame.time.Clock()

rect_width    = 40
rect_height   = 50
x             = screen_width/2-rect_width/2
y             = screen_height/2-rect_height/2
rect_velocity = 10

blue_rect_x = randint(rect_width, screen_width-rect_width)
blue_rect_y = randint(rect_height, screen_height-rect_height)

#Setting the text: params -> (font_family, font_size, is_the_font_bold?, is_the_font_italic?)
font = pygame.font.SysFont("arial", 40, True, False)

#Setting the points logic
points = 0

while True:

    clock.tick(30)
    screen.fill(BLACK)

    #Creating the text 
    message = f'Points: {points}'
    #Params -> (message, Anti_alysing, (RGB))
    formated_text = font.render(message, True, WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_a]:
        x -= rect_velocity
    if pygame.key.get_pressed()[K_d]:
        x += rect_velocity
    if pygame.key.get_pressed()[K_w]:
        y -= rect_velocity
    if pygame.key.get_pressed()[K_s]:
        y += rect_velocity

    red_rect = pygame.draw.rect(screen, RED, (x, y, rect_width, rect_height))
    blue_rect = pygame.draw.rect(screen, BLUE, (blue_rect_x, blue_rect_y, rect_width, rect_height))

    if red_rect.colliderect(blue_rect):
        blue_rect_x = randint(rect_width, screen_width-rect_width)
        blue_rect_y = randint(rect_height, screen_height-rect_height)
        
        #Increase the point counter by 1
        points += 1
    
    #Showing the text: params (message, position_that_the_message_starts)
    screen.blit(formated_text, (450, 40))

    pygame.display.update()

'''
In order to check which fonts you got installed in your computer, enter the following codeline:
pygame.font.get_fonts()
'''