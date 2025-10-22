def divisible_by_exactly_one(x, y, u, v):
    for n in range(x, y + 1):
        if (n % u == 0 and n % v != 0) or (n % u != 0 and n % v == 0):
            print(n) 
        else:
            pass

divisible_by_exactly_one(10, 20, 3, 5)
