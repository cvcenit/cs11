def game_mistakes(words):
    a, b = (0, 0)
    for i in range(1, len(words)):
        if i % 2 == 0:
            a += words[i][0] != words[i - 1][-1]
        elif i % 2 != 0:
            b += words[i][0] != words[i - 1][-1]
    return a, b

print(game_mistakes((
    'pizza', 'apple', 'egg', 'hazelnut', 'tofu', 'udon', 'nut',
    'tinapay', 'yema', 'edamame', 'eggplant', 'durian', 'nutella',
    'avocado', 'orangutan', 'noodles', 'spaghetti', 'iodizedsalt',
    'toatmeal', 'linguine', 'egg', 'gulaman', 'nut', 'tea', 'uh',
))
)