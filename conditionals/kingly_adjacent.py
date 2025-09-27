def are_kingly_adjacent(x1, y1, x2, y2):
    return (abs(x2 - x1) == 1 and abs(y2 - y1) == 1) or (x1 == x2 and abs(y2 - y1) == 1) or (y1 == y2 and abs(x2 - x1) == 1)

assert are_kingly_adjacent(11, 11, 12, 12) == True, are_kingly_adjacent(11, 11, 12, 12)
assert are_kingly_adjacent(11, 11, 33, 33) == False, are_kingly_adjacent(11, 11, 33, 33)