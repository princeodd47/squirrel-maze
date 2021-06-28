import random
from typing import List


def get_rand_val(min_val: int, max_val: int) -> int:
    return random.randint(min_val, max_val)


def is_critical_hit(value: int, crit_hit_chance: int) -> bool:
    if value >= crit_hit_chance:
        return True
    else:
        return False


def is_critical_fail(value: int, crit_fail_chance: int) -> bool:
    if value <= crit_fail_chance:
        return True
    else:
        return False


def get_crit_hit_bonus() -> int:
    return int(get_rand_val(1, 10) / 2)


def get_crit_fail_bonus() -> int:
    value = int(get_rand_val(1, 10) / 2) * -1
    return value


def get_stat_list() -> List[str]:
    stats = ["hp", "str", "dex", "sta", "wil", "crit_hit_chance", "crit_fail_chance"]
    return stats


def calc_magic_defense(source, target) -> int:  # type: ignore
    return source.cur_wil - target.cur_wil


def any_members_alive(actors, pc_type: str) -> bool:  # type: ignore
    for actor in actors:
        if actor.pc_type == pc_type and actor.cur_hp > 0:
            return True
    return False


def get_actor_list_by_stat(actors, stat_primary: str, stat_secondary: str):  # type: ignore
    sorted_actors = sorted(
        actors,
        key=lambda actor: (
            getattr(actor, stat_primary),
            getattr(actor, stat_secondary),
        ),
        reverse=True,
    )
    return sorted_actors


def get_max_stat_from_actor_list(actors, stat: str) -> int:  # type: ignore
    max_val = max(getattr(actor, stat) for actor in actors)
    return max_val


def get_affiliated_actors(affiliation: str, compared_actors):  # type: ignore
    return [actor for actor in compared_actors if affiliation == actor.affiliation]
