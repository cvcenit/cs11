def append_ellipsis(s):
    return s.removesuffix("...") + "..."

print(append_ellipsis("Hello"))
print(append_ellipsis("Hello...."))