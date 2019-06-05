from __future__ import print_function, unicode_literals

import sys

from art import tprint
from PyInquirer import style_from_dict, Token, prompt

from squirrel_maze.resources import action as sm_action
from squirrel_maze.resources import combat as sm_combat
from squirrel_maze.resources import db_helpers as sm_db_helpers


def get_default_style():
    style = style_from_dict({
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })
    return style


def main_menu():
    tprint('squirrel_maze')
    get_default_style()

    choices = [
        {
            'name': 'Combat',
            'value': 'combat'
        },
        {
            'name': 'Exit',
            'value': 'exit'
        }
    ]

    questions = [
        {
            'type': 'list',
            'message': 'Main Menu',
            'name': 'selection',
            'choices': choices
        }
    ]

    answers = prompt(questions)

    if 'not implemented' in answers['selection']:
        print("Feature not implemented")
        sys.exit()
    elif answers['selection'] == 'exit':
        exit_game_menu('main')
    else:
        if answers['selection'] == 'combat':
            location_menu()
            # combat_menu()


def location_menu():
    get_default_style()

    choices = get_location_menu_list()
    choices.append({'name': 'Return', 'value': 9999})

    questions = [
        {
            'type': 'list',
            'name': 'selection',
            'message': 'Choose an opponent',
            'choices': choices
        }
    ]

    answers = prompt(questions)

    if answers['selection'] == 9999:
        go_to_menu('main')
    else:
        actors = []
        db = sm_db_helpers.Database('squirrel_maze/data/db.json')
        actors.append(db.get_actor(2, pc_type='pc', affiliation='friendly'))
        actors.append(db.get_actor(choices[answers['selection']]['enemy_id'], pc_type='npc', affiliation='unfriendly'))
        db.close()
        cur_battle = sm_combat.Combat(actors)
        print_battle_header(cur_battle)
        cur_battle.battle()


def get_location_menu_list():
    db = sm_db_helpers.Database('squirrel_maze/data/db.json')
    locations = db.get_table_contents('locations')
    location_menu_list = []
    for location in locations:
        enemy = db.get_actor_by_id(location['npcs'])
        location_menu_list.append(format_location_item(location, enemy))
    db.close()
    return location_menu_list


def format_location_item(location, enemy):
    return {'name': f"{location['name']} - {enemy['name']}", 'value': location['id'], 'enemy_id': enemy['id']}


def combat_menu():
    get_default_style()

    choices = [
        {
            'name': 'Big Goblin',
            'value': 'goblin'
        },
        {
            'name': 'Return',
            'value': 'return'
        }
    ]

    questions = [
        {
            'type': 'list',
            'name': 'selection',
            'message': 'Choose an opponent',
            'choices': choices
        }
    ]

    answers = prompt(questions)

    if 'not implemented' in answers['selection']:
        print("Feature not implemented")
        sys.exit()
    elif answers['selection'] == 'return':
        go_to_menu('main')
    else:
        if answers['selection'] == 'goblin':
            actors = []
            db = sm_db_helpers.Database('squirrel_maze/data/db.json')
            actors.append(db.get_actor('pcs', 0, pc_type='pc', affiliation='friendly'))
            actors.append(db.get_actor('npcs', 1, pc_type='npc', affiliation='unfriendly'))
            db.close()
            cur_battle = sm_combat.Combat(actors)
            print_battle_header(cur_battle)
            cur_battle.battle()


def print_battle_header(battle):
    print('Battle between:')
    for team in battle.teams:
        print("Team: {}: {}".format(team, battle.teams[team]))


def battle_menu(active_actor, actors):
    get_default_style()

    choices = [
        {
            'key': '0',
            'name': 'Fight',
            'value': 'fight'
        }
    ]

    questions = [
        {
            'type': 'list',
            'name': 'selection',
            'message': "{} - Choose an action".format(active_actor.name),
            'choices': choices
        }
    ]

    prompt(questions)
    unfriendly_target_select_menu(active_actor, actors)


def unfriendly_target_select_menu(active_actor, actors):
    get_default_style()
    choices = []

    for actor in active_actor.get_unfriendly_actors(actors):
        choices.append(
            {
                'key': actor.actor_id,
                'name': "{}) {}".format(actor.actor_id, actor.name),
                'value': actor.actor_id
            }
        )

    questions = [
        {
            'type': 'list',
            'name': 'selection',
            'message': 'Fight -> Choose a target',
            'choices': choices
        }
    ]

    answers = prompt(questions)
    for actor in actors:
        if actor.actor_id == answers['selection']:
            target_actor = actor
    sm_action.fight(active_actor, target_actor)


def exit_game_menu(prev_menu):
    get_default_style()

    choices = [
        'Yes',
        'No'
        ]

    questions = [
        {
            'type': 'list',
            'name': 'selection',
            'message': 'Exit?',
            'choices': choices
        }
    ]

    answers = prompt(questions)
    if answers['selection'] == 'Yes':
        sys.exit()
    else:
        go_to_menu(prev_menu)


def go_to_menu(menu_name):
    if menu_name == 'main':
        main_menu()
    elif menu_name == 'combat':
        combat_menu()


def victory():
    print("Congratulations, you win!")
    go_to_menu('main')


def defeat():
    print("You have lost...")
    go_to_menu('main')
