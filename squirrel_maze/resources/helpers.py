import random

def get_rand_val(min_val, max_val):
    return random.randint(min_val, max_val)

def is_critical_hit(value, crit_hit_chance):
    if value >= crit_hit_chance:
        return True
    else:
        return False

def is_critical_fail(value, crit_fail_chance):
    if value <= crit_fail_chance:
        return True
    else:
        return False

def get_crit_hit_bonus():
    # TODO: add recursive addition on 10s
    # should that be an advantage?
    return int(get_rand_val(1, 10) / 2)

def get_crit_fail_bonus():
    #value = random.randint(1, 10) * -1
    value = int(get_rand_val(1, 10) / 2) * -1
    return value

def get_stat_list():
    stats = ["hp", "str", "dex", "sta", "wil",
            "crit_hit_chance", "crit_fail_chance"]
    return stats

def calc_magic_defense(source, target):
    return source.cur_wil - target.cur_wil

