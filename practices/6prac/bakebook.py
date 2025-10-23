def bakebook(events):
    users = set()
    friends = {}

    for event in events:
        t, n = event
        if t == "register":
            if n in users:
                print("already registered")
            else:
                users.add(n)
                friends.setdefault(n, set())
                print("ok")
        elif t == "num_friends":
            if n in users:
                print(len(friends[n]))
            else:
                print('not found')
        else:
            if n[0] in users and n[1] in users:
                if n[0] == n[1]:
                    print("invalid")
                elif n[1] in friends[n[0]]:
                    print("already friends")
                else:
                    friends[n[0]].add(n[1])
                    friends[n[1]].add(n[0])
                    print("ok")
            else:
                print("not found")


bakebook((
    ("num_friends", "gordon"),
    ("register", "gordon"),
    ("num_friends", "gordon"),
    ("register", "ramsey"),
    ("register", "ramsay"),
    ("register", "ramses"),
    ("make_friends", ("gordon", "ramsay")),
    ("make_friends", ("ramsay", "gordon")),
    ("num_friends", "gordon"),
    ("num_friends", "ramses"),
    ("num_friends", "gordan"),
    ("register", "ramsay"),
    ("make_friends", ("gordon", "ramses")),
    ("num_friends", "gordon"),
    ("num_friends", "ramsey"),
    ("make_friends", ("gordon", "gordon")),
    ("make_friends", ("garden", "garden")),
))
