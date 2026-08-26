from binary import (
    binary_calculator,
    ones_complement,
    twos_complement
)


def test_binary_addition():
    assert binary_calculator("1010", "+", "0011") == "1101"


def test_binary_subtraction():
    assert binary_calculator("1010", "-", "0011") == "111"


def test_binary_multiplication():
    assert binary_calculator("101", "*", "10") == "1010"


def test_binary_division():
    assert binary_calculator("1010", "/", "10") == "101"


def test_ones_complement():
    assert ones_complement("1010") == "0101"


def test_twos_complement():
    assert twos_complement("1010") == "0110"


def test_invalid_binary():
    assert ones_complement("1020") == "Invalid binary number"