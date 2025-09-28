def broken_add(nums, w1, w2):
    if w1 == "even" and w2 == "even":
        return sum(i for i in nums) + (number_of_even(nums) % 2 == 1)
    elif w1 == "even" and w2 == "odd":
        return sum(i for i in nums) + (number_of_odd(nums) % 2 == 0)
    elif w1 == "odd" and w2 == "even":
        return sum(i for i in nums) + (number_of_even(nums) % 2 == 1)
    else:
        return sum(i for i in nums) + (number_of_odd(nums) % 2 == 0)

def number_of_odd(seq):
    if not seq:
        return 0
    else:
        return (seq[0] % 2 == 1) + number_of_odd(seq[1:])

def number_of_even(seq):
    if not seq:
        return 0
    else:
        return (seq[0] % 2 == 0) + number_of_even(seq[1:])

print(number_of_odd((1, 2, 3, 4, 4, 5, 5)))
print(number_of_even((1, 2, 3, 4, 4, 5, 5)))

print(broken_add((1, 1), "even", "even"))
print(broken_add((1, 1), "odd", "even"))