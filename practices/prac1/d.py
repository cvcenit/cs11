from decorators import *

@show_calls
def fix_music(sheet):
    if not sheet:
        return ()
    else:
        return sheet[::-1][0][::-1], *fix_music(sheet[:-1])

print(fix_music(((3, 1, 4), (1, 5))))
print(fix_music(((1, 2, 3), (4, 5), (6, 7, 8, 9))))