def max_pieces(conveyor_belt, k):
    c = []
    for i in range(len(conveyor_belt) - k + 1):
        c += [sum(conveyor_belt[i:i+k])]
    return max(c)
print(max_pieces((1, 4, 2, 1, 4, 2, 2, 1, 4, 2), 5))
print(max_pieces((4, 4, 4, 4, 4, 4, 4, 4, 4), 5))