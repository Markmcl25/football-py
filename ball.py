import pygame

WHITE = (255, 255, 255)

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (10, 10), 10)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.math.Vector2(0, 0)
        self.friction = 0.95  # Ball slows down gradually

    def update(self):
        # Apply velocity to position
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Apply friction to slow the ball down
        self.velocity *= self.friction

        # Clamp small velocity values to 0
        if abs(self.velocity.x) < 0.1:
            self.velocity.x = 0
        if abs(self.velocity.y) < 0.1:
            self.velocity.y = 0
