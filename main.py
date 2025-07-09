import pygame
import sys
from player import Player  # Import the Player class from player.py

# Initialize Pygame
pygame.init()

# Set screen dimensions and create the game window
WIDTH, HEIGHT = 800, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down 2D Football Game")

# Define colors
GREEN = (0, 128, 0)     # Field color
WHITE = (255, 255, 255) # Lines and borders
GRAY = (100, 100, 100)  # Goal color

# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Create a Player object positioned at the center of the field
player = Player(WIDTH // 2, HEIGHT // 2)

# Create a sprite group to manage drawing and updating
player_group = pygame.sprite.Group()
player_group.add(player)

# Function to draw the football field
def draw_field():
    SCREEN.fill(GREEN)  # Fill the background with green (grass)

    # Draw outer field border
    pygame.draw.rect(SCREEN, WHITE, (50, 50, WIDTH - 100, HEIGHT - 100), 5)

    # Center line
    pygame.draw.line(SCREEN, WHITE, (WIDTH // 2, 50), (WIDTH // 2, HEIGHT - 50), 5)

    # Center circle
    pygame.draw.circle(SCREEN, WHITE, (WIDTH // 2, HEIGHT // 2), 60, 5)

    # Center spot
    pygame.draw.circle(SCREEN, WHITE, (WIDTH // 2, HEIGHT // 2), 5)

    # Penalty boxes (left and right)
    pygame.draw.rect(SCREEN, WHITE, (50, 150, 100, 200), 5)
    pygame.draw.rect(SCREEN, WHITE, (WIDTH - 150, 150, 100, 200), 5)

    # Goal boxes (left and right)
    pygame.draw.rect(SCREEN, WHITE, (50, 200, 40, 100), 5)
    pygame.draw.rect(SCREEN, WHITE, (WIDTH - 90, 200, 40, 100), 5)

    # Goals (grey rectangles beyond the field)
    pygame.draw.rect(SCREEN, GRAY, (40, 225, 10, 50))  # Left goal
    pygame.draw.rect(SCREEN, GRAY, (WIDTH - 50, 225, 10, 50))  # Right goal

# Game loop - runs forever until user quits
while True:
    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Cleanly exit pygame
            sys.exit()     # Exit the Python script

    # Get keys currently pressed
    keys = pygame.key.get_pressed()

    # Update player based on input
    player.update(keys)

    # Draw everything on the screen
    draw_field()              # Draw football field
    player_group.draw(SCREEN)  # Draw the player

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)
