def get_plates(conveyor_belt, k):
    if not conveyor_belt:
        return []
    s = conveyor_belt[0]
    plates = [s]
    for item in conveyor_belt[1:]:
        if abs(s - item) <= k:
            s = item
            plates += [s]
    return plates

print(get_plates((1, 10, 3, 2, 5, 8), 3))