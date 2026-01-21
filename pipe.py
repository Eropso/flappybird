from gameObject import GameObject
class Pipe(GameObject):
    def __init__(self, x, y, width, height, speed, passes):
        super().__init__(x, y, width, height)
        self._speed = speed
        self._passes = passes

