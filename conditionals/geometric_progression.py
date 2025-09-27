def is_geometric_progression(r, g, y):
    return r == g == y or g*g == y*r and r != g

assert is_geometric_progression(1, 1, 1) == True, is_geometric_progression(1, 1, 1)
assert is_geometric_progression(0, 0, 0) == True
assert is_geometric_progression(-1, 1, -1) == True, is_geometric_progression(-1, 1, -1)
assert is_geometric_progression(1, -1, 1) == True, is_geometric_progression(1, -1, 1)
assert is_geometric_progression(1, 0, 0) == True
assert is_geometric_progression(0, 0, 1) == False