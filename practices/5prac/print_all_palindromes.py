def print_all_palindromes(words):
    for word in words:
        if word.lower() == word.lower()[::-1]:
            print(word)

print_all_palindromes((
    'Madam',
    'Webew',
    'Abaca',
    'rawr',
    'lol',
))
