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
def ones_complement(binary):
    result =""
    for bit in binary:
        if bit=="0":
            result+="1"
        else:
            result+="0"
    return result 
def twos_complement(binary):
    ones = ones_complement(binary)

    decimal = int(ones, 2) + 1

    result = bin(decimal)[2:]

    return result.zfill(len(binary))
# each decimal digit gets converted separately into 4 bits.
def decimal_to_bcd(decimal):
    decimal = str(decimal)

    result = ""

    for digit in decimal:
        binary = bin(int(digit))[2:]
        binary = binary.zfill(4)
        result += binary

    return result
def bcd_to_decimal(bcd):
    if len(bcd) % 4 != 0:
        return "Invalid BCD"

    result = ""

    for i in range(0, len(bcd), 4):
        group = bcd[i:i+4]

        digit = int(group, 2)

        if digit > 9:
            return "Invalid BCD"

        result += str(digit)

    return int(result)
# first gray bit is first binary bit and then every neext bit is prev binary bit xor current binry bit 
def binary_to_gray(binary):

    gray = binary[0]

    for i in range(1, len(binary)):
        gray += str(int(binary[i - 1]) ^ int(binary[i]))

    return gray

# First Binary bit = first Gray bit and next bianry bit prev binary bit xor current gray bit 
def gray_to_binary(gray):

    binary = gray[0]

    for i in range(1, len(gray)):
        binary += str(int(binary[i - 1]) ^ int(gray[i]))

    return binary
def half_adder(a, b):
    sum_bit = a ^ b
    carry = a & b

    return sum_bit, carry


def full_adder(a, b, carry_in):
    sum_bit = a ^ b ^ carry_in

    carry_out = (a & b) | (carry_in & (a ^ b))

    return sum_bit, carry_out


def half_subtractor(a, b):
    difference = a ^ b
    borrow = (1 - a) & b

    return difference, borrow

def full_subtractor(a, b, borrow_in):
    difference = a ^ b ^ borrow_in

    borrow_out = ((1 - a) & (b | borrow_in)) | (b & borrow_in)

    return difference, borrow_out

def binary_multiplier(a, b):

    a = int(a, 2)
    b = int(b, 2)

    result = 0

    while b > 0:

        if b & 1:
            result += a

        a = a << 1
        b = b >> 1

    return bin(result)[2:]