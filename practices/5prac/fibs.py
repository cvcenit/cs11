def fibs(n):
    res = [0, 1]
    for x in range(n):
        res += [res[-1] + res[-2]]
    return res[:n]
print(fibs(1))