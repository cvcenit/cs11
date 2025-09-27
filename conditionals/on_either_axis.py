def on_either_axis(a, b):
    return a == 0 or b == 0

assert on_either_axis(0, 0) == True
assert on_either_axis(0, 1) == True
assert on_either_axis(1, 0) == True
assert on_either_axis(2, 1) == False