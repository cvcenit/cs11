def last_letters(words):
    s = ""
    for word in words:
        s += word[-1]
    return s

print(last_letters(('can', 'i', 'have', 'this', 'dance'))
)