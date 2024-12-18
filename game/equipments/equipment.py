from equipments.item import Item


class Equipment(Item):
    """ equipment item class """
    def __init__(self, name, item_type, space, place, classes, stat=None):
        super().__init__(name, item_type, space, stat)
        self.place = place
        self.allowed_classes = classes