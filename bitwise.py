def binary_to_decimal(binary):
    return int(binary, 2)
def decimal_to_binary(decimal):
    return bin(decimal)[2:]
    # [2:] beacuse first two number is0b which means it is binary numbe rdef bitwise_calculator(a,b,op):
def bitwise_calculator(a,b,op):
    a=binary_to_decimal(a)
    b=binary_to_decimal(b)
    if op=="&":
        return decimal_to_binary(a & b)
    elif op=="|":
        return decimal_to_binary(a|b)
    elif op=="^":
        return decimal_to_binary(a^b)
    else:
        return "Invalid result"
    
def shift_calculator(a, op, n):
    a = binary_to_decimal(a)

    if op == "<<":
        return decimal_to_binary(a << n)

    elif op == ">>":
        return decimal_to_binary(a >> n)

    else:
        return "Invalid operation"
def not_calculator(binary):
    result =""
    for bit in binary:
        if bit=="0":
            result+="1"
        else:
            result+="0"
    return result 


    