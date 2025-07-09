import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down 2D Football Field")

# Colors
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# Field dimensions
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
CENTER_RADIUS = 60

def draw_field():
    SCREEN.fill(GREEN)

    # Outer border
    pygame.draw.rect(SCREEN, WHITE, (50, 50, WIDTH - 100, HEIGHT - 100), 5)

    # Center line
    pygame.draw.line(SCREEN, WHITE, (WIDTH // 2, 50), (WIDTH // 2, HEIGHT - 50), 5)

    # Center circle
    pygame.draw.circle(SCREEN, WHITE, (CENTER_X, CENTER_Y), CENTER_RADIUS, 5)

    # Center spot
    pygame.draw.circle(SCREEN, WHITE, (CENTER_X, CENTER_Y), 5)

    # Penalty boxes
    pygame.draw.rect(SCREEN, WHITE, (50, 150, 100, 200), 5)  # Left
    pygame.draw.rect(SCREEN, WHITE, (WIDTH - 150, 150, 100, 200), 5)  # Right

    # Goal boxes
    pygame.draw.rect(SCREEN, WHITE, (50, 200, 40, 100), 5)  # Left small box
    pygame.draw.rect(SCREEN, WHITE, (WIDTH - 90, 200, 40, 100), 5)  # Right small box

    # Goals
    pygame.draw.rect(SCREEN, GRAY, (40, 225, 10, 50))  # Left goal
    pygame.draw.rect(SCREEN, GRAY, (WIDTH - 50, 225, 10, 50))  # Right goal

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_field()
    pygame.display.flip()
    clock.tick(60)
