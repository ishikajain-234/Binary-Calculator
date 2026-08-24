# Binary & Boolean Calculator

A Python-based command-line calculator designed for **binary computation, bitwise operations, and Boolean algebra**.

The project goes beyond basic binary-to-decimal conversion by combining binary arithmetic, bitwise operations, Boolean operations, and Boolean expression simplification into one application.

## Features

### 🔢 Binary & Decimal Conversion

- Binary → Decimal
- Decimal → Binary

### ➕ Binary Arithmetic

Perform arithmetic directly on binary numbers:

- Addition `+`
- Subtraction `-`
- Multiplication `*`
- Division `/`

### ⚡ Bitwise Operations

Perform operations on binary numbers at the bit level:

- AND `&`
- OR `|`
- XOR `^`
- NOT `~`
- Left Shift `<<`
- Right Shift `>>`

### 🧠 Boolean Operations

Work with Boolean values (`0` and `1`):

- AND
- OR
- XOR
- NOT

### 📐 Boolean Algebra

Basic Boolean expression simplification using Boolean laws.

Currently supported:

```text
A + A' = 1
A * A' = 0
A + 0  = A
A + 1  = 1
A * 1  = A
A * 0  = 0
```

## Project Structure

```text
binary-boolean-calculator/
│
├── main.py       # Command-line interface
├── binary.py     # Binary conversion and arithmetic
├── bitwise.py    # Bitwise operations
├── boolean.py    # Boolean operations and algebra
└── README.md     # Project documentation
```

## How to Run

Make sure Python 3 is installed.

```bash
git clone <your-repository-url>
cd binary-boolean-calculator
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

## Example

```text
===== BINARY & BOOLEAN CALCULATOR =====

1. Binary ↔ Decimal
2. Arithmetic
3. Bitwise
4. Boolean Algebra
5. Exit

Choose one option: 2

===== ARITHMETIC =====

Enter first binary number: 1010
Enter second binary number: 0011
Enter operation (+, -, *, /): +

Result: 1101
```

## Project Goal

A specialized calculator combining **Binary Arithmetic, Bitwise Operations, and Boolean Algebra** in one tool, with a web interface planned for future versions.

## Current Status

**Version 1 — Terminal Application**

Core binary, arithmetic, bitwise, and basic Boolean operations are implemented.

**Next:** Advanced Boolean simplification, truth tables, error handling, and web interface.

## License

This project is open source.
