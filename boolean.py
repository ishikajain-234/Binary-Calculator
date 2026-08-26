from itertools import product


# =========================
# BASIC BOOLEAN OPERATIONS
# =========================

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


# =========================
# INPUT VALIDATION
# =========================

def validate_expression(exp):

    exp = exp.replace(" ", "")

    if not exp:
        return False

    allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01+*'()"

    for char in exp:
        if char not in allowed:
            return False

    return True


# =========================
# EXPRESSION EVALUATOR
# =========================

def get_variables(exp):

    variables = []

    for char in exp:
        if char.isalpha() and char not in variables:
            variables.append(char)

    return sorted(variables)


def precedence(op):

    if op == "'":
        return 3

    if op == "*":
        return 2

    if op == "+":
        return 1

    return 0


def tokenize(exp):

    exp = exp.replace(" ", "")

    tokens = []

    for char in exp:

        if char.isalpha() or char in "01":

            if tokens and (
                tokens[-1].isalpha()
                or tokens[-1] in "01"
                or tokens[-1] == ")"
                or tokens[-1] == "'"
            ):
                tokens.append("*")

            tokens.append(char)

        elif char == "(":

            if tokens and (
                tokens[-1].isalpha()
                or tokens[-1] in "01"
                or tokens[-1] == ")"
                or tokens[-1] == "'"
            ):
                tokens.append("*")

            tokens.append(char)

        elif char == ")":

            tokens.append(char)

        elif char == "'":

            tokens.append(char)

        elif char in "+*":

            tokens.append(char)

        else:

            return None

    return tokens


def apply_operator(values, operators):

    op = operators.pop()

    if op == "'":

        a = values.pop()
        values.append(1 - a)

    else:

        b = values.pop()
        a = values.pop()

        if op == "*":
            values.append(a & b)

        elif op == "+":
            values.append(a | b)

    return values, operators


def evaluate_expression(exp, variables_values):

    tokens = tokenize(exp)

    if tokens is None:
        return "Invalid expression"

    values = []
    operators = []

    for token in tokens:

        if token.isalpha() or token in "01":

            if token in "01":
                values.append(int(token))
            else:
                if token not in variables_values:
                    return "Variable value missing"

                values.append(variables_values[token])

        elif token == "(":

            operators.append(token)

        elif token == ")":

            while operators and operators[-1] != "(":
                values, operators = apply_operator(values, operators)

            if not operators:
                return "Invalid parentheses"

            operators.pop()

        else:

            while (
                operators
                and operators[-1] != "("
                and precedence(operators[-1]) >= precedence(token)
            ):
                values, operators = apply_operator(values, operators)

            operators.append(token)

    while operators:

        if operators[-1] == "(":
            return "Invalid parentheses"

        values, operators = apply_operator(values, operators)

    if len(values) != 1:
        return "Invalid expression"

    return values[0]


# =========================
# BOOLEAN LAWS
# =========================

