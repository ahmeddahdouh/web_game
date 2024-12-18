class Obstacle:
    nbObstacle = 0

    def __init__(self, penality):
        self._penality = penality
        self.nbObstacle += 1

    @property
    def penality(self):
        return self._penality

    @penality.setter
    def penality(self, value):
        self._penality = value
