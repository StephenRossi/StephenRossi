####################################################################
#
#                      DuckJumperV.1 - Stephen Rossi
#       Contact: SteveR@stephenkrossi.com or stephenrossi99@gmail.com
#
# File/Project Started 4/11/17 1:09PM
# Description: First pygame project intended to be a Duck jumping from
#              platform to platform.
#
# Controls:   TBA
#
####################################################################

import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))  #window size = 640x480
background = pygame.Surface(screen.get_size()) #creates an empty pygame surface
background.fill((215, 205, 175)) #fills background white
background = background.convert() #converts surface to make blittering faster
                            # surfaces with transparency need .convert_alpha()
screen.blit(background, (0, 0)) #place background at grid (0,0)
clock = pygame.time.Clock() # create clock object

circleSurface = pygame.Surface((50, 50)) #create surface for the ball
pygame.draw.circle(circleSurface, (0,0,225), (25,25),25) #draws circle
pygame.draw.rect(background, (0, 255, 0), (50, 50, 100, 25))
circlex = 320
circley = 240

screen.blit(circleSurface, (circlex, circley)) #blit corners of ball
screen.blit (background,(0,0))
mainloop = True
FPS = 60.00
playtime = 0.0
roundNum = 0


while mainloop:
    milliseconds = clock.tick(FPS) # do not go faster than this framerate
    roundThing = clock.tick(FPS) / 1000
    playtime += milliseconds / 1000.0 # add (mili)seconds to playtime
    roundNum += roundThing 
    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                mainloop = False

    #dispaly framerate and palytime in title
    text = "FPS: {0:.2f}   Playtime: {1:.2f}   Round: {2:.0f}".format(clock.get_fps(), playtime, roundNum)
    pygame.display.set_caption(text)

    #update display
    pygame.display.flip()

pygame.quit()
print("This game was played for {0:.2f} seconds".format(playtime),"and had a score of {0:.0f}!".format(roundNum))



                                   
