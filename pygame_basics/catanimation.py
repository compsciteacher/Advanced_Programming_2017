import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('car2.png')
catx = 10
caty = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 7

        if catx == 276:
            direction = 'down'
            catImg = pygame.transform.rotate(catImg, 90)
    elif direction == 'down':
        caty += 7
        if caty == 220:

            direction = 'left'
            catImg=pygame.transform.flip(catImg, True, False)
            catImg = pygame.transform.rotate(catImg,90)
    elif direction == 'left':
        catx -= 7
        if catx == 10:
            direction = 'up'
            catImg = pygame.transform.rotate(catImg, 270)
    elif direction == 'up':
        caty -= 7
        if caty == 10:
            print(caty)
            direction = 'right'
            catImg = pygame.transform.flip(catImg, True, False)
            catImg = pygame.transform.rotate(catImg, 90)

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)