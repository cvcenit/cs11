def find_pen(catalog, want):
    p, r = (0, 0)
    for item in catalog:
        if item[0] == want:
            return item[1], item[2]
    raise ValueError


print(find_pen((
    ('Black Ballpen', 20, 8),
    ('Blue Ballpen', 20, 8),
    ('White Ballpen', 50, 1),
    ('Sign Pen', 100, 9),
    ('Pencil', 800, 7),
    ('Fountain Pen', 20, 2),
    ('Waifu Pen', 5000, 10),
), 'Pencil')
)