def make_list_with_updates(n, updates):
    l = [0] * n
    for i, v in updates:
        l[i] = v
    return l
print(make_list_with_updates(7, (
    (2, 5),
    (1, 10),
    (6, 5),
    (1, -5),
    (1, -5),
    (3, 0),
    (4, 4)
))
)