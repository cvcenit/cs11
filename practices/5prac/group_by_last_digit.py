def group_by_last_digit(nums):
    n = [[] for _ in range(10)]
    for num in nums:
        d = num % 10
        for i in range(10):
            if d == i:
                n[d] += [num]
    return tuple(n)
print(group_by_last_digit((314, 159, 26, 5, 35, 8, 9, 7, 9, 32))
)