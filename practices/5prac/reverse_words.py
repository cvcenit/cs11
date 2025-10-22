def reverse_words(text):
    res = []
    for word in text.split():
        res.append(word[::-1])
    return " ".join(res)

print(reverse_words('loopang hinirang')
)