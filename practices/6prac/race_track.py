def bad_section_count(sections):
    res = 0
    for i in range(len(sections)):
        if i < len(sections) - 1:
            res += (sections[i] < sections[i - 1] and sections[i] < sections[i + 1]) or (sections[i] > sections[i - 1] and sections[i] > sections[i + 1])
        elif i == len(sections) - 1:
            res += (sections[i] < sections[i - 1] and sections[i] < sections[0]) or (sections[i] > sections[i - 1] and sections[i] > sections[0])
    return res

assert bad_section_count((3, 1, 4, 1, 5, 9, 2, 6, 5)) == 6, print(bad_section_count((3, 1, 4, 1, 5, 9, 2, 6, 5)))
assert bad_section_count((5, 5, 5)) == 0
assert bad_section_count((1, 2, 2, 2)) == 1
assert bad_section_count(()) == 0