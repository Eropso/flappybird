from gameObject import GameObject
class Bird(GameObject):
    def __init__(self, x, y, width, height, velocity, gravity, jump):
        super().__init__(x, y, width, height)
        self.y = y
        self._velocity = velocity
        self._gravity = gravity
        self._jump = jump

    def update(self):
        self._velocity += self._gravity
        self.y += self._velocity
        self.rect.y = self.y

    def check_collision(self, pipes):
        for pipe in pipes:
            if self.rect.colliderect(pipe.rect):
                self._velocity = 0
                self._gravity = 0
                self._jump = 0
                for p in pipes:
                    p._speed = 0



    def jump(self):
        self._velocity = -self._jump




        