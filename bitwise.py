from binary import validate_binary
def binary_to_decimal(binary):
    return int(binary, 2)
def decimal_to_binary(decimal):
    return bin(decimal)[2:]
    # [2:] beacuse first two number is0b which means it is binary numbe rdef bitwise_calculator(a,b,op):
def bitwise_calculator(a, b, op):
    if not validate_binary(a):
        return "Invalid first binary number"
    if not validate_binary(b):
        return "Invalid second binary number"
    a = binary_to_decimal(a)
    b = binary_to_decimal(b)
    if op == "&":
        return decimal_to_binary(a & b)
    elif op == "|":
        return decimal_to_binary(a | b)
    elif op == "^":
        return decimal_to_binary(a ^ b)
    else:
        return "Invalid operation"
    
def shift_calculator(a, op, n):
    if not validate_binary(a):
        return "Invalid binary number"
    if n < 0:
        return "Invalid shift amount"
    a = binary_to_decimal(a)
    if op == "<<":
        return decimal_to_binary(a << n)
    elif op == ">>":
        return decimal_to_binary(a >> n)
    else:
        return "Invalid operation"
def not_calculator(binary):
    if not validate_binary(binary):
        return "Invalid binary number"
    result = ""
    for bit in binary:
        if bit == "0":
            result += "1"
        else:
            result += "0"
    return result


    