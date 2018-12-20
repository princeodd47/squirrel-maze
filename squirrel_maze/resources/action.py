import random
from squirrel_maze.resources import helpers

def fight(source, target):
    # TODO: dmg should be a list of dictionaries
    src_atk_total = source.get_atk_value()
    tar_def_total = target.get_def_value()

    dmg = src_atk_total - tar_def_total
    if dmg < 1:
        dmg = 1

    target.cur_hp -= dmg
    # TODO: add stamina reduction
    #source.cur_sta_modify(-1)
    #target.cur_sta_modify(-1)

    # TODO: add helper.print_atk_result()
    print("{}({}) attacks {}({}) for {} dmg.".format(
        source.name, src_atk_total, target.name,
        tar_def_total, dmg)
    )

def fight_all(source, targets):
    for target in targets:
        fight(source, target)

def fire_bolt(source, target):
    dmg_val = helpers.get_rand_val(1, 2) + source.level + (source.cur_wil - target.cur_wil)
    dmg = []
    dmg.append(
        {"element": "fire", "damage": dmg_val}
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
