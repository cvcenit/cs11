def differentiate(coeffs):
    if not coeffs:
        return []
    f = []
    i = tuple(enumerate(rtz(coeffs)))
    for ind, t in i:
        f.append(ind * t)
    return f if f[0] != 0 else f[1:]

def rtz(c):
    s = 0
    it = list(enumerate(c))[::-1]
    for a, i in it:
        if i == 0 and frozenset(c[a:]) == frozenset((0,)):
            s = a
    if s == 0:
        return c
    return c[:s]

print(differentiate((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)))
print(differentiate((1, 2, 3, 0, 0, 0, 0)))
print(differentiate((1, 0, 2)))