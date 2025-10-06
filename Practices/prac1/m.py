from decorators import *

@show_calls
def split_path(phrase):
    if not phrase:
        return ""
    else:
        if phrase[0] == "/":
            return split_path(phrase[1:])
        elif "/" not in phrase:
            return (phrase,)
        else:
            return phrase[:phrase.find("/")], *split_path(phrase[(1 + phrase.find("/")):])

print(split_path("Desktop/games/Minesweeper"))