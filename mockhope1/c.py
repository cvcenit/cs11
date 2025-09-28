def evaluate_op(string):
    if string[0] == "A":
        return int(string[2:string.find(",")]) + int(string[string.find(",") + 1:-1])
    elif string[0] == "S":
        return int(string[2:string.find(",")]) - int(string[string.find(",") + 1:-1])
    elif string[0] == "M":
        return int(string[2:string.find(",")]) * int(string[string.find(",") + 1:-1])
print(evaluate_op("A(52,12)")
)