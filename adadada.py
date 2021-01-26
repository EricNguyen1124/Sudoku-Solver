def invert_dict(a_dict):
    inverted = {}
    for key in a_dict:
        inverted[a_dict[key]] = key
        print(inverted)
    return inverted

test = {1: "A", 2: "B", 3: ["C", "D"]}
inverse = invert_dict(test)