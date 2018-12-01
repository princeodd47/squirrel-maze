#from tabulate import tabulate
#from prettytable import PrettyTable
#from texttabele import Texttable
#terminaltables
#asciitable

class Actor:
    def __init__(self, pc_type, name, level, max_hp, max_str, max_dex, max_sta):
        self.pc_type = pc_type
        self.name = name
        self.level = level
        self.status = "normal"
        self.max_crit_hit_chance = 10
        self.cur_crit_hit_chance = 10
        self.max_crit_fail_chance = 0
        self.cur_crit_fail_chance = 0
        self.set_stats(max_hp, max_str, max_dex, max_sta)
    
    def set_stats(self, max_hp, max_str, max_dex, max_sta):
        self.max_hp = max_hp
        self.max_str = max_str
        self.max_dex = max_dex
        self.max_sta = max_sta
        self.cur_hp = max_hp
        self.cur_str = max_str
        self.cur_dex = max_dex
        self.cur_sta = max_sta

    def get_stat_list(self):
        stats = ["hp", "str", "dex", "sta",
                "crit_hit_chance", "crit_fail_chance"]
        return stats

    def print_char_sheet(self):
        raise "not implemented"

    def print_name(self):
        print(self.name)

    def print_attribute(self, attirbute):
        raise "not implemented"

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
        #stats = ["hp", "str", "agi", "sta",
        #        "crit_hit_chance", "crit_fail_chance"]
        stats = self.get_stat_list()
        for stat in stats:
            self.restore_stat_to_max(stat)

