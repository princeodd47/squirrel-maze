from typing import List
from squirrel_maze.resources import helpers
from squirrel_maze.resources.actor import Actor


def fight(source: Actor, target: Actor) -> None:
    """Physical attack between actors. Target actor's hp is reduced by damage dealt."""
    src_atk_total = source.get_atk_value()
    tar_def_total = target.get_def_value()

    dmg = src_atk_total - tar_def_total
    if dmg < 1:
        dmg = 1

    print(
        "{} {} (hp: {}) attacks {} {} (hp: {}) for {} dmg.".format(
            source.actor_id,
            source.name,
            source.cur_hp,
            target.actor_id,
            target.name,
            target.cur_hp,
            dmg,
        )
    )

    target.cur_hp -= dmg


def fight_all(source: Actor, targets: List[Actor]) -> None:
    """Physical attack against multiple actors. Target actors' hp is reduced by damage dealt."""
    for target in targets:
        fight(source, target)


def fire_bolt(source: Actor, target: Actor) -> List:
    dmg_val = (
        helpers.get_rand_val(1, 2) + source.level + (source.cur_wil - target.cur_wil)
    )
    dmg = []
    dmg.append({"element": "fire", "damage": dmg_val})
    return dmg


def fire_punch(source: Actor, target: Actor) -> List:
    dmg = []
    dmg.append({"element": "fire", "damage": helpers.get_rand_val(1, 2) + source.level})
    dmg.append({"element": "none", "damage": helpers.get_rand_val(1, 10)})
    return dmg


def do_nothing() -> None:
    pass


def stun(source: Actor, target: Actor) -> None:
    pass
