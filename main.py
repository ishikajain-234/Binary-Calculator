from boolean import (
    boolean_calculator,
    boolean_not,
    evaluate_expression,
    truth_table,
    simplify_expression,
    generate_sop,
    generate_pos
)
from bitwise import not_calculator
from bitwise import bitwise_calculator
from bitwise import shift_calculator
from binary import (
    binary_calculator,
    ones_complement,
    twos_complement,
    decimal_to_bcd,
    bcd_to_decimal,
    binary_to_gray,
    gray_to_binary,
    binary_multiplier,
    half_adder,
    full_adder,
    half_subtractor,
    full_subtractor
)
from number_system import convert



def number_system_menu():

    print("===== NUMBER SYSTEM CONVERSION =====")
    print("1. Binary → Decimal")
    print("2. Decimal → Binary")
    print("3. Convert Between Any Bases")
    print("4. Back")

    choose = input("Choose one option: ")

    if choose == "1":
        number = input("Enter binary number: ")
        result = convert(number, 2, 10)
        print("Decimal:", result)

    elif choose == "2":
        number = input("Enter decimal number: ")
        result = convert(number, 10, 2)
        print("Binary:", result)

    elif choose == "3":
        print("1. Binary")
        print("2. Octal")
        print("3. Decimal")
        print("4. Hexadecimal")

        from_choice = input("Convert from: ")
        to_choice = input("Convert to: ")
        number = input("Enter number: ")

        bases = {
            "1": 2,
            "2": 8,
            "3": 10,
            "4": 16
        }

        if from_choice in bases and to_choice in bases:
            result = convert(
                number,
                bases[from_choice],
                bases[to_choice]
            )
            print("Result:", result)

        else:
            print("Invalid base choice.")

    elif choose == "4":
        return

    else:
        print("Invalid option.")
def binary_operations_menu():

    print("===== BINARY OPERATIONS =====")
    print("1. Arithmetic")
    print("2. Complements")
    print("3. Binary Codes")
    print("4. Digital Logic")
    print("5. Back")

    choose = input("Choose one option: ")

    if choose == "1":
        arithmetic_menu()

    elif choose == "2":
        complement_menu()

    elif choose == "3":
        binary_codes_menu()

    elif choose == "4":
        digital_logic_menu()

    elif choose == "5":
        return

    else:
        print("Invalid option")
def arithmetic_menu():

    print("===== BINARY ARITHMETIC =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Back")

    choose = input("Choose one option: ")

    if choose == "1":
        a = input("Enter first binary number: ")
        b = input("Enter second binary number: ")

        print("Result:", binary_calculator(a, "+", b))

    elif choose == "2":
        a = input("Enter first binary number: ")
        b = input("Enter second binary number: ")

        print("Result:", binary_calculator(a, "-", b))

    elif choose == "3":
        a = input("Enter first binary number: ")
        b = input("Enter second binary number: ")

        print("Result:", binary_calculator(a, "*", b))

    elif choose == "4":
        a = input("Enter first binary number: ")
        b = input("Enter second binary number: ")

        print("Result:", binary_calculator(a, "/", b))

    elif choose == "5":
        return

    else:
        print("Invalid option")
def complement_menu():

    print("===== COMPLEMENTS =====")
    print("1. 1's Complement")
    print("2. 2's Complement")
    print("3. Back")

    choose = input("Choose one option: ")

    if choose == "1":
        binary = input("Enter binary number: ")
        print("1's Complement:", ones_complement(binary))

    elif choose == "2":
        binary = input("Enter binary number: ")
        print("2's Complement:", twos_complement(binary))

    elif choose == "3":
        return

    else:
        print("Invalid option")
def binary_codes_menu():

    print("===== BINARY CODES =====")
    print("1. Decimal → BCD")
    print("2. BCD → Decimal")
    print("3. Binary → Gray Code")
    print("4. Gray Code → Binary")
    print("5. Back")

    choose = input("Choose one option: ")

    if choose == "1":
        decimal = input("Enter decimal number: ")
        print("BCD:", decimal_to_bcd(decimal))

    elif choose == "2":
        bcd = input("Enter BCD: ")
        print("Decimal:", bcd_to_decimal(bcd))

    elif choose == "3":
        binary = input("Enter binary number: ")
        print("Gray Code:", binary_to_gray(binary))

    elif choose == "4":
        gray = input("Enter Gray Code: ")
        print("Binary:", gray_to_binary(gray))

    elif choose == "5":
        return

    else:
        print("Invalid option")
