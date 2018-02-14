import pygame, sys, random
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Input')


def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True


# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DOWNLEFT = 0
DOWNRIGHT = 1
UPLEFT = 2
UPRIGHT = 3
# set up the player and food data structure
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player1 = pygame.Rect((WINDOWWIDTH / 2) - WINDOWWIDTH * .05, WINDOWHEIGHT - 50, WINDOWWIDTH * .1, 10)
# player2 = pygame.Rect((WINDOWWIDTH/2)-WINDOWWIDTH*.05, 50, WINDOWWIDTH*.1, 10)
balls = []
# ball=pygame.Rect(WINDOWWIDTH*.5, WINDOWHEIGHT*.5, 10, 10)
ball = {'rect': pygame.Rect(player1.x + WINDOWWIDTH * .05, player1.y - 15, 10, 10), 'color': WHITE,
        'dir': random.randrange(4), 'speed': 3}
balls.append(ball)
blocks = []
blocklength = 36
blockheight = 16
for x in range(int(WINDOWWIDTH / blocklength)):
    difference = int(WINDOWWIDTH % blocklength)
    # if (x>=2) & (x<=10):
    for y in range(int(WINDOWHEIGHT / blockheight)):
        if (y >= 2) & (y <= 10):
            # print("{},{}".format(x,y))
            block = pygame.Rect(blocklength * x + (difference / 1.5), blockheight * y, blocklength * (10 / 11),
                                blockheight * 3 / 4)
            # print(block.x)
            blocks.append(block)
# ball={'rect':pygame.Rect(WINDOWWIDTH*.5, WINDOWHEIGHT*.5, 10, 10), 'color':WHITE, 'dir':random.randrange(4)}
fixer = pygame.Rect(50, (WINDOWHEIGHT / 2) - WINDOWHEIGHT * .1, 10, 10)
# set up movement variables
p1moveLeft = False
p1moveRight = False
# p2moveUp = False
# p2moveDown = False

# p1score=0
# p2score=0

MOVESPEED = 6

