import pygame
import sys
from player import Player
from player2 import Player2
from ball import Ball

# Kick mechanic for Player 1
kick_power = 0
max_power = 10
charging = False

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down 2D Football Game")

# Colors
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

clock = pygame.time.Clock()

# Control mappings
controls_p1 = {
    "left": pygame.K_a,
    "right": pygame.K_d,
    "up": pygame.K_w,
    "down": pygame.K_s
}

controls_p2 = {
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "up": pygame.K_UP,
    "down": pygame.K_DOWN
}

# Create players with their control mappings
player1 = Player(200, HEIGHT // 2, controls_p1)
player2 = Player2(600, HEIGHT // 2, controls_p2)

players_group = pygame.sprite.Group(player1, player2)

ball = Ball(WIDTH // 2, HEIGHT // 2)

ball_group = pygame.sprite.Group(ball)

score_left = 0
score_right = 0

# Font for scoreboard
font = pygame.font.SysFont(None, 48)

# Draw field function
def draw_field():
    SCREEN.fill(GREEN)
    pygame.draw.rect(SCREEN, WHITE, (50, 50, WIDTH - 100, HEIGHT - 100), 5)
    pygame.draw.line(SCREEN, WHITE, (WIDTH // 2, 50), (WIDTH // 2, HEIGHT - 50), 5)
    pygame.draw.circle(SCREEN, WHITE, (WIDTH // 2, HEIGHT // 2), 60, 5)
    pygame.draw.circle(SCREEN, WHITE, (WIDTH // 2, HEIGHT // 2), 5)
    pygame.draw.rect(SCREEN, WHITE, (50, 150, 100, 200), 5)
    pygame.draw.rect(SCREEN, WHITE, (WIDTH - 150, 150, 100, 200), 5)
    pygame.draw.rect(SCREEN, WHITE, (50, 200, 40, 100), 5)
    pygame.draw.rect(SCREEN, WHITE, (WIDTH - 90, 200, 40, 100), 5)
    pygame.draw.rect(SCREEN, GRAY, (40, 225, 10, 50))
    pygame.draw.rect(SCREEN, GRAY, (WIDTH - 50, 225, 10, 50))

# Draw field function
def draw_score():
    score_text = font.render(f"{score_left}   :   {score_right}", True, WHITE)
    SCREEN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

def reset_ball():
    ball.rect.center = (WIDTH // 2, HEIGHT // 2)
    ball.velocity = pygame.math.Vector2(0, 0)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Check collision with players and "kick" the ball
    if pygame.sprite.collide_rect(player1, ball):
        direction = pygame.math.Vector2(ball.rect.center) - pygame.math.Vector2(player1.rect.center)
        if direction.length() != 0:
            ball.velocity += direction.normalize() * 5

    if pygame.sprite.collide_rect(player2, ball):
        direction = pygame.math.Vector2(ball.rect.center) - pygame.math.Vector2(player2.rect.center)
        if direction.length() != 0:
            ball.velocity += direction.normalize() * 5

    # Each player now uses its own control set
    player1.update(keys)
    player2.update(keys)
    ball.update()

    # Goal detection (left and right goals)
    if 40 <= ball.rect.left <= 50 and 225 <= ball.rect.centery <= 275:
        score_right += 1
        reset_ball()

    if WIDTH - 50 <= ball.rect.right <= WIDTH - 40 and 225 <= ball.rect.centery <= 275:
        score_left += 1
        reset_ball()

    draw_field()
    players_group.draw(SCREEN)
    ball_group.draw(SCREEN)
    ball.update()
    draw_score()
    pygame.display.flip()
    clock.tick(60)
