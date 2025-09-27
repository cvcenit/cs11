from decorators import *

def div_by_9_between(a, b):
    if a > b:
        return ()
    elif a == b:
        return (b,) if b % 9 == 0 else ()
    else:
        if a % 9 == 0:
            return a, *div_by_9_between(a+1, b)
        else:
            return div_by_9_between(a+1, b)

print(div_by_9_between(27, 45))
print(div_by_9_between(1, 8))
print(div_by_9_between(18,18))
print(div_by_9_between(-50, -25))
print(div_by_9_between(-99, -99))