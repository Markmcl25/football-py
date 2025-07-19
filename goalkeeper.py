import pygame

class Goalkeeper(pygame.sprite.Sprite):
    def __init__(self, x, y, is_left=True):
        super().__init__()
        self.image = pygame.Surface((20, 60))
        self.image.fill((0, 0, 255))  # Blue keeper
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 4
        self.is_left = is_left

    def update(self, ball_y):
        # Follow ball's Y position but clamp within the goal
        if self.rect.centery < ball_y:
            self.rect.centery += self.speed
        elif self.rect.centery > ball_y:
            self.rect.centery -= self.speed

        # Stay within vertical bounds of goal
        self.rect.centery = max(175, min(self.rect.centery, 325))  # Goal height range

    def deflect(self, ball):
        # Push the ball away in a direction based on which goal
        direction = pygame.math.Vector2(ball.rect.center) - pygame.math.Vector2(self.rect.center)
        if direction.length() != 0:
            direction = direction.normalize()
            ball.velocity = direction * ball.velocity.length() * 0.8  # reduce speed slightly
