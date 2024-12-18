import random

from categories.stats import Stat


class Avatar:
    """Base class for characters"""

    id_counter = 0

    def __init__(self, name, race, classe, bag, equipment, element):
        Avatar.id_counter += 1
        self.id = Avatar.id_counter
        self.name = name
        self.race = race
        self.classe = classe
        self.bag = bag
        self.equipment = equipment
        self.element = element
        self.level = 1

        # Initialize base stats
        self.stat = Stat({})
        self.update_stats()

        self.life = self.stat.life_point
        self.statistics = {"fights": 0, "wins": 0, "max_damage": 0}

    def update_stats(self):
        """Update stats based on race, class, and equipment"""
        base_stats = {
            "strength": self.race.stat.strength + self.classe.stat.strength,
            "magic": self.race.stat.magic + self.classe.stat.magic,
            "agility": self.race.stat.agility + self.classe.stat.agility,
            "speed": self.race.stat.speed + self.classe.stat.speed,
            "charisma": self.race.stat.charisma + self.classe.stat.charisma,
            "chance": self.race.stat.chance + self.classe.stat.chance,
        }

        # Add equipment bonuses
        for equip in self.equipment:
            for stat_name, stat_value in equip.stat.__dict__.items():
                if stat_name in base_stats:
                    base_stats[stat_name] += stat_value

        # Recreate stat object with updated values
        self.stat = Stat(base_stats)

    def initiative(self):
        """Calculate initiative"""
        return random.randint(
            self.stat.speed, self.stat.agility + self.stat.chance + self.stat.speed
        )

    def attack_damage(self):
        """Calculate attack damage"""
        crit_chance = random.randint(0, self.stat.chance)

        if crit_chance > self.stat.chance / 2:
            print("Critical hit!")
            max_damage = random.randint(self.stat.attack, 2 * self.stat.attack)
        else:
            max_damage = random.randint(0, self.stat.attack)

        print(f"{self.name} deals {max_damage} damage")
        return max_damage

    def defend(self, damage):
        """Calculate damage defense"""
        dodge_chance = random.randint(
            self.stat.agility, self.stat.agility + self.stat.chance + self.stat.speed
        )
        max_dodge = self.stat.agility + self.stat.chance + self.stat.speed

        # Dodge logic
        if dodge_chance == max_dodge:
            print("Attack completely dodged!")
            return 0
        elif dodge_chance > max_dodge / 2:
            print("Partial dodge!")
            damage //= 2

        # Reduce damage by defense
        actual_damage = max(0, damage - self.stat.defense)

        # Reduce life
        self.life = max(0, self.life - actual_damage)

        print(f"{self.name} takes {actual_damage} damage. Remaining life: {self.life}")
        return actual_damage
