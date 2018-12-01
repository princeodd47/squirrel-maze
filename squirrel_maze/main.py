import pprint
import random
import resources.action as action
import resources.npc as npc
from resources.actor import Actor

random.seed()

foo = Actor("pc", "foo", 1, 10, 4, 3, 4)

# example create npcs
gob1 = npc.get_goblin("gob1")
gob2 = npc.get_goblin("gob2")

# print object attributes
#pprint.pprint(dir(foo))

# example loop over fight commands
#for i in range(1, 10):
#    action.fight(foo, gob1)

# example fight list of targets
#targets = []
#targets.append(gob1)
#targets.append(gob2)
#action.fight_all(foo, targets)

# example fight until one's hp is reduced to 0
#while foo.cur_hp > 0:
#    action.fight(foo, gob1)
#    if gob1.cur_hp > 0:
#        action.fight(gob1, foo)
#    else:
#        break

# example change attribute
#print("name = {}".format(foo.name))
#foo.change_attribute("name", "hank")
#print("name = {}".format(foo.name))

# example reduce stamina
#print("cur_sta = {}".format(foo.cur_sta))
#foo.modify_stat("cur_sta", -2)
#print("cur_sta = {}".format(foo.cur_sta))

# example restore attibute
#foo.restore_stat_to_max("sta")
#print("cur_sta = {}".format(foo.cur_sta))

# example restore all attributes
#print("cur_sta = {} ".format(foo.cur_sta), end="")
#print("max_sta = {} ".format(foo.max_sta), end="")
#print(" | ", end="")
#print("cur_str = {} ".format(foo.cur_str), end="")
#print("max_str = {} ".format(foo.max_str), end="")
#print("")
#foo.modify_stat("cur_sta", -1)
#foo.modify_stat("cur_str", -3)
#print("cur_sta = {} ".format(foo.cur_sta), end="")
#print("max_sta = {} ".format(foo.max_sta), end="")
#print(" | ", end="")
#print("cur_str = {} ".format(foo.cur_str), end="")
#print("max_str = {} ".format(foo.max_str), end="")
#print("")
#foo.restore_all_stats_to_max()
#print("cur_sta = {} ".format(foo.cur_sta), end="")
#print("max_sta = {} ".format(foo.max_sta), end="")
#print(" | ", end="")
#print("cur_str = {} ".format(foo.cur_str), end="")
#print("max_str = {} ".format(foo.max_str), end="")
#print("")

foo.print_char_sheet()
