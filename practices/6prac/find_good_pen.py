def find_good_pen(catalog, p1, p2, r1, r2):
    res = []
    for pen in catalog:
        if p1 <= pen[1] <= p2 and r1 <= pen[2] <= r2:
            res.append(pen[0])
    return res

print(find_good_pen((
    ('Black Ballpen', 20, 8),
    ('Blue Ballpen', 20, 8),
    ('White Ballpen', 50, 1),
    ('Sign Pen', 100, 9),
    ('Pencil', 800, 7),
    ('Fountain Pen', 20, 2),
    ('Waifu Pen', 5000, 10),
), 20, 888, 6, 9)
)