def triangle_kind(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "degenerate"
    else:
        return (a == b == c) * "equilateral" + "scalene" * (a != b and b != c and a != c) + "isosceles" * ((a == b or a == c or b == c) and not (a == b == c))

print(triangle_kind(1, 1, 1))
print(triangle_kind(3, 4, 5))
print(triangle_kind(3, 3, 5))
print(triangle_kind(3, 2, 1))