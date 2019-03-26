from __future__ import print_function, unicode_literals

import sys

from art import tprint
# from examples import custom_style_2
# from PyInquirer import style_from_dict, Token, prompt, Separator, print_json
from PyInquirer import style_from_dict, Token, prompt
# from pprint import pprint

from squirrel_maze.resources import actor
from squirrel_maze.resources import action
from squirrel_maze.resources import combat
from squirrel_maze.resources import npc

# TODO: change combat to be an object. This will allow for always
# being able to access actors and active actor

# TODO: Figure out how to change colors


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
    style = get_default_style()

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
            combat_menu()


def combat_menu():
    style = get_default_style()

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
            # TODO: Put in battle_setup()
            actors = []
            actors.append(actor.Actor(actor_id=len(actors), name='ham', pc_type='pc', level=1, max_hp=10, max_str=10,
                          max_dex=10, max_sta=10))
            actors.append(npc.get_big_goblin(actor_id=len(actors)))
            cur_battle = combat.Combat(actors)
            # TODO: write function to let player know what is going on
            print_battle_header(cur_battle)
            cur_battle.battle()


def print_battle_header(battle):
    print('Battle between:')
    for team in battle.teams:
        print("Team: {}: {}".format(team, battle.teams[team]))


def battle_menu(active_actor, actors):

    style = get_default_style()

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

    answers = prompt(questions)

    # TODO: initiative

    unfriendly_target_select_menu(active_actor, actors)


def unfriendly_target_select_menu(active_actor, actors):
    style = get_default_style()
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
    target_actor = actors[answers['selection']]
    action.fight(active_actor, target_actor)


def exit_game_menu(prev_menu):
    style = get_default_style()

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


# TODO: correct this function
# def actor_menu(actor, actors):
#     cur_menu = 'actor_menu'
#     style = get_default_style()
#
#     choices = [
#         'Fight'
#         ]
#
#     questions = [
#         {
#             'type': 'list',
#             'name': 'selection',
#             'message': 'Choose your action.',
#             'choices': choices
#         }
#     ]
#
#     answers = prompt(questions)
#     if answers['selection'] == 'Fight':
#         sys.exit()
#     else:
#         go_to_menu(prev_menu)


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
