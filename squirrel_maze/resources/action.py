import random
from squirrel_maze.resources import helpers

def fight(source, target):
    # TODO: add function to calculate damage
    # to be used with all other physical attacks
    # TODO: dmg should be a list of dictionaries
    atk_rand = helpers.get_rand_val(1, 10)
    if helpers.is_critical_hit(atk_rand, source.cur_crit_hit_chance):
        atk_rand += helpers.get_crit_hit_bonus()
    elif helpers.is_critical_fail(atk_rand, source.cur_crit_fail_chance):
        atk_rand += helpers.get_crit_fail_bonus()

    src_atk_base = source.cur_str + source.cur_dex
    src_atk_total = src_atk_base + atk_rand
    if src_atk_total < 0:
        src_atk_total = 0

    def_rand = helpers.get_rand_val(1, 10)
    target_def = target.cur_sta + target.cur_dex + def_rand
    if target_def < 0:
        target_def = 0

    dmg = src_atk_total - target_def
    if dmg < 1:
        dmg = 1

    target.cur_hp -= dmg
    # TODO: fix
    #source.cur_sta_modify(-1)
    #target.cur_sta_modify(-1)

    print("{}({} + {} = {}) attacks {}({}) for {} dmg.".format(
        source.name, src_atk_base, atk_rand, src_atk_total,
        target.name, target_def, dmg))

def fight_all(source, targets):
    for target in targets:
        fight(source, target)

def fire_bolt(source, target):
    raise "not implemented"
    # TODO: calculate magic defense
    dmg = []
    dmg.append(
        {"element": "fire", "damage": get_rand_val(1, 2) + source.level}
    )
    return dmg

def fire_punch(source, target):
    raise "not implemented"
    # TODO: calculate magic defense
    # TODO: calculate normal attack
    dmg = []
    dmg.append(
        {"element": "fire", "damage": get_rand_val(1, 2) + source.level}
    )
    dmg.append(
        {"element": "none", "damage": get_rand_val(1, 10)}
    )
    return dmg
