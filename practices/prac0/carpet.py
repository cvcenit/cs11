def carpet(r, c, r1, c1, i, j):
    return (("." * c), ) * (i) + (("." * (j) + "#" * (c1) + "." * (c - c1 - j)),) * (r1) + ("." * (c),) * (r - r1 - i)

print(carpet(6, 9, 3, 4, 1, 2))