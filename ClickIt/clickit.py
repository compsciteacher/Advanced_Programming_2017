import pygame, sys
from pygame.locals import *
import time
pygame.init()

def main():

    #check if tie is moving
    moving=False
    shot=False
    #basic colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    PINK = (255, 0, 255)

    #starting tie location and destination
    tiex = 10
    tiey = 60
    destinationx=10
    destinationy=60
    movingL=False
    laserx=0
    lasery=0
    #tie image
    Tie = pygame.image.load('tie.png')

    #exit button
    exit_button=pygame.image.load('exit_unclicked.png')
    exit_clicked=pygame.image.load('exit_clicked.png')
    exitButton=False#exit hasn't been clicked yet

    #load button
    load_unclicked=pygame.image.load('load_unclicked.png')
    load_clicked=pygame.image.load('load_clicked.png')

    #save buttom
    save_unclicked=pygame.image.load('save_unclicked.png')
    save_clicked=pygame.image.load('save_clicked.png')

    #laser
    laser=pygame.image.load('tiny_laser.png')

    #audio
    soundObj = pygame.mixer.Sound('tie.wav')
    soundObj.set_volume(.2)

    #calculates destination to nearest 10, otherwise the tie goes crazy trying to get to location because it never reaches right number
    def destination(x,base=10):
        return int(base*round(float(x)/base))

    #saving to position file
    def saveIt(x,y):
        #print(destinationx, destinationy)
        saveit = open('position.txt', 'w')
        saveit.write(str(x) + ',' + str(y))
        saveit.close()
    def loadIt():
        fileref=open('position.txt','r')
        line=fileref.readline()
        nums=line.split(',')
        x=int(nums[0])
        y=int(nums[1])
        #print(x, y) debug it
        fileref.close()
        return(x,y)

    def moveValid(destinationx,destinationy,check):#FIX QUIRKS ON EDGES

        # all below is checking edges, if hits edge it goes as far as possible
        soundObj.play()
        # all below is checking edges, if hits edge it goes as far as possible
        if check=='x':
            if destinationx <= 10:
                destinationx = 10
            elif destinationx >= 400:
                destinationx = 400
        if check=='y':
            if destinationy >= 300:
                destinationy = 300
            elif destinationy <= 70:
                destinationy = 70
        return (destinationx,destinationy)

    def mouseCheck(mousex,mousey,destinationx,destinationy):
        exitButton=False
        # check if above line
        if mousey <= 60:
            #check exit
            if mousex <= 100 and mousex>=10:
                exitButton = True
                DISPLAYSURF.blit(exit_clicked, (10, 10))
            # SAVE CLICKED
            elif mousex >= 390 and mousex <= 490:
                DISPLAYSURF.blit(save_clicked, (390, 10))
                saveIt(destinationx, destinationy)
            #check load

            elif mousex >=200 and mousex<=300:
                soundObj.play()
                DISPLAYSURF.blit(load_clicked,(200,10))
                destinationx,destinationy=loadIt()

        else:
            soundObj.play()
            moving = True
            destinationx = destination(mousex - 50)  # subtract 50 to get center
            # all below is checking edges, if hits edge it goes as far as possible
            if destinationx <= 10:
                destinationx = 0
            elif destinationx >= 400:
                destinationx = 400
            destinationy = destination(mousey - 50)
            if destinationy >= 300:
                destinationy = 300
            elif destinationy <= 60:
                destinationy = 60

        return (destinationx,destinationy,exitButton)
    while True:# the main game loop
        FPS = 60 # frames per second setting
        fpsClock = pygame.time.Clock()
        #surface

        DISPLAYSURF = pygame.display.set_mode((500, 400))
        pygame.display.set_caption('TIE Flyer')

        #draw images
        DISPLAYSURF.blit(Tie, (tiex, tiey))  # paste tie at current x,y
        DISPLAYSURF.blit(exit_button, (10, 10))
        DISPLAYSURF.blit(save_unclicked,(390,10))
        DISPLAYSURF.blit(load_unclicked,(200,10))

        if exitButton:#if exit has been clicked, this way the image changes below, then on update exits after .1 sec
            pygame.time.wait(100)
            pygame.quit()
            sys.exit()

        if moving:#this checks to see if tie is currently moving, false to start, true after button is clicked
            if tiex > destinationx: #changes tie location to destination x,y
                tiex -= 10
            elif tiex < destinationx:
                tiex += 10
            if tiey > destinationy:
                tiey -= 10
            elif tiey < destinationy:
                tiey += 10

        if shot:#checks to see if shot and then moves laser shot
            laserstart+=15
            DISPLAYSURF.blit(laser, (laserstart, tiey + 50))
            if laserstart>600:
                shot=False



        for event in pygame.event.get():#event handling
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN: #if player clicks, changes tie to moving, and gets destination to nearest 10
                mousex, mousey = event.pos
                moving=True
                destinationx,destinationy,exitButton=mouseCheck(mousex,mousey,destinationx,destinationy)

                #key movements
            if event.type==KEYUP:
                if event.key == K_a:
                    print("grr")
                    movingL=False
            if event.type == KEYDOWN:
                moving=True
                if event.key==(K_1):
                    laserstart=tiex+50
                    DISPLAYSURF.blit(laser, (laserstart, tiey+50))
                    shot=True#changes laser to shot, will then blit at each new location

                if event.key in (K_LEFT, K_a):#LEFT

                    destinationx, destinationy = moveValid(destinationx, destinationy, 'x')
                    destinationx-=10

                elif event.key in (K_UP,K_w):#UP

                    destinationx, destinationy = moveValid(destinationx, destinationy,'y')
                    destinationy -= 10
                elif event.key in (K_DOWN,K_s):#DOWN

                    destinationx, destinationy = moveValid(destinationx, destinationy,'y')
                    destinationy += 10
                elif event.key in (K_RIGHT,K_d):#RIGHT

                    destinationx, destinationy = moveValid(destinationx, destinationy,'x')
                    destinationx += 10
                print(destinationx,destinationy)



        #print(mousex,mousey) this was for debugging

        # run the game loop
        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    main()