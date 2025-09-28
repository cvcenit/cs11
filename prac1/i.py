def pares_pairs(prices):
    if not prices:
        return ()
    else:
        return *every_pair(prices[0], prices[1:]), *pares_pairs(prices[1:])

def every_pair(first, rest):
    if not rest:
        return ()
    else:
        return tuple((first, rest[0])), *every_pair(first, rest[1:])

print(pares_pairs((1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10)))
print(pares_pairs((1, 2)))