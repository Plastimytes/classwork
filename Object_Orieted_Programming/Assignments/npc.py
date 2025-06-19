#Importing
import pygame
import sys

#Initalizing pygame
pygame.init()

#Dimensions on theb screeen
Screen_width = 720
Screen_height = 1080
screen = pygame.display.set_mode((Screen_width, Screen_height))
pygame.display.set_caption('Andreas demo')

#To keep the screen open create a game loop like so;
#sat open screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#If user clicks quit
            running = False

    screen.fill((0,0,0))#Fills screen with a certain color. In this case black

    #Updating the display
    pygame.display.flip() #You acn use pygame.display.update()

#Quit the screen
pygame.quit()
sys.exit()            