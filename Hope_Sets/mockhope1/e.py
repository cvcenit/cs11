def take_all_and_count(items, want):
    return remaining(items, want), count(items, want)

def remaining(items, want):
    return tuple(item for item in items if item.lower() != want.lower())

def count(items, want):
    return len(tuple(item for item in items if item.lower() == want.lower()))

print(take_all_and_count(
    ('Bag', 'earrings', 'rings', "EarRings", 'kaban', 'ramen', 'EARRINGS', 'eArRiNgS', 'ears'),
    'Earrings',
)
)