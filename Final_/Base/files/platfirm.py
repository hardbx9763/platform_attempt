import pygame, sys, os
from pygame.locals import *
os.chdir("C:\\Base")
pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platfirm")

#images
sun = pygame.image.load("sun.png")
sky = pygame.image.load("sky.png")

run = True
while run:

    screen.blit(sky, (0,0))
    screen.blit(sun, (100,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update() 

pygame.quit()