from boolean import (
    boolean_calculator,
    boolean_not,
    evaluate_expression,
    simplify_expression
)


def test_boolean_and():
    assert boolean_calculator("1", "1", "AND") == 1
    assert boolean_calculator("1", "0", "AND") == 0


def test_boolean_or():
    assert boolean_calculator("1", "0", "OR") == 1
    assert boolean_calculator("0", "0", "OR") == 0


def test_boolean_xor():
    assert boolean_calculator("1", "0", "XOR") == 1
    assert boolean_calculator("1", "1", "XOR") == 0


def test_boolean_not():
    assert boolean_not("0") == 1
    assert boolean_not("1") == 0


def test_boolean_expression():
    assert evaluate_expression(
        "A+B",
        {"A": 0, "B": 1}
    ) == 1


def test_boolean_expression_and():
    assert evaluate_expression(
        "AB",
        {"A": 1, "B": 1}
    ) == 1


def test_boolean_expression_not():
    assert evaluate_expression(
        "AB'",
        {"A": 1, "B": 0}
    ) == 1


def test_simplification_identity():
    result, steps = simplify_expression("A+0")

    assert result == "A"


def test_simplification_idempotent():
    result, steps = simplify_expression("A+A")

    assert result == "A"


def test_simplification_complement():
    result, steps = simplify_expression("A+A'")

    assert result == "1"