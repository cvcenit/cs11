def doublets(words):
    return tuple(word for word in words if len(word) % 2 == 0 and word[:len(word)//2] == word[len(word)//2:])

print(doublets(('haha', 'hah', 'lapulapu', 'laplap', 'malomali')))