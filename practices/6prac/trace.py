def trace(matrix):
    counter = 0
    res = 0
    for r in matrix:
        res += r[counter]
        counter += 1
    return res

print(trace(((1, 2, 3), (4, 5, 6), (7, 8, 9))))