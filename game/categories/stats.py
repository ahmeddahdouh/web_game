import random

class Stat:
    """ stat of the player """
    def __init__(self, dict_args):
        self.strength = dict_args.get('strength', 1)
        self.magic = dict_args.get('magic', 1)
        self.agility = dict_args.get('agility', 1)
        self.speed = dict_args.get('speed', 1)
        self.charisma = dict_args.get('charisma', 0)
        self.chance = dict_args.get('chance', 0)

        # Fix random stat generation
        self.endurance = random.randint(
            self.strength + self.agility, 
            2 * (self.strength + self.agility)
        )
        self.life_point = random.randint(
            self.endurance, 
            2 * self.endurance
        )
        self.attack = self.strength + self.magic + self.agility
        self.defense = self.agility + self.speed + self.endurance

    def __str__(self):
        return str(self.__dict__)