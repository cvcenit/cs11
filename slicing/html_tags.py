def identify_tag(tag):
    return tag[2:-1] * (tag[1] == "/") or tag[1:-1] * (tag[1] != "/")

print(identify_tag("<h1>"))
print(identify_tag("</aas>"))
print(identify_tag("<h2>"))

assert identify_tag("<h1>") == "h1"
assert identify_tag("</aas>") == "aas"
assert identify_tag("</h2>") == "h2"