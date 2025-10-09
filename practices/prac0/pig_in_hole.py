def has_piggy_hole(p, h, m):
    return bool((p >= m * h) * (p % h == 0) or (p % h != 0) * ((1 + p // h) >= m))
print(has_piggy_hole(24, 6, 6))
print(has_piggy_hole(24, 5, 5))