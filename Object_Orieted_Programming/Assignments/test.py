import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Test")

# Set a color
color = (0, 128, 255)  # RGB color (blue)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the color
    screen.fill(color)

    # Draw a rectangle
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))  # Red rectangle

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
