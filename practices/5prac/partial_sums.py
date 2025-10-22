def partial_sums(seq):
    res = [0]
    for n in seq:
        res += [res[-1] + n]
    return res

print(partial_sums((3, 1, 4, 1)))