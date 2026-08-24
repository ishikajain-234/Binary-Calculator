def boolean_calculator(a, b, op):
    a = int(a)
    b = int(b)
    if a not in [0, 1] or b not in [0, 1]:
        return "Boolean values must be 0 or 1"
    if op == "AND":
        return a & b
    elif op == "OR":
        return a | b
    elif op == "XOR":
        return a ^ b
    else:
        return "Invalid operation"

def boolean_not(a):
    a = int(a)
    if a not in [0, 1]:
        return "Boolean value must be 0 or 1"
    return 1 - a
def simple(exp):
    exp = exp.replace(" ", "")
    if "+" in exp:
        l, r = exp.split("+")
        # X + X' = 1
        if r == l + "'":
            return "1"
        # X + 0 = X
        elif r == "0":
            return l
        # X + 1 = 1
        elif r == "1":
            return "1"
    elif "*" in exp:
        l, r = exp.split("*")
        # X * X' = 0
        if r == l + "'":
            return "0"
        # X * 1 = X
        elif r == "1":
            return l
        # X * 0 = 0
        elif r == "0":
            return "0"
    return exp
    

 