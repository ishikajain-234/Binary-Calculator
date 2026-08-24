# def binary_to_decimal(binary):
#     return int(binary, 2)
# def decimal_to_binary(decimal):
#     return bin(decimal)[2:]
#     # [2:] beacuse first two number is0b which means it is binary numbe r
# # b1 = input("Enter first binary number: ")
# # b2 = input("Enter second binary number: ")
# # op = input("Enter operation (+, -, /, *): ")
# def binary_calculator(a, op, b):

#     if op == "+":
#         return binary_to_decimal(a) + binary_to_decimal(b)

#     elif op == "-":
#         if a >= b:
#             return decimal_to_binary(a - b)
#         else:
#             return decimal_to_binary(b - a)

#     elif op == "/":
#         if binary_to_decimal(b) != 0:
#             return binary_to_decimal(a) // binary_to_decimal(b)
#         return "Cannot divide by zero"

#     elif op == "*":
#         return binary_to_decimal(a) * binary_to_decimal(b)

#     else:
#         return "Invalid operation"

# print(binary_calculator(b1, op, b2))
def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def binary_calculator(a, op, b):
    a = binary_to_decimal(a)
    b = binary_to_decimal(b)
    if op == "+":
        return decimal_to_binary(a + b)
    elif op == "-":
        if a >= b:
            return decimal_to_binary(a - b)
        else:
            return "-" + decimal_to_binary(b - a)
    elif op == "/":
        if b != 0:
            return decimal_to_binary(a // b)
        return "Cannot divide by zero"

    elif op == "*":
        return decimal_to_binary(a * b)
    else:
        return "Invalid operation"
