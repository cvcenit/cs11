def triangular_numbers(nums):
    return tuple(((n * n) + n) // 2 for n in nums)

assert triangular_numbers((3, 1, 4, 1)) == (6, 1, 10, 1)
