def in_neither_half_interval(a, b, c, d, y):
    return not (a <= y < b or c <= y < d)

assert in_neither_half_interval(2023, 2033, 2000, 2010, 2033) == True