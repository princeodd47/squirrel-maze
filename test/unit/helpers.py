from squirrel_maze.resources import actor
from squirrel_maze.resources import weapon


def get_single_actor():
    return actor.Actor(actor_id=0, name='ham', level=1, pc_type='pc', affiliation='friendly',
                       stats={'max_hp': 10, 'max_str': 10, 'max_dex': 10, 'max_sta': 10},
                       equipment={'weapon': 1, 'body': 0, 'head': 0, 'arm': 0, 'accessory': 0})


def get_multiple_actors():
    actors = []
    actors.append(actor.Actor(actor_id=0, name='ham', pc_type='pc', affiliation='friendly',
                  stats={'max_hp': 10, 'max_str': 10, 'max_dex': 12, 'max_sta': 10}))
    actors.append(actor.Actor(actor_id=1, name='spam', pc_type='pc', affiliation='friendly',
                  stats={'max_hp': 10, 'max_str': 10, 'max_dex': 10, 'max_sta': 10}))
    actors.append(actor.Actor(actor_id=2, name='eggs', pc_type='pc', affiliation='friendly',
                  stats={'max_hp': 5, 'max_str': 5, 'max_dex': 5, 'max_sta': 5}))
    actors.append(actor.Actor(actor_id=3, name='foo', pc_type='npc', affiliation='friendly',
                  stats={'max_hp': 6, 'max_str': 6, 'max_dex': 6, 'max_sta': 6}))
    actors.append(actor.Actor(actor_id=4, name='bar', pc_type='npc', affiliation='unfriendly',
                  stats={'max_hp': 6, 'max_str': 6, 'max_dex': 6, 'max_sta': 6}))
    actors.append(actor.Actor(actor_id=5, name='baz', pc_type='npc', affiliation='unfriendly',
                  stats={'max_hp': 2, 'max_str': 2, 'max_dex': 2, 'max_sta': 2}))
    return actors


def get_single_weapon():
    return weapon.Weapon(weapon_id=0, name="Short Sword", weapon_type=0, atk_bonus=2)
