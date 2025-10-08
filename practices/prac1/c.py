def darts_landed(x1, y1, x2, y2, darts_coords):
    if not darts_coords:
        return 0
    else:
        return (x1 <= darts_coords[0][0] <= x2 and y1 <= darts_coords[0][1] <= y2) + darts_landed(x1, y1, x2, y2, darts_coords[1:])

print(darts_landed(-20, -10, 20, 10, (
    (0, 0),
    (500, 0),
    (1, 1),
))
)