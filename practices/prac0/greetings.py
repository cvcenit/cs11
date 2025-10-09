def greet(n, greeting, name):
    return (n * (greeting + ", " + name + "! "))[:-1]

print(greet(3, "Welcome", "John"))