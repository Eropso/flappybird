from gameObject import GameObject

# Class representing the bird
class Bird(GameObject):
    def __init__(self, x, y, width, height, velocity, gravity, jump):
        super().__init__(x, y, width, height)
        self.y = y
        self._velocity = velocity
        self._gravity = gravity
        self._jump = jump

    # Updates position
    def update(self):
        self._velocity += self._gravity
        self.y += self._velocity
        self.rect.y = self.y

    # Checks collision with pipes or floor/ceiling
    def check_collision(self, pipes, window_height):
        if self.rect.bottom >= window_height or self.rect.top < 0:
            self._velocity = 0
            self._gravity = 0
            self._jump = 0
            for p in pipes:
                p._speed = 0

        for pipe in pipes:
            if self.rect.colliderect(pipe.rect.inflate(-88, 5)):
                self._velocity = 0
                self._gravity = 0
                self._jump = 0
                for p in pipes:
                    p._speed = 0



    # bird jump
    def jump(self):
        self._velocity = -self._jump




        