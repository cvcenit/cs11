def uniquify(seq):
    if not seq:
        return []
    res = [seq[0]]
    for s in seq:
        if s != res[-1]:
            res += [s]
    return res

print(uniquify((
    'hi',
    'hello',
    'hello',
    'hi',
    'hi',
    'hi',
    'hey',
    'hoy',
    'hoy',
    'hi',
    'hello',
    'hello',
))
)