background_image_filename ="images.jpeg"
mouse_image_filename="home.jpg"

import pygame
import sys
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Hello Young Adventurer!!!")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the color
  

    # Draw a rectangle
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))  # Red rectangle

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
