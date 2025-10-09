def snip(s):
    if ". " in s:
        return s[:s.index(". ") + 2] + "[...]" * (". " in s)
    else:
        return s

print(snip("You play, you pay, you bastard"))
print(snip("Michelle? Honey, anybody home?"))
print(snip("They were all dead."))