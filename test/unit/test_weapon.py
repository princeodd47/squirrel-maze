from unittest.mock import patch, call

from . import helpers as test_helpers
from squirrel_maze.resources import weapon

def test_initialize():
    weapon_ham = weapon.Weapon(0, 0, "Short Sword", 2)
    assert weapon_ham.id == 0
    assert weapon_ham.type == 0
    assert weapon_ham.name == "Short Sword"
    assert weapon_ham.damage == 2
