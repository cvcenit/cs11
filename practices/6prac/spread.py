def spread(grid):
    for i in range(len(grid)):
        for k in range(len(grid[i])):
            if grid[i][k] == "." and is_adjacent_to_skulk(grid[i][k]):
                