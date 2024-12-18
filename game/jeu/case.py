class Case:

    def __init__(self, **kwargs):
        self._gain = kwargs["gain"]
        self._perso = kwargs["perso"]
        self._obs = kwargs["obs"]

    def __int__(self, gain):
        self._gain = gain

    def get_penality(self):
        return self._obs.penality if self._obs is not None else 0

    def placer_personnage(self, personnage):
        self._perso = personnage

    def placer_obstacle(self, obstacle):
        self._obs = obstacle

    def enlever_personnage(self):
        self._perso = None

    def sans_personnage(self):
        return self._perso is None

    def sans_obstacle(self):
        return self._obs is None

    def __str__(self):
        if self.sans_obstacle() and self.sans_personnage():
            return f"Libre, (gain = {self._gain})"
        else:
            if not self.sans_obstacle():
                return f"Obstacle (penalité = - {self._obs.penality})"
            else:
                return f"{str(self._perso)} (penalité = {self._gain}))"
