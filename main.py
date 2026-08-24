from boolean import boolean_calculator
from boolean import boolean_not
from boolean import simple
from binary import binary_calculator
from binary import binary_to_decimal
from binary import decimal_to_binary
from bitwise import bitwise_calculator
from bitwise import shift_calculator
from bitwise import not_calculator

print("===== BINARY CALCULATOR =====")
print("1. Binary ↔ Decimal")
print("2. Arithmetic")
print("3. Bitwise")
print("4. Boolean Algebra")
print("5. Exit")
choose = input("Choose one option: ")

if choose == "1":
    print("===== BINARY ↔ DECIMAL =====")
    print("1. Binary → Decimal")
    print("2. Decimal → Binary")
    conversion = input("Choose one option: ")
    if conversion == "1":
        binary = input("Enter binary number: ")
        result = binary_to_decimal(binary)
        print("Decimal:", result)
    elif conversion == "2":
        decimal = int(input("Enter decimal number: "))
        result = decimal_to_binary(decimal)
        print("Binary:", result)
    else:
        print("Invalid option")

elif choose == "2":
    print("===== ARITHMETIC =====")
    a = input("Enter first binary number: ")
    b = input("Enter second binary number: ")
    op = input("Enter operation (*,+,-,/): ")
    result = binary_calculator(a, op, b)
    print("Result:", result)

elif choose == "3":
    print("===== BITWISE =====")
    a = input("Enter binary number: ")
    op = input("Enter operation (&, |, ^, ~, <<, >>): ")
    if op == "&" or op == "|" or op == "^":
        b = input("Enter second binary number: ")
        result = bitwise_calculator(a, b, op)
    elif op == "~":
        result = not_calculator(a)
    elif op == "<<" or op == ">>":
        n = int(input("Enter shift amount: "))
        result = shift_calculator(a, op, n)
    else:
        result = "Invalid operation"
    print("Result:", result)

elif choose == "4":
    print("===== BOOLEAN ALGEBRA =====")
    print("1. Boolean Operations")
    print("2. Boolean NOT")
    print("3. Simplify Expression")
    option = input("Choose one option: ")
    if option == "1":
        a = input("Enter first Boolean value (0/1): ")
        b = input("Enter second Boolean value (0/1): ")
        op = input("Enter operation (AND, OR, XOR): ")
        result = boolean_calculator(a, b, op)
        print("Result:", result)
    elif option == "2":
        a = input("Enter Boolean value (0/1): ")
        result = boolean_not(a)
        print("Result:", result)
    elif option == "3":
        exp = input("Enter Boolean expression: ")
        result = simple(exp)
        print(result)
    else:
        print("Invalid option")
  
elif choose == "5":
    print("Exit")
else:
    print("Invalid option")

    


