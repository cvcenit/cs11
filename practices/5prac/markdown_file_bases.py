def markdown_file_bases(filenames):
    res = []
    for file in filenames:
        if file[-3:] == ".md":
            res += [file[:-3]]
    return res

print(markdown_file_bases((
    'hello.md',
    'fromtheoutside.jpg',
    'lol.mdown',
    'lol.amd',
    'md.txt',
    'lol.png.md',
    'lol.png.png',
    'lol.md.md',
    'lol',
    'md.md.md',
    'md.md.lol',
    'lolo.md',
))
)