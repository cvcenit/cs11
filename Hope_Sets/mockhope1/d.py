def take_all_and_count(items, want):
    return remaining(items, want), count(items, want)

def remaining(items, want):
    if not items:
        return ()
    else:
        if items[0].lower() == want.lower():
            return remaining(items[1:], want)
        else:
            return items[0], *remaining(items[1:], want)

def count(items, want):
    if not items:
        return 0
    else:
        if items[0].lower() == want.lower():
            return (1 + count(items[1:], want))
        else:
            return count(items[1:], want)

print(take_all_and_count(
    ('Bag', 'earrings', 'rings', "EarRings", 'kaban', 'ramen', 'EARRINGS', 'eArRiNgS', 'RAMEN', 'ears'),
    'Earrings',
)
)