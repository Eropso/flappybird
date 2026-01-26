from gameObject import GameObject
class Pipe(GameObject):
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height)
        self._speed = speed

    def update(self):
        self._x -= self._speed
    
    

