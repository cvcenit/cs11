def move2d(current, moves):
    direction = {
    'north': 1,
    'south': -1,
    'east': 1,
    'west': -1,
    }

    x, y = current

    for move in moves:
        if move[0] in {'north', 'south'}:
            y += direction.get(move[0]) * move[1]
        elif move[0] in {'east', 'west'}:
            x += direction.get(move[0]) * move[1]
    return x, y
assert move2d((3, 5), (
    ('south', 2),
    ('east', 5),
    ('west', 3),
    ('south', 2),
    ('south', 5),
)) == (5, -4)