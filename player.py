import pygame

# Define a color for the player (blue square)
BLUE = (0, 0, 255)

# Create a Player class that inherits from Pygame's built-in Sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()  # Call the parent class (Sprite) constructor

        # Create a surface (image) for the player sprite - a blue square
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)  # Fill the surface with blue color

        # Create a rectangle around the image to track position and collisions
        self.rect = self.image.get_rect(center=(x, y))  # Start at (x, y)

        # Set movement speed
        self.speed = 5

    def update(self, keys):
        """
        Move the player based on which keys are currently being pressed.
        Accepts a 'keys' list from pygame.key.get_pressed()
        """
        # Move left (arrow key or A)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        # Move right (arrow key or D)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        # Move up (arrow key or W)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        # Move down (arrow key or S)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
