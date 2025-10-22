def longest_streak(names):
    if len(names) <= 1:
        return len(names)
    streak = 1
    n = []
    for i in range(1, len(names)):
        if names[i] == names[i - 1]:
            streak += 1
        else:
            streak = 1
        n += [streak]
    print(n)
    return max(n)

print(longest_streak((
        'charlie',
        'charlie',
        'charlie'
    ))
)

print(longest_streak((
        'magnus',
        'xqc',
        'magnus',
        'magnus',
        'charlie',
        'charlie',
        'charlie',
        'magnus',
        'xqc',
        'magnus',
        'magnus',
        'charlie',
        'magnus',
    ))
)

print(longest_streak((
        'charlie',
        'charlie',
        'xqc',
        'xqc',
        'charlie',
        'charlie',
        'charlie',
        'charlie',
        'xqc',
        'xqc',
        'charlie',
        'charlie',
    ))
)