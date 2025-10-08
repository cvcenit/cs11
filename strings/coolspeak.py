def coolspeakify(w):
    return "7".join(("4".join(("0".join(("1".join(("1".join(("3".join(w.split("E"))).split("L"))).split("I"))).split("O"))).split("A"))).split("T"))

print(coolspeakify("HELLO I AM TOLL"))

assert coolspeakify("HELLO") == "H3110"