def in_exactly_one(l, s1, s2):
    return tuple(i for i in l if (i in s1 and not i in s2) or (i in s2 and not i in s1))

print(in_exactly_one(
    (3, 1, 4, 1, 5, 9, 2),
    frozenset((3, 0, 5, 6)),
    frozenset((2, 1, 5)),
)
)