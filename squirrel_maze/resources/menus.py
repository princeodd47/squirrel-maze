from __future__ import print_function, unicode_literals

import sys
from typing import List

from art import tprint
from PyInquirer import style_from_dict, Token, prompt

from squirrel_maze.resources.actor import Actor
from squirrel_maze.resources import action as sm_action
from squirrel_maze.resources import combat as sm_combat
from squirrel_maze.resources import helpers as sm_helpers
from squirrel_maze.resources import db_helpers as sm_db_helpers


def main_menu() -> None:
    tprint("squirrel_maze")
    _get_default_style()

    choices = [{"name": "Combat", "value": "combat"}, {"name": "Exit", "value": "exit"}]

    questions = [
        {
            "type": "list",
            "message": "Main Menu",
            "name": "selection",
            "choices": choices,
        }
    ]

    answers = prompt(questions)

    if "not implemented" in answers["selection"]:
        print("Feature not implemented")
        sys.exit()
    elif answers["selection"] == "exit":
        _exit_game_menu("main")
    else:
        if answers["selection"] == "combat":
            _location_menu()
            # combat_menu()


def format_location_item(location: dict, enemy: dict) -> dict:
    return {
        "name": f"{location['name']} - {enemy['name']}",
        "value": location["id"],
        "enemy_id": enemy["id"],
    }


def combat_menu() -> None:
    _get_default_style()

    choices = [
        {"name": "Big Goblin", "value": "goblin"},
        {"name": "Return", "value": "return"},
    ]

    questions = [
        {
            "type": "list",
            "name": "selection",
            "message": "Choose an opponent",
            "choices": choices,
        }
    ]

    answers = prompt(questions)

    if "not implemented" in answers["selection"]:
        print("Feature not implemented")
        sys.exit()
    elif answers["selection"] == "return":
        go_to_menu("main")
    else:
        # is this even used?
        if answers["selection"] == "goblin":
            actors = []
            db = sm_db_helpers.Database("squirrel_maze/data/db.json")
            actors.append(db.get_actor(0, pc_type="pc", affiliation="friendly"))
            actors.append(db.get_actor(1, pc_type="npc", affiliation="unfriendly"))
            db.close()
            cur_battle = sm_combat.Combat(actors)
            _print_battle_header(cur_battle)
            cur_battle.battle()


def battle_menu(active_actor: Actor, actors: List[Actor]) -> None:
    _get_default_style()

    choices = [{"key": "0", "name": "Fight", "value": "fight"}]

    questions = [
        {
            "type": "list",
            "name": "selection",
            "message": "{} - Choose an action".format(active_actor.name),
            "choices": choices,
        }
    ]

    prompt(questions)
    _unfriendly_target_select_menu(active_actor, actors)


def go_to_menu(menu_name: str) -> None:
    if menu_name == "main":
        main_menu()
    elif menu_name == "combat":
        combat_menu()


def victory() -> None:
    print("Congratulations, you win!")
    go_to_menu("main")


def defeat() -> None:
    print("You have lost...")
    go_to_menu("main")


def _get_default_style():  # type: ignore
    style = style_from_dict(
        {
            Token.Separator: "#cc5454",
            Token.QuestionMark: "#673ab7 bold",
            Token.Selected: "#cc5454",  # default
            Token.Pointer: "#673ab7 bold",
            Token.Instruction: "",  # default
            Token.Answer: "#f44336 bold",
            Token.Question: "",
        }
    )
    return style


def _unfriendly_target_select_menu(active_actor: Actor, actors: List[Actor]):  # type: ignore
    _get_default_style()
    choices = []

    for actor in sm_helpers.get_affiliated_actors("unfriendly", actors):
        choices.append(
            {
                "key": actor.actor_id,
                "name": "{}) {}".format(actor.actor_id, actor.name),
                "value": actor.actor_id,
            }
        )

    questions = [
        {
            "type": "list",
            "name": "selection",
            "message": "Fight -> Choose a target",
            "choices": choices,
        }
    ]

    answers = prompt(questions)
    for actor in actors:
        if actor.actor_id == answers["selection"]:
            target_actor = actor
    sm_action.fight(active_actor, target_actor)


def _exit_game_menu(prev_menu: str) -> None:
    _get_default_style()

    choices = ["Yes", "No"]

    questions = [
        {"type": "list", "name": "selection", "message": "Exit?", "choices": choices}
    ]

    answers = prompt(questions)
    if answers["selection"] == "Yes":
        sys.exit()
    else:
        go_to_menu(prev_menu)


def _location_menu() -> None:
    _get_default_style()

    choices = _get_location_menu_list()
    choices.append({"name": "Return", "value": 9999})

    questions = [
        {
            "type": "list",
            "name": "selection",
            "message": "Choose an opponent",
            "choices": choices,
        }
    ]

    answers = prompt(questions)

    if answers["selection"] == 9999:
        go_to_menu("main")
    else:
        actors = []
        db = sm_db_helpers.Database("squirrel_maze/data/db.json")
        actors.append(db.get_actor(2, pc_type="pc", affiliation="friendly"))
        actors.append(
            db.get_actor(
                choices[answers["selection"]]["enemy_id"],
                pc_type="npc",
                affiliation="unfriendly",
            )
        )
        db.close()
        cur_battle = sm_combat.Combat(actors)
        _print_battle_header(cur_battle)
        cur_battle.battle()


def _get_location_menu_list() -> List:
    db = sm_db_helpers.Database("squirrel_maze/data/db.json")
    locations = db.get_table_contents("locations")
    _location_menu_list = []
    for location in locations:
        enemy = db.get_actor_by_id(location["npcs"])
        _location_menu_list.append(format_location_item(location, enemy))
    db.close()
    return _location_menu_list


def _print_battle_header(battle) -> None:  # type: ignore
    print("Battle between:")
    for team in battle.teams:
        print("Team: {}: {}".format(team, battle.teams[team]))