def apply_boolean_laws(exp):

    exp = exp.replace(" ", "")
    steps = []

    # =========================
    # COMPLEMENT LAW
    # A + A' = 1
    # A * A' = 0
    # =========================

    if "+" in exp:

        terms = exp.split("+")

        if len(terms) == 2:

            left = terms[0]
            right = terms[1]

            if left + "'" == right or right + "'" == left:

                exp = "1"

                steps.append(
                    (exp, "Complement Law: A + A' = 1")
                )

                return exp, steps

    if "*" in exp:

        terms = exp.split("*")

        if len(terms) == 2:

            left = terms[0]
            right = terms[1]

            if left + "'" == right or right + "'" == left:

                exp = "0"

                steps.append(
                    (exp, "Complement Law: A * A' = 0")
                )

                return exp, steps

    # =========================
    # IDEMPOTENT LAW
    # A + A = A
    # A * A = A
    # =========================

    if "+" in exp:

        terms = exp.split("+")

        if len(terms) == 2 and terms[0] == terms[1]:

            exp = terms[0]

            steps.append(
                (exp, "Idempotent Law: A + A = A")
            )

            return exp, steps

    if "*" in exp:

        terms = exp.split("*")

        if len(terms) == 2 and terms[0] == terms[1]:

            exp = terms[0]

            steps.append(
                (exp, "Idempotent Law: A * A = A")
            )

            return exp, steps

    # =========================
    # IDENTITY LAW
    # A + 0 = A
    # A * 1 = A
    # =========================

    if "+" in exp:

        terms = exp.split("+")

        if len(terms) == 2:

            left = terms[0]
            right = terms[1]

            if right == "0":
                exp = left

                steps.append(
                    (exp, "Identity Law: A + 0 = A")
                )

                return exp, steps

    if "*" in exp:

        terms = exp.split("*")

        if len(terms) == 2:

            left = terms[0]
            right = terms[1]

            if right == "1":
                exp = left

                steps.append(
                    (exp, "Identity Law: A * 1 = A")
                )

                return exp, steps

    # =========================
    # DOMINATION LAW
    # A + 1 = 1
    # A * 0 = 0
    # =========================

    if "+" in exp:

        terms = exp.split("+")

        if len(terms) == 2:

            if "1" in terms:

                exp = "1"

                steps.append(
                    (exp, "Domination Law: A + 1 = 1")
                )

                return exp, steps

    if "*" in exp:

        terms = exp.split("*")

        if len(terms) == 2:

            if "0" in terms:

                exp = "0"

                steps.append(
                    (exp, "Domination Law: A * 0 = 0")
                )

                return exp, steps

    # =========================
    # INVOLUTION LAW
    # (A')' = A
    # =========================

    for variable in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

        if variable + "''" in exp:

            exp = exp.replace(
                variable + "''",
                variable
            )

            steps.append(
                (exp, "Involution Law: (A')' = A")
            )

            return exp, steps

    return exp, steps

# =========================
# STEP-BY-STEP SIMPLIFICATION
# =========================
def simple(exp):

    exp = exp.replace(" ", "")

    if "+" in exp:

        l, r = exp.split("+", 1)

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

        l, r = exp.split("*", 1)

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

def simplify_expression(exp):

    exp = exp.replace(" ", "")

    steps = []

    previous = ""

    while previous != exp:

        previous = exp

        exp, law_steps = apply_boolean_laws(exp)

        for step in law_steps:
            steps.append(step)

        simple_result = simple(exp)

        if simple_result != exp:
            steps.append(
                (
                    simple_result,
                    "Applying basic Boolean law"
                )
            )

            exp = simple_result

    return exp, steps


# =========================
# TRUTH TABLE
# =========================

def truth_table(exp):

    if not validate_expression(exp):
        return "Invalid expression"

    variables = get_variables(exp)

    if not variables:
        result = evaluate_expression(exp, {})
        return [(result,)]

    table = []

    for values in product([0, 1], repeat=len(variables)):

        assignment = dict(zip(variables, values))

        result = evaluate_expression(exp, assignment)

        table.append(
            tuple(values) + (result,)
        )

    return variables, table


# =========================
# SOP
# =========================

def generate_sop(exp):

    result = truth_table(exp)

    if isinstance(result, str):
        return result

    variables, table = result

    terms = []

    for row in table:

        output = row[-1]

        if output == 1:

            term = ""

            for i in range(len(variables)):

                variable = variables[i]
                value = row[i]

                if value == 1:
                    term += variable
                else:
                    term += variable + "'"

            terms.append(term)

    if not terms:
        return "0"

    return " + ".join(terms)


# =========================
# POS
# =========================

def generate_pos(exp):

    result = truth_table(exp)

    if isinstance(result, str):
        return result

    variables, table = result

    terms = []

    for row in table:

        output = row[-1]

        if output == 0:

            term = ""

            for i in range(len(variables)):

                variable = variables[i]
                value = row[i]

                if value == 0:
                    term += variable
                else:
                    term += variable + "'"

            terms.append("(" + " + ".join(term) + ")")

    if not terms:
        return "1"

    return " * ".join(terms)

