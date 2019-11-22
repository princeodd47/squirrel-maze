class Weapon():
    def __init__(self, weapon_id, weapon_type, name, atk_bonus):
        self.id = weapon_id
        self.type = weapon_type
        self.name = name
        self.atk_bonus = atk_bonus

    def get_atk_bonus(self):
        switcher = {
            1: self.atk_bonus + 1  # Fire Sword
        }
        return switcher.get(self.id, self.atk_bonus)

    # def special_action(self, target):
    #     switcher = {
    #             3: lambda : action.stun(source, target)  # Stun baton
    #     }
    #     switcher.get(self.id, action.do_nothing())
