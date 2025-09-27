def center_align(s, w):
    return (abs(len(s) - w)//2) * " " + s + (((len(s) - w) % 2 != 0) + (abs(len(s) - w)//2)) * " "

assert center_align("banana", 10) == "  banana  "