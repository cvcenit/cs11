def every_combination(tup):
    l = list(tup)
    combinations = []
    for pair in l:
        first_pair = pair
        for second_pair in l[1:]:
            combinations += ((first_pair, second_pair),)
        l = l[1:]
    return combinations

def check_if_intersecting(pair1, pair2):
    l1, r1 = pair1
    l2, r2 = pair2
    if (l1 <= l2 and r1 >= r2) or (l1 >= l2 and r1 <= r2) or (l1 <= l2 and r1 > l2) or (l1 > l2 and l1 < r2):
        return True
    else:
        return False

def count_intersecting(l):
    count = 0
    for pair in l:
        if check_if_intersecting(pair[0], pair[1]):
            count += 1
        else:
            count += 0
    return count

def num_intersecting_pairs(intervals):
    if len(intervals) == 1 or 0:
        return 0
    return count_intersecting(every_combination(intervals))


assert num_intersecting_pairs(((1, 3), (4, 7), (2, 5), (8, 9))) == 2
assert num_intersecting_pairs(((1, 10), (2, 3), (1, 4), (10, 11), (1, 20))) == 7
assert num_intersecting_pairs(((1, 10), (2, 3), (1, 4))) == 3
assert num_intersecting_pairs(((1, 3), (1, 3), (1, 3), (2, 3))) == 6
assert num_intersecting_pairs(((0, 50), )) == 0
assert num_intersecting_pairs(((0, 1), (1, 3), (2, 3))) == 1
assert num_intersecting_pairs(((0, 5), (4, 9), (9, 12), (8, 14))) == 3