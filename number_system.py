def is_valid_number(number, base):
    valid_digits = {
        2: "01",
        8: "01234567",
        10: "0123456789",
        16: "0123456789ABCDEFabcdef"
    }
    if base not in valid_digits:
           return False
    if not number:
        return False
    for digit in str(number):
        if digit not in valid_digits[base]:
            return False
    return True
def binary_to_decimal(binary):

    if not is_valid_number(binary, 2):
        return "Invalid binary number"

    return int(binary, 2)

def decimal_to_binary(decimal):

    if not is_valid_number(decimal, 10):
        return "Invalid decimal number"

    decimal = int(decimal)

    if decimal < 0:
        return "Negative numbers are not supported"

    return bin(decimal)[2:]


def octal_to_decimal(octal):

    if not is_valid_number(octal, 8):
        return "Invalid octal number"

    return int(octal, 8)


def decimal_to_octal(decimal):

    if not is_valid_number(decimal, 10):
        return "Invalid decimal number"

    decimal = int(decimal)

    if decimal < 0:
        return "Negative numbers are not supported"

    return oct(decimal)[2:]


def hexadecimal_to_decimal(hexadecimal):

    if not is_valid_number(hexadecimal, 16):
        return "Invalid hexadecimal number"

    return int(hexadecimal, 16)


def decimal_to_hexadecimal(decimal):

    if not is_valid_number(decimal, 10):
        return "Invalid decimal number"

    decimal = int(decimal)

    if decimal < 0:
        return "Negative numbers are not supported"

    return hex(decimal)[2:].upper()


def convert(number, from_base, to_base):

    if not is_valid_number(number, from_base):
        return "Invalid number for the selected base"

    if to_base not in [2, 8, 10, 16]:
        return "Invalid destination base"

    decimal = int(number, from_base)

    if to_base == 2:
        return bin(decimal)[2:]

    elif to_base == 8:
        return oct(decimal)[2:]

    elif to_base == 10:
        return str(decimal)

    elif to_base == 16:
        return hex(decimal)[2:].upper()
