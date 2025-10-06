def matches(team1, team2):
    if not team1 or not team2:
        return ()
    else:
        return (team1[0], team2[0],), *matches(team1[1:], team2[1:])

print(matches(
    ('Domon', 'Tokiya', 'Fuuko', 'Koganei', 'Recca'),
    ('Noroi', 'Kai', 'Mikoto', 'Joker', 'Kurei', 'hello'),
))