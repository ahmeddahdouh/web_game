from personnages.avatar import Avatar


class Mobs(Avatar):
    def __init__(self, targs):
        Avatar.__init__(self, targs)
        self._type = targs["type"]

    def __str__(self):
        output = "Mobs " + self._type + " " + self._nom
        return output
