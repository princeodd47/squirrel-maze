import random

def get_rand_val(min_val, max_val):
    return random.randint(min_val, max_val)

def is_critical_hit(value, crit_hit_chance):
    if value >= crit_hit_chance:
        return True
    else:
        return False

def is_critical_fail(value, crit_fail_chance):
    if value <= crit_fail_chance:
        return True
    else:
        return False

def get_crit_hit_bonus():
    # TODO: add recursive addition on 10s
    return get_rand_val(1, 10)
    

def get_crit_fail_bonus(value):
    value = random.randint(1, 10) * -1
    return value
