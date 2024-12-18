class Classe:
    """ class type """
    def __init__(self, name, stat):
        self.name = name
        self.stat = stat

    def __str__(self):
        return self.name