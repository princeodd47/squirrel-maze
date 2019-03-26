from squirrel_maze.resources import helpers


def fight(source, target):
    # TODO: dmg should be a list of dictionaries
    src_atk_total = source.get_atk_value()
    tar_def_total = target.get_def_value()

    dmg = src_atk_total - tar_def_total
    if dmg < 1:
        dmg = 1

    print("{} {} (hp: {}) attacks {} {} (hp: {}) for {} dmg.".format(
        source.actor_id, source.name, source.cur_hp,
        target.actor_id, target.name, target.cur_hp, dmg)
    )

    target.cur_hp -= dmg
    # TODO: add stamina reduction
    # source.cur_sta_modify(-1)
    # target.cur_sta_modify(-1)

    # TODO: add helper.print_atk_result()


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
        {"element": "fire", "damage": helpers.get_rand_val(1, 2) + source.level}
    )
    dmg.append(
        {"element": "none", "damage": helpers.get_rand_val(1, 10)}
    )
    return dmg
