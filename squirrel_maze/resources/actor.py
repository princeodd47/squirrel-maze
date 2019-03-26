from tabulate import tabulate

from squirrel_maze.resources import helpers


class Actor:
    def __init__(self, actor_id=0, pc_type="npc", name="unknown", level=0, max_hp=0, max_str=0, max_dex=0, max_sta=0,
                 max_wil=0):
        self.actor_id = actor_id
        self.pc_type = pc_type
        self.name = name
        self.level = level
        self.status = "normal"
        self.max_crit_hit_chance = 10
        self.cur_crit_hit_chance = 10
        self.max_crit_fail_chance = 1
        self.cur_crit_fail_chance = 1
        self.set_stats(max_hp, max_str, max_dex, max_sta, max_wil)

    def set_stats(self, max_hp, max_str, max_dex, max_sta, max_wil):
        self.max_hp = max_hp
        self.max_str = max_str
        self.max_dex = max_dex
        self.max_sta = max_sta
        self.max_wil = max_wil
        self.cur_hp = max_hp
        self.cur_str = max_str
        self.cur_dex = max_dex
        self.cur_sta = max_sta
        self.cur_wil = max_wil

    def print_char_sheet(self):
        print(
            tabulate(
                {
                    "name": [self.name],
                    "level": [self.level],
                    "hp": [str("{}/{}".format(self.cur_hp, self.max_hp))],
                    "str": [str("{}/{}".format(self.cur_str, self.max_str))],
                    "dex": [str("{}/{}".format(self.cur_dex, self.max_dex))],
                    "sta": [str("{}/{}".format(self.cur_sta, self.max_sta))],
                    "wil": [str("{}/{}".format(self.cur_wil, self.max_wil))],
                    "crit_hit": [str("{}/{}".format(self.cur_crit_hit_chance, self.max_crit_hit_chance))],
                    "crit_fail": [str("{}/{}".format(self.cur_crit_fail_chance, self.max_crit_fail_chance))],
                },
                headers="keys",
                tablefmt="grid"
            )
        )

    def modify_stat(self, stat, value):
        self.__setattr__(stat, self.__getattribute__(stat) + value)

    def change_attribute(self, stat, value):
        self.__setattr__(stat, value)

    def get_sta_reduction(self):
        raise "not implemented"

    def get_crit_modifier(self):
        raise "not implemented"

    def restore_stat_to_max(self, stat):
        self.__setattr__("cur_{}".format(stat), self.__getattribute__("max_{}".format(stat)))

    def restore_all_stats_to_max(self):
        stats = helpers.get_stat_list()
        for stat in stats:
            self.restore_stat_to_max(stat)

    def get_atk_value(self):
        atk_rand = helpers.get_rand_val(1, 10)
        if helpers.is_critical_hit(atk_rand, self.cur_crit_hit_chance):
            atk_rand += helpers.get_crit_hit_bonus()
        elif helpers.is_critical_fail(atk_rand, self.cur_crit_fail_chance):
            atk_rand += helpers.get_crit_fail_bonus()
        atk_base = self.cur_str + self.cur_dex
        atk_total = atk_base + atk_rand
        if atk_total < 0:
            atk_total = 0
        return atk_total

    def get_def_value(self):
        def_rand = helpers.get_rand_val(1, 10)
        def_total = self.cur_sta + self.cur_dex + def_rand
        if def_total < 0:
            def_total = 0
        return def_total

    def get_friendly_actors(self, actors):
        friendlies = []
        for actor in actors:
            if self.pc_type == actor.pc_type:
                friendlies.append(actor)
        return friendlies

    def get_unfriendly_actors(self, actors):
        friendlies = []
        for actor in actors:
            if self.pc_type != actor.pc_type:
                friendlies.append(actor)
        return friendlies
