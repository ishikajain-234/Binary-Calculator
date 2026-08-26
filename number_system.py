def binary_to_decimal(binary):
    return int(binary,2)
def decimal_to_binary(decimal):
    return bin(decimal)[2:]
#[2:] as first 2 reprsent it belongs to binary system 
def octal_to_decimal(octal):
    return int(octal)
def decimal_to_octal(decimal):
    return oct(decimal)[2:]
def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal,16)
def decimal_to_decimal(decimal):
    return hex(decimal)[2:].upper()
def is_valid_number(number, base):

    valid_digits = {
        2: "01",
        8: "01234567",
        10: "0123456789",
        16: "0123456789ABCDEFabcdef"
    }

    if base not in valid_digits:
        return False

    for digit in number:
        if digit not in valid_digits[base]:
            return False

    return True
def convert(number,from_base,to_base):
    if not is_valid_number(number, from_base):
        return "Invalid number for the selected base"
    decimal=int(number,from_base)
    if to_base==2:
        return bin(decimal)[2:]
    elif to_base == 8:
        return oct(decimal)[2:]

    elif to_base == 10:
        return str(decimal)

    elif to_base == 16:
        return hex(decimal)[2:].upper()

    else:
        return "Invalid destination base"