def digital_logic_menu():

    print("===== DIGITAL LOGIC =====")
    print("1. Binary Multiplier")
    print("2. Half Adder")
    print("3. Full Adder")
    print("4. Half Subtractor")
    print("5. Full Subtractor")
    print("6. Back")

    choose = input("Choose one option: ")

    if choose == "1":
        a = input("Enter first binary number: ")
        b = input("Enter second binary number: ")

        print("Result:", binary_multiplier(a, b))

    elif choose == "2":
        a = int(input("Enter first bit (0/1): "))
        b = int(input("Enter second bit (0/1): "))

        print("Result:", half_adder(a, b))

    elif choose == "3":
        a = int(input("Enter A (0/1): "))
        b = int(input("Enter B (0/1): "))
        carry = int(input("Enter Carry In (0/1): "))

        print("Result:", full_adder(a, b, carry))

    elif choose == "4":
        a = int(input("Enter first bit (0/1): "))
        b = int(input("Enter second bit (0/1): "))

        print("Result:", half_subtractor(a, b))

    elif choose == "5":
        a = int(input("Enter A (0/1): "))
        b = int(input("Enter B (0/1): "))
        borrow = int(input("Enter Borrow In (0/1): "))

        print("Result:", full_subtractor(a, b, borrow))

    elif choose == "6":
        return

    else:
        print("Invalid option")


def bitwise_menu():

    print("===== BITWISE =====")
    print("1. AND")
    print("2. OR")
    print("3. XOR")
    print("4. NOT")
    print("5. Left Shift")
    print("6. Right Shift")
    print("7. Back")

    choose = input("Choose: ")

    if choose == "1":
        a = input("Enter first binary number: ")
        b = input("Enter second binary number: ")
        print("Result:", bitwise_calculator(a, b, "&"))

    elif choose == "2":
        a = input("Enter first binary number: ")
        b = input("Enter second binary number: ")
        print("Result:", bitwise_calculator(a, b, "|"))

    elif choose == "3":
        a = input("Enter first binary number: ")
        b = input("Enter second binary number: ")
        print("Result:", bitwise_calculator(a, b, "^"))

    elif choose == "4":
        a = input("Enter binary number: ")
        print("Result:", not_calculator(a))

    elif choose == "5":
        a = input("Enter binary number: ")
        n = int(input("Enter shift amount: "))
        print("Result:", shift_calculator(a, "<<", n))

    elif choose == "6":
        a = input("Enter binary number: ")
        n = int(input("Enter shift amount: "))
        print("Result:", shift_calculator(a, ">>", n))

    elif choose == "7":
        return

    else:
        print("Invalid option")

def boolean_menu():

    while True:

        print("\n===== BOOLEAN ALGEBRA =====")
        print("1. Boolean Operation")
        print("2. Boolean NOT")
        print("3. Evaluate Expression")
        print("4. Truth Table")
        print("5. Simplify Expression")
        print("6. SOP")
        print("7. POS")
        print("8. Back")

        choice = input("Choose: ")
        if choice == "1":

            a = input("Enter first value (0/1): ")
            op = input("Enter operation (AND/OR/XOR): ")
            b = input("Enter second value (0/1): ")

            print(
                "Result:",
                boolean_calculator(a, b, op.upper())
            )

        # -------------------------
        # NOT
        # -------------------------

        elif choice == "2":

            a = input("Enter Boolean value (0/1): ")

            print(
                "Result:",
                boolean_not(a)
            )
        elif choice == "3":

            exp = input("Enter Boolean expression: ")

            variables = {}

            for variable in sorted(set(
                char for char in exp
                if char.isalpha()
            )):

                value = input(
                    f"Enter value for {variable} (0/1): "
                )

                variables[variable] = int(value)

            print(
                "Result:",
                evaluate_expression(exp, variables)
            )
        elif choice == "4":

            exp = input("Enter Boolean expression: ")

            result = truth_table(exp)

            if isinstance(result, str):

                print(result)

            else:

                variables, table = result

                print()

                for variable in variables:
                    print(variable, end=" ")

                print("| Result")

                print("-" * (len(variables) * 2 + 9))

                for row in table:

                    for value in row[:-1]:
                        print(value, end=" ")

                    print("|", row[-1])

    

        elif choice == "5":

            exp = input("Enter Boolean expression: ")

            result, steps = simplify_expression(exp)

            print("\nSimplified:", result)

            if steps:

                print("\nSteps:")

                for expression, law in steps:

                    print(expression, "<-", law)

        elif choice == "6":

            exp = input("Enter Boolean expression: ")

            print("SOP:", generate_sop(exp))



        elif choice == "7":

            exp = input("Enter Boolean expression: ")

            print("POS:", generate_pos(exp))


        elif choice == "8":
            break

        else:
            print("Invalid choice")

def main():
    while True:
        print("\n")
        print("================================")
        print("      BINARY & BOOLEAN CALC")
        print("================================")
        print("1. Number System Conversion")
        print("2. Binary Operations")
        print("3. Bitwise Operations")
        print("4. Boolean Algebra")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            number_system_menu()

        elif choice == "2":
            binary_menu()

        elif choice == "3":
            bitwise_menu()

        elif choice == "4":
            boolean_menu()

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice")