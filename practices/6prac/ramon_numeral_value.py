def ramon_numeral_value(b, v):
    res = 0
    for c in v:
        res += b.get(c)
    return res

print(ramon_numeral_value({
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}, 'VIII')
)