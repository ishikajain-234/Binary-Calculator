from number_system import (
    decimal_to_binary,
    binary_to_decimal
)


def test_decimal_to_binary():
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(5) == "101"


def test_binary_to_decimal():
    assert binary_to_decimal("1010") == 10
    assert binary_to_decimal("1111") == 15


def test_invalid_binary():
    assert binary_to_decimal("102") == "Invalid binary number"


def test_invalid_decimal():
    assert decimal_to_binary("abc") == "Invalid decimal number"