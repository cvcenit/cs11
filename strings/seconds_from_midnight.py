def seconds_since_midnight(t):
    return int(t[0:2]) * 60 * 60 + int(t[3:5]) * 60 + int(t[6:])

print(seconds_since_midnight("01:00:00"))
print(seconds_since_midnight("01:00:01"))
print(seconds_since_midnight("23:59:59"))
print(seconds_since_midnight("00:00:00"))