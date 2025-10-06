def odds_in_range(x, y):
    return frozenset(i for i in range(x, y + 1) if i % 2 == 1)


print(odds_in_range(0, 11))