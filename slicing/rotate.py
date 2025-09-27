def rotate_clockwise(m):
    return (m[1][0], m[0][0]), (m[1][1], m[0][1])

assert rotate_clockwise(((1, 2), (3, 4))) == ((3, 1), (4, 2))