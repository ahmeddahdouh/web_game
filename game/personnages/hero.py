import math
from datetime import date

from personnages.avatar import Avatar


class Hero(Avatar):
    """ Hero class with additional RPG mechanics """
    def __init__(self, name, race, classe, bag, equipment, element, profession):
        super().__init__(name, race, classe, bag, equipment, element)
        self.xp = 1
        self.profession = profession

    def gain_xp(self, xp_amount):
        """ Gain experience points and level up if needed """
        self.xp += xp_amount
        new_level = math.floor(self.xp / 100)
        
        if new_level > self.level:
            self.level_up()

    def level_up(self):
        """ Increase stats when leveling up """
        print("### Level Up! ###")
        stat_dict = self.stat.__dict__
        for stat in stat_dict:
            if stat not in ['attack', 'defense', 'life_point', 'endurance']:
                stat_dict[stat] += 5
        
        # Regenerate life points
        self.life = self.stat.life_point
        print("### Stats upgraded! ###")

    def save_character(self, format='txt'):
        """ Save character data """
        base_filename = f"{date.today()}_{self.id}_{self.name}"
        
        if format == 'txt':
            with open(f"{base_filename}.txt", 'w') as f:
                f.write(f"Name: {self.name}\n")
                f.write(f"Race: {self.race.name}\n")
                f.write(f"Class: {self.classe.name}\n")
                f.write(f"Level: {self.level}\n")
                f.write(f"XP: {self.xp}\n")
                
                # Write stats
                for stat, value in self.stat.__dict__.items():
                    f.write(f"{stat}: {value}\n")
                
                # Write equipment
                f.write("Equipment:\n")
                for item in self.equipment:
                    f.write(f"{item.name}\n")
                
                # Write bag items
                f.write("Bag:\n")
                for item in self.bag.items:
                    f.write(f"{item.name}\n")
        
        elif format == 'xml':
            root = ET.Element('hero')
            ET.SubElement(root, 'name').text = self.name
            ET.SubElement(root, 'race').text = self.race.name
            ET.SubElement(root, 'class').text = self.classe.name
            ET.SubElement(root, 'level').text = str(self.level)
            ET.SubElement(root, 'xp').text = str(self.xp)
            
            # Stats
            stats_elem = ET.SubElement(root, 'stats')
            for stat, value in self.stat.__dict__.items():
                ET.SubElement(stats_elem, stat).text = str(value)
            
            # Equipment
            equip_elem = ET.SubElement(root, 'equipment')
            for item in self.equipment:
                ET.SubElement(equip_elem, 'item').text = item.name
            
            # Bag
            bag_elem = ET.SubElement(root, 'bag')
            for item in self.bag.items:
                ET.SubElement(bag_elem, 'item').text = item.name
            
            tree = ET.ElementTree(root)
            tree.write(f"{base_filename}.xml", encoding='utf-8', xml_declaration=True)
