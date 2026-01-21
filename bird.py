from gameObject import GameObject
class Bird(GameObject):
    def __init__(self, x, y, width, height, velocity, gravity, jump):
        super().__init__(x, y, width, height)
        self._velocity = velocity
        self._gravity = gravity
        self._jump = jump

    def update(self):
        self._velocity += self._gravity
        self._y += self._velocity

    def jump(self):
        self._velocity = -self._jump




        