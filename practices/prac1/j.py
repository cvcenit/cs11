def bacteria_counts(b, n):
    return _bacteria_counts(b, n-1)

def _bacteria_counts(b, n):
    if n == 0:
        return (b,)
    else:
        return *_bacteria_counts(b, n-1), b * (2 ** (n))

print(bacteria_counts(1, 4))