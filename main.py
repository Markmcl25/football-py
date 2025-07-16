import pygame
import sys
from player import Player
from player2 import Player2
from ball import Ball

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

# Create players
player1 = Player(200, HEIGHT // 2, controls_p1)
player2 = Player2(600, HEIGHT // 2, controls_p2)

players_group = pygame.sprite.Group(player1, player2)

# Ball
ball = Ball(WIDTH // 2, HEIGHT // 2)
ball_group = pygame.sprite.Group(ball)

# Score
score_left = 0
score_right = 0
font = pygame.font.SysFont(None, 48)

# Kick mechanic for Player 1
kick_power_1 = 0
charging_1 = False

# Kick mechanic for Player 2
kick_power_2 = 0
charging_2 = False

max_power = 10

# Draw the field
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

# Draw scoreboard
def draw_score():
    score_text = font.render(f"{score_left}   :   {score_right}", True, WHITE)
    SCREEN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

# Draw power bar for Player 1
def draw_power_bar():
    if charging:
        bar_width = int((kick_power / max_power) * 100)
        pygame.draw.rect(SCREEN, WHITE, (30, 450, 100, 10), 2)
        pygame.draw.rect(SCREEN, (0, 255, 0), (30, 450, bar_width, 10))

# Reset the ball to center
def reset_ball():
    ball.rect.center = (WIDTH // 2, HEIGHT // 2)
    ball.velocity = pygame.math.Vector2(0, 0)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                charging_1 = True
            if event.key == pygame.K_RCTRL or event.key == pygame.K_KP_ENTER:
                charging_2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and charging_1:
                charging_1 = False
                if pygame.sprite.collide_rect(player1, ball):
                    direction = pygame.math.Vector2(ball.rect.center) - pygame.math.Vector2(player1.rect.center)
                    if direction.length() != 0:
                        ball.velocity += direction.normalize() * kick_power_1
                kick_power_1 = 0

            if (event.key == pygame.K_RCTRL or event.key == pygame.K_KP_ENTER) and charging_2:
                charging_2 = False
                if pygame.sprite.collide_rect(player2, ball):
                    direction = pygame.math.Vector2(ball.rect.center) - pygame.math.Vector2(player2.rect.center)
                    if direction.length() != 0:
                        ball.velocity += direction.normalize() * kick_power_2
                kick_power_2 = 0

    # Increase power while holding space
    keys = pygame.key.get_pressed()
    if charging_1:
        kick_power_1 += 0.2
        if kick_power_1 > max_power:
            kick_power_1 = max_power

    if charging_2:
        kick_power_2 += 0.2
        if kick_power_2 > max_power:
            kick_power_2 = max_power

    # Update players and ball
    player1.update(keys)
    player2.update(keys)
    ball.update()

    # Player 2 auto-kick (bump)
    if pygame.sprite.collide_rect(player2, ball) and not charging_2:
        direction = pygame.math.Vector2(ball.rect.center) - pygame.math.Vector2(player2.rect.center)
        if direction.length() != 0:
            ball.velocity += direction.normalize() * 2

    # Player 1 bump if not kicking
    if pygame.sprite.collide_rect(player1, ball) and not charging:
        direction = pygame.math.Vector2(ball.rect.center) - pygame.math.Vector2(player1.rect.center)
        if direction.length() != 0:
            ball.velocity += direction.normalize() * 2  # Smaller bump if not kicking

    # Goal detection
    if 40 <= ball.rect.left <= 50 and 225 <= ball.rect.centery <= 275:
        score_right += 1
        reset_ball()

    if WIDTH - 50 <= ball.rect.right <= WIDTH - 40 and 225 <= ball.rect.centery <= 275:
        score_left += 1
        reset_ball()

    # Draw everything
    draw_field()
    players_group.draw(SCREEN)
    ball_group.draw(SCREEN)
    draw_score()
    draw_power_bar()
    draw_power_bar_p2()
    pygame.display.flip()
    clock.tick(60)
