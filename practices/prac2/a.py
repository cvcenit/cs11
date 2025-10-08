def first_letters(words):
    return tuple(word[0] for word in words)
print(first_letters(('can', 'i', 'have', 'this', 'dance')))