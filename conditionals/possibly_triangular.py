def possibly_triangular(a, b, c):
    return a + b >= c and b + c >= a and a + c >= b

assert possibly_triangular(3, 4, 5) == True
assert possibly_triangular(2, 2, 5) == False