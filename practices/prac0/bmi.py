def bmi_check(weight, height):
    return "Go on a diet!" * (weight >= 25 * (height**2)) + "You are too thin!" * (weight < 25 * (height**2))

print(bmi_check(100, 2))