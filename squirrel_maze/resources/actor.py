from squirrel_maze.resources import helpers

EQUIPMENT_DEFAULTS = {
    'weapon': 0,
    'body': 0,
    'head': 0,
    'arm': 0,
    'accessory': 0
}

STAT_DEFAULTS = {
        'max_str': 10,
        'max_dex': 10,
        'max_sta': 10,
        'max_wil': 10,
        'max_hp': 10
}


class Actor:
    def __init__(self, actor_id: int = 0, level: int = 1, pc_type: str = "npc", affiliation: str = "friendly",
                 name: str = "unknown", stats: dict = STAT_DEFAULTS, equipment: dict = EQUIPMENT_DEFAULTS):
        self.actor_id = actor_id
        self.pc_type = pc_type
        self.affiliation = affiliation
        self.name = name
        self.level = level
        self.status = "normal"
        self.set_equipment(equipment)

        self._initialize_stats()
        self.set_stats(stats)
        self.restore_all_stats_to_max()

    def _initialize_stats(self) -> None:
        self.max_hp = 0
        self.max_str = 0
        self.max_dex = 0
        self.max_sta = 0
        self.max_wil = 0
        self.max_crit_hit_chance = 10
        self.max_crit_fail_chance = 1
        self.cur_hp = 0
        self.cur_str = 0
        self.cur_dex = 0
        self.cur_sta = 0
        self.cur_wil = 0
        self.cur_crit_hit_chance = 10
        self.cur_crit_fail_chance = 1

    def set_equipment(self, equipment: dict) -> None:
        self.equipment = {
            'weapon': equipment['weapon'],
            'body': equipment['body'],
            'head': equipment['head'],
            'arm': equipment['arm'],
            'accessory': equipment['accessory']
        }

    def update_equipment(self, equipment: dict) -> None:
        self.equipment.update(equipment)

    # def get_weapon(self):
    #     return self.equipment['weapon']

    def set_stats(self, stats: dict) -> None:
        if 'max_hp' in stats.keys():
            self.max_hp = stats['max_hp']
        else:
            self.max_hp = 10
        if 'max_str' in stats.keys():
            self.max_str = stats['max_str']
        else:
            self.max_str = 10
        if 'max_dex' in stats.keys():
            self.max_dex = stats['max_dex']
        else:
            self.max_dex = 10
        if 'max_sta' in stats.keys():
            self.max_sta = stats['max_sta']
        else:
            self.max_sta = 10
        if 'max_wil' in stats.keys():
            self.max_wil = stats['max_wil']
        else:
            self.max_wil = 10

    def modify_stat(self, stat: str, value: int) -> None:
        self.__setattr__(stat, self.__getattribute__(stat) + value)

    def set_stat(self, stat: str, value: int) -> None:
        self.__setattr__(stat, self.__getattribute__(stat))

    def change_attribute(self, stat: str, value: int) -> None:
        self.__setattr__(stat, value)

    def restore_stat_to_max(self, stat: str) -> None:
        self.__setattr__("cur_{}".format(stat), self.__getattribute__("max_{}".format(stat)))

    def restore_all_stats_to_max(self) -> None:
        stats = helpers.get_stat_list()
        for stat in stats:
            self.restore_stat_to_max(stat)

    def get_atk_value(self) -> int:
        atk_rand = helpers.get_rand_val(1, 10)
        if helpers.is_critical_hit(atk_rand, self.cur_crit_hit_chance):
            atk_rand += helpers.get_crit_hit_bonus()
        elif helpers.is_critical_fail(atk_rand, self.cur_crit_fail_chance):
            atk_rand += helpers.get_crit_fail_bonus()
        atk_base = self.cur_str + self.cur_dex
        atk_total = atk_base + atk_rand + self.get_weapon_bonus()
        if atk_total < 0:
            atk_total = 0
        return atk_total

    def get_def_value(self) -> int:
        def_rand = helpers.get_rand_val(1, 10)
        def_total = self.cur_sta + self.cur_dex + def_rand
        if def_total < 0:
            def_total = 0
        return def_total

    def get_weapon_bonus(self) -> int:
        return self.equipment['weapon']
