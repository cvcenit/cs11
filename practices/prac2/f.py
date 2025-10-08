def sets_containing_range(x, y, intsets):
    return tuple(intsets[i] for i in len(intsets) if intsets[i])


print(sets_containing_range(3, 6, (
    frozenset((3, 4, 5, 6, 7)),
    frozenset((2, 3, 4, 5, 6, 8)),
    frozenset((1, 2, 3, 5, 6, 7, 8)),
    frozenset(()),
    frozenset((3, 4, 5, 6)),
    frozenset((1, 2, 3, 4, 5)),
    frozenset((4, 5, 6, 7, 8)),
    frozenset((1, 2, 3, 4, 5, 6, 7, 8)),
)))