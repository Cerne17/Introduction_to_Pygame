'''This lesson teaches to add sound effects to the game
Free sound FX at: https://themushroomkingdom.net/media/smw/wav
Free musics at: https://freemusicarchive.org/music/BoxCat_Games
'''

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

#Creating the theme song
pygame.mixer.music.set_volume(0.05)
#The codeline above changes the volume of the song
theme_song = pygame.mixer.music.load('theme_song.mp3')
#Play the music: param -1 makes the music restart
pygame.mixer.music.play(-1)

#Creating the collision SFX -> The SFX MUST be .wav in order not to get an error
collision_sound = pygame.mixer.Sound('smw_coin.wav')
collision_sound.set_volume(1.0)

screen_width  = 640
screen_height = 480
screen        = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game')
clock         = pygame.time.Clock()

rect_width    = 40
rect_height   = 50
x             = int(screen_width/2-rect_width/2)
y             = int(screen_height/2-rect_height/2)
rect_velocity = 20

blue_rect_x = randint(rect_width, screen_width-rect_width)
blue_rect_y = randint(rect_height, screen_height-rect_height)

font = pygame.font.SysFont("arial", 40, True, False)
points = 0

while True:

    clock.tick(30)
    screen.fill(BLACK)

    message = f'Points: {points}'
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
        points += 1
        #Playing the SFX
        collision_sound.play()

    screen.blit(formated_text, (450, 40))

    pygame.display.update()