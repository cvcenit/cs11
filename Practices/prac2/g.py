def text_file_bases(filenames):
    return tuple(base[:-4] for base in filenames if base[-4:] == ".txt")

print(text_file_bases((
    'hello.txt',
    'fromtheoutside.jpg',
    'lol.text',
    'lol.png.txt',
    'lol.png.png',
    'lol.txt.txt',
    'lol',
    'txt.txt.txt',
    'txt.txt.lol',
    'lolo.txt',
))
)