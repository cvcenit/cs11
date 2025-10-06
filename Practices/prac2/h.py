def products(s1, s2, s):
    return frozenset(x*y for x in s1 for y in s2 if x + y == s)

print(products(
    frozenset((3, 1, 4, 2, 5)),
    frozenset((4, 6, 8, 10, 12)),
    9,
)
)