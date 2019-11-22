from . import helpers as test_helpers


def test_initialize():
    weapon_ham = test_helpers.get_single_weapon()
    assert weapon_ham.id == 0
    assert weapon_ham.type == 0
    assert weapon_ham.name == "Short Sword"
    assert weapon_ham.atk_bonus == 2


def test_get_atk_bonus():
    weapon_ham = test_helpers.get_single_weapon()
    assert weapon_ham.get_atk_bonus() == 2
