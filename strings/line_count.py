def line_count(s):
    return 1+s.removesuffix("\n").count("\n")

print(line_count("""\
Roses are red
Violets are blue
I like CS 11
And so should you
"""))
print(line_count("""



"""))
print(line_count(""))
print(line_count("""a



a"""))
print(line_count("""



a"""))
print(line_count("""
Roses are red
Violets are blue
I like CS 11
And so should you

"""))