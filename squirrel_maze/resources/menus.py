from __future__ import print_function, unicode_literals

import sys

from PyInquirer import style_from_dict, Token, prompt, Separator, print_json
from pprint import pprint

from squirrel_maze.resources import combat

def main_menu():
    style = get_default_style()

    choices = [
        'combat',
        'create character (not implemented)',
        'load character (not implemented)',
        'Exit'
        ]

    questions = [
        {
            'type': 'list',
            'name': 'selection',
            'message': 'Squirrel Maze!?',
            'choices': choices
        }
    ]

    answers = prompt(questions)
    #print(answers)

    if 'not implemented' in answers['selection']:
        print("Feature not implemented")
        sys.exit()
    elif answers['selection'] == 'Exit':
        exit_game_menu('main')
    else:
        if answers['selection'] == 'combat':
            combat_menu()

def combat_menu():
    style = get_default_style()

    choices = [
        'Fight a Goblin',
        'Return'
        ]

    questions = [
        {
            'type': 'list',
            'name': 'selection',
            'message': 'Combat',
            'choices': choices
        }
    ]

    answers = prompt(questions)
    #print(answers)

    if 'not implemented' in answers['selection']:
        print("Feature not implemented")
        sys.exit()
    elif answers['selection'] == 'Return':
        go_to_menu('main')
    else:
        if answers['selection'] == 'Fight a Goblin':
            combat.combat_setup('Fight a Goblin')

def battle_menu(active_actor, actors):
    # TODO: write actor method to get a list of actions per actor
    #for action in actor.get_actions():

    # TODO: choices should be a dictionary to easily chose between targets

    style = get_default_style()

    choices = [
        'Fight a Goblin'
    ]

    # TODO: get id from actors of Goblin
    action.fight(active_actor, actor[0])

    # TODO: find a way to loop over actors, so they go in some sort of order
    # TODO: initiative

    battle_menu(actor[0], actors)

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

def go_to_menu(menu_name):
    if menu_name == 'main':
        main_menu()
    elif menu_name == 'combat':
        combat_menu()

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
