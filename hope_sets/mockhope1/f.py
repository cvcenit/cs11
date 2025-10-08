def _splits2(toys):
    return frozenset(_splits2(toys))

def _splits2(toys):
    if not toys:
        return ()
    else:
        return (toys[0])

def every_pair(seq):
    if len(seq) == 0:
        return ()
    elif len(seq) == 1:
        return seq
    else:
        return (seq[0], seq[1:]), every_pair

print(every_pair((1, 2, 3)))