from squirrel_maze.resources import helpers

class Weapon:
    def __init__(self, weapon_id, weapon_type, name, damage):
        self.id = weapon_id
        self.type = weapon_type
        self.name = name
        self.damage = damage

    def get_damage(self):
        switcher = {
            1: self.damage + 1  # Fire Sword
        }
        return switcher.get(self.id, self.damage)
