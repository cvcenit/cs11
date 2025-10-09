def winner(k, y):
    return "Kaguya wins!" * (k % y == 0 and not y % k == 0) + "Yuzuru wins!" * (y % k == 0 and not k % y == 0) + "It's a tie." * ((y % k == 0 and k % y == 0) or (y % k != 0 and k % y != 0))
print(winner(10, 5))
print(winner(10, 50))
print(winner(10, 10))