# run the game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == ord('a'):
                p1moveLeft = True
            if event.key == ord('d'):
                p1moveRight = True
            # if event.key == K_UP:
            #    p2moveUp = True
            # if event.key == K_DOWN:
            #    p2moveDown = True
            # if event.key == ord('x'):
            #    player.top = random.randint(0, WINDOWHEIGHT - player.height)
            #    player.left = random.randint(0, WINDOWWIDTH - player.width)
            if event.key == K_SPACE:
                for x in range(int(WINDOWWIDTH / blocklength)):
                    difference = int(WINDOWWIDTH % blocklength)
                    # if (x>=2) & (x<=10):
                    for y in range(int(WINDOWHEIGHT / 16)):
                        if (y >= 2) & (y <= 10):
                            # print("{},{}".format(x,y))
                            block = pygame.Rect(blocklength * x + (difference / 1.5), blockheight * y,
                                                blocklength * (10 / 11), blockheight * 3 / 4)
                            # print(block.x)
                            blocks.append(block)
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == ord('a'):
                p1moveLeft = False
            if event.key == ord('d'):
                p1moveRight = False
                # if event.key == K_UP:
                #    p2moveUp = False
                # if event.key == K_DOWN:
                #    p2moveDown = False

        if event.type == MOUSEBUTTONUP:
            ball = {'rect': pygame.Rect(player1.x + WINDOWWIDTH * .05, player1.y - 15, 10, 10), 'color': WHITE,
                    'dir': random.randrange(4), 'speed': 3}
            balls.append(ball)

    '''foodCounter += 1
    if foodCounter >= NEWFOOD:
        # add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))'''

    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    # move the players
    if p1moveLeft and player1.left > 0:
        player1.left -= MOVESPEED
    if p1moveRight and player1.right < WINDOWWIDTH:
        player1.right += MOVESPEED
        # if p2moveDown and player2.bottom < WINDOWHEIGHT:
        #    player2.top += MOVESPEED
        # fixer=pygame.Rect(50, player1.y+WINDOWHEIGHT*.1, 10, 10)
        # if p2moveUp and player2.top > 0:
        #    player2.top -= MOVESPEED
        # fixer=pygame.Rect(50, player1.y+WINDOWHEIGHT*.1, 10, 10)

    # draw the player onto the surface
    pygame.draw.rect(windowSurface, WHITE, player1)
    # pygame.draw.rect(windowSurface, WHITE, player2)
    # pygame.draw.rect(windowSurface, GREEN, fixer)

    # draw scores
    # windowSurface.blit(pygame.font.SysFont("Comic Sans MS", int((WINDOWWIDTH+WINDOWHEIGHT)*.05)).render('{}'.format(p1score), True, (255,255,255)), (WINDOWWIDTH*.2,WINDOWHEIGHT*.1))
    # windowSurface.blit(pygame.font.SysFont("Comic Sans MS", int((WINDOWWIDTH+WINDOWHEIGHT)*.05)).render('{}'.format(p2score), True, (255,255,255)), (WINDOWWIDTH-WINDOWWIDTH*.2,WINDOWHEIGHT*.1))



    for b in balls[:]:
        # ball hits blocks
        for b2 in blocks[:]:
            if b2.colliderect(b['rect']):
                blocks.remove(b2)
                if isPointInsideRect(b['rect'].left, b['rect'].top, b2):
                    # block has moved past the top
                    if b['dir'] == UPLEFT:
                        b['dir'] = DOWNLEFT
                    if b['dir'] == UPRIGHT:
                        b['dir'] = DOWNRIGHT
                    b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))
                if isPointInsideRect(b['rect'].left, b['rect'].bottom, b2):
                    # block has moved past the bottom
                    if b['dir'] == DOWNLEFT:
                        b['dir'] = DOWNRIGHT
                    if b['dir'] == DOWNRIGHT:
                        b['dir'] = DOWNLEFT
                    if b['dir'] == UPLEFT:
                        b['dir'] = UPRIGHT
                    if b['dir'] == UPRIGHT:
                        b['dir'] = UPLEFT
                    b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))
                if isPointInsideRect(b['rect'].right, b['rect'].top, b2):
                    # block has moved past the left side
                    if b['dir'] == DOWNLEFT:
                        b['dir'] = DOWNRIGHT
                    if b['dir'] == DOWNRIGHT:
                        b['dir'] = DOWNLEFT
                    if b['dir'] == UPLEFT:
                        b['dir'] = UPRIGHT
                    if b['dir'] == UPRIGHT:
                        b['dir'] = UPLEFT
                    b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))
                if isPointInsideRect(b['rect'].right, b['rect'].bottom, b2):
                    # block has moved past the right side
                    if b['dir'] == UPRIGHT:
                        b['dir'] = DOWNLEFT
                    if b['dir'] == UPRIGHT:
                        b['dir'] = DOWNLEFT
                    b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))
                if b['rect'].top < b2.top:
                    # block has moved past the top
                    if b['dir'] == UPLEFT:
                        b['dir'] = DOWNLEFT
                    if b['dir'] == UPRIGHT:
                        b['dir'] = DOWNRIGHT
                    if b['dir'] == DOWNLEFT:
                        b['dir'] = UPLEFT
                    if b['dir'] == DOWNRIGHT:
                        b['dir'] = UPRIGHT
                    b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))
                if b['rect'].bottom > b2.bottom:
                    # block has moved past the bottom
                    if b['dir'] == DOWNLEFT:
                        b['dir'] = UPLEFT
                    if b['dir'] == DOWNRIGHT:
                        b['dir'] = UPRIGHT
                    if b['dir'] == UPLEFT:
                        b['dir'] = DOWNLEFT
                    if b['dir'] == UPRIGHT:
                        b['dir'] = DOWNRIGHT
                    b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))


                    # fix me \/
                if b['rect'].left < b2.left:
                    # block has moved past the left side
                    if b['dir'] == DOWNRIGHT:
                        b['dir'] = DOWNLEFT
                    if b['dir'] == UPRIGHT:
                        b['dir'] = UPLEFT
                    if b['dir'] == DOWNLEFT:
                        b['dir'] = DOWNRIGHT
                    if b['dir'] == UPLEFT:
                        b['dir'] = UPRIGHT
                    b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))
                if b['rect'].right > b2.right:
                    # block has moved past the right side
                    if b['dir'] == DOWNRIGHT:
                        b['dir'] = DOWNLEFT
                    if b['dir'] == UPRIGHT:
                        b['dir'] = UPLEFT
                    if b['dir'] == DOWNLEFT:
                        b['dir'] = DOWNRIGHT
                    if b['dir'] == UPLEFT:
                        b['dir'] = UPRIGHT
                    b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))

        # ball hits paddle1
        if player1.colliderect(b['rect']):
            if b['rect'].x > (player1.x + WINDOWWIDTH * .05):
                if b['dir'] == DOWNLEFT:
                    b['dir'] = UPRIGHT
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = UPRIGHT
            else:
                if b['dir'] == DOWNLEFT:
                    b['dir'] = UPLEFT
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = UPLEFT
            b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))
        # if player2.colliderect(b['rect']):
        #    if b['rect'].y>(player2.y+WINDOWHEIGHT*.1):
        #        if b['dir'] == UPRIGHT:
        #            b['dir'] = DOWNLEFT
        #        if b['dir'] == DOWNRIGHT:
        #            b['dir'] = DOWNLEFT
        #    else:
        #        if b['dir'] == UPRIGHT:
        #            b['dir'] = UPLEFT
        #        if b['dir'] == DOWNRIGHT:
        #            b['dir'] = UPLEFT
        #    b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))
        if b['rect'].top < 0:
            # block has moved past the top
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
            b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))
        if b['rect'].bottom > WINDOWHEIGHT + 10:
            '''# block has moved past the bottom
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
            b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))'''
            for i in range(len(balls)):
                if b == balls[i]:
                    balls.remove(b)
                    break
        if b['rect'].left < 0:
            # block has moved past the left side
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
            b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))
            '''for i in range(len(balls)):
                if b==balls[i]:
                    balls.remove(b)
                    break
            #p2score+=1'''
        if b['rect'].right > WINDOWWIDTH:
            # block has moved past the right side
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
            b['color'] = (random.randrange(256), random.randrange(256), random.randrange(256))
            '''for i in range(len(balls)):
                if b==balls[i]:
                    balls.remove(b)
                    break
            #p1score+=1'''
    for b in balls:
        # move the block data structure
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= b['speed']
            b['rect'].top += b['speed']
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += b['speed']
            b['rect'].top += b['speed']
        if b['dir'] == UPLEFT:
            b['rect'].left -= b['speed']
            b['rect'].top -= b['speed']
        if b['dir'] == UPRIGHT:
            b['rect'].left += b['speed']
            b['rect'].top -= b['speed']
    # draw the balls
    for i in range(len(balls)):
        pygame.draw.rect(windowSurface, WHITE, balls[i]['rect'])
        '''windowSurface.blit(pygame.font.SysFont("Comic Sans MS", int((balls[i]['rect'].width+balls[i]['rect'].height))).render('{},{}'.format(balls[i]['rect'].width,balls[i]['rect'].height), True, (255,255,255)), (balls[i]['rect'].x, balls[i]['rect'].y))
        windowSurface.blit(pygame.font.SysFont("Comic Sans MS", int((balls[i]['rect'].width+balls[i]['rect'].height))).render('{},{}'.format(balls[i]['rect'].x,balls[i]['rect'].y), True, (255,255,255)), (balls[i]['rect'].x, (balls[i]['rect'].y+balls[i]['rect'].height+20)))
        windowSurface.blit(pygame.font.SysFont("Comic Sans MS", int((balls[i]['rect'].width+balls[i]['rect'].height))).render('{},{}'.format(balls[i]['rect'].top,balls[i]['rect'].right), True, (255,255,255)), (balls[i]['rect'].x, (balls[i]['rect'].y+balls[i]['rect'].height+40)))
        windowSurface.blit(pygame.font.SysFont("Comic Sans MS", int((balls[i]['rect'].width+balls[i]['rect'].height))).render('{},{}'.format(balls[i]['rect'].right,balls[i]['rect'].top), True, (255,255,255)), (balls[i]['rect'].x, (balls[i]['rect'].y+balls[i]['rect'].height+60)))
        windowSurface.blit(pygame.font.SysFont("Comic Sans MS", int((player1.width+player1.height)/5)).render('{},{}'.format(player1.x,player1.y), True, (0,255,0)), (player1.x, player1.y))
        '''
    for i in range(len(blocks)):
        pygame.draw.rect(windowSurface, WHITE, blocks[i])
    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(120)
