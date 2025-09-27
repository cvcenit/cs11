def o_wins(grid):
    return (grid[0][0] == grid[0][1] == grid[0][2] == "O") or (grid[1][0] == grid[1][1] == grid[1][2] == "O") or (grid[2][0] == grid[2][1] == grid[2][2] == "O") or (grid[0][0] == grid[1][0] == grid[2][0] == "O") or (grid[0][1] == grid[1][1] == grid[2][1] == "O") or (grid[0][2] == grid[1][2] == grid[2][2] == "O") or (grid[0][0] == grid[1][1] == grid[2][2] == "O") or (grid[0][2] == grid[1][1] == grid[2][0] == "O")

assert o_wins(("OXX", "OXO", "OOX")) == True
assert o_wins(("XOX", "OOX", "OOX")) == True
assert o_wins(("OXO", "XOX", "OXO")) == True
assert o_wins(("XXX", "XXX", "XXX")) == False
assert o_wins(("OXX", "OXO", "XXO")) == False