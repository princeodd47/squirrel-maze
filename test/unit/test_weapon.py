from . import helpers as test_helpers


def test_initialize():
    weapon_ham = test_helpers.get_single_weapon()
    assert weapon_ham.id == 0
    assert weapon_ham.type == 0
    assert weapon_ham.name == "Short Sword"
    assert weapon_ham.damage == 2


def test_get_damage():
    weapon_ham = test_helpers.get_single_weapon()
    assert weapon_ham.get_damage() == 2
