from decorators import *


def buy_cheapest(sacks):
    cheapest = find_cheapest(sacks)
    return cheapest, (sacks[:sacks.index(cheapest)] + sacks[1 + sacks.index(cheapest):])

def find_cheapest(sacks):
    if len(sacks) == 1:
        return sacks[0]
    else:
        if sacks[0] < sacks[1]:
            return find_cheapest((sacks[0],) + sacks[2:])
        else:
            return find_cheapest(sacks[1:])

print(buy_cheapest((31, 41, 59, 26, 53)))
print(buy_cheapest((33, 11, 44, 11, 55)))