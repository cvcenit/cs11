from decorators import *

def perfect_shuffle(t):
    return sum(zip(t[:len(t)//2], t[len(t)//2:]), ())

print(perfect_shuffle((1, 2, 3, 4, 5, 6, 7, 8)))
print(perfect_shuffle((1, 2)))

print(perfect_shuffle((3, 2)))
print(perfect_shuffle(()))