import pygame

WHITE = (255, 255, 255)

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (10, 10), 10)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.math.Vector2(0, 0)
        self.friction = 0.95

    def update(self):
        # Apply velocity
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Apply friction
        self.velocity *= self.friction

        # Clamp small velocity values
        if abs(self.velocity.x) < 0.1:
            self.velocity.x = 0
        if abs(self.velocity.y) < 0.1:
            self.velocity.y = 0

        # Field boundaries
        field_left = 50
        field_right = 750 - self.rect.width
        field_top = 50
        field_bottom = 450 - self.rect.height

        if self.rect.left <= field_left:
            self.rect.left = field_left
            self.velocity.x *= -1

        if self.rect.right >= field_right + self.rect.width:
            self.rect.right = field_right + self.rect.width
            self.velocity.x *= -1

        if self.rect.top <= field_top:
            self.rect.top = field_top
            self.velocity.y *= -1

        if self.rect.bottom >= field_bottom + self.rect.height:
            self.rect.bottom = field_bottom + self.rect.height
            self.velocity.y *= -1
