def enumerate_from(books, d):
    if not books:
        return ()
    else:
        return (d, books[0]), *enumerate_from(books[1:], d+1)

def enumerate_from_0(books):
    return enumerate_from(books, 0)

print(enumerate_from(('SICP', 'CTMCP', 'CLRS'), 5))