def intersection_stats(intervals, m):
    stats = []
    for k in range(m):
        stats += [0]
        for p in every_combination(intervals):
            stats[k] += int_count(p[0], p[1], k)
    return stats

def every_combination(tup):
    l = list(tup)
    c = []
    for p in l:
        fp = p
        for sp in l[1:]:
            c += ((fp, sp),)
        l = l[1:]
    return c

def int_count(p1, p2, k):
    (l1, r1), (l2, r2) = p1, p2
    if p1 == p2:
        return r1 - l1 == k
    elif l1 <= l2 < r2 <= r1:
        return r2 - l2 == k
    elif l2 <= l1 < r1 <= r2:
        return r1 - l1 == k
    elif l1 <= l2 < r1 <= r2:
        return r1 - l2 == k
    elif l2 <= l1 < r2 <= r1:
        return r2 - l1 == k
    else:
        return 0 == k

print(intersection_stats(((2, 4), (1, 3), (1, 5), (10**20 - 50, 10**20)), 4))
print(intersection_stats(((1, 3), (2, 5), (1, 3), (1, 3)), 5))
print(intersection_stats(((9, 15), (1, 10), (2, 6), (10, 20), (20, 50), (1, 21)), 20))