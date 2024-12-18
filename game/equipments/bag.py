class Bag:
    """ Bag class to manage items """
    def __init__(self, max_size, items=None):
        self.max_size = max_size
        self.items = items or []

    def add_item(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
            return True
        return False

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            return self.items.pop(index)
        return None

    def __str__(self):
        return ", ".join(str(item) for item in self.items)