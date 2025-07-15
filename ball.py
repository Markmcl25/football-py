def update(self):
    # Apply velocity
    self.rect.x += self.velocity.x
    self.rect.y += self.velocity.y

    # Apply friction
    self.velocity *= self.friction

    # Clamp very small values to 0
    if abs(self.velocity.x) < 0.1:
        self.velocity.x = 0
    if abs(self.velocity.y) < 0.1:
        self.velocity.y = 0

    # Wall collision — keep ball inside the field (between lines)
    field_left = 50
    field_right = 750 - self.rect.width  # 800 - 50 (right border) - ball width
    field_top = 50
    field_bottom = 450 - self.rect.height  # 500 - 50 (bottom border) - ball height

    if self.rect.left <= field_left:
        self.rect.left = field_left
        self.velocity.x *= -1  # Bounce

    if self.rect.right >= field_right + self.rect.width:
        self.rect.right = field_right + self.rect.width
        self.velocity.x *= -1

    if self.rect.top <= field_top:
        self.rect.top = field_top
        self.velocity.y *= -1

    if self.rect.bottom >= field_bottom + self.rect.height:
        self.rect.bottom = field_bottom + self.rect.height
        self.velocity.y *= -1
