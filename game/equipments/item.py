from categories.stats import Stat

class Item:
    """ base item class """
    def __init__(self, name, item_type, space, stat=None):
        self.name = name
        self.type = item_type
        self.space = space
        self.stat = stat or Stat({})

    def __str__(self):
        return self.name