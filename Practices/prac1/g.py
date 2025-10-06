from decorators import *

@show_calls
def suspense_sort(ratings):
    if is_sorted(ratings):
        return ratings
    else:
        

print(suspense_sort(()))
print(suspense_sort((0, 0, 1, 1, 2, 2, 0, 0)))