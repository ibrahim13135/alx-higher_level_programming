#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])

        if operator == "+":
            result = add(a, b)
            print("{} + {} = {}".format(a, b, result))
        elif operator == "-":
            result = sub(a, b)
            print("{} - {} = {}".format(a, b, result))
        elif operator == "*":
            result = mul(a, b)
            print("{} * {} = {}".format(a, b, result))
        elif operator == "/":
            result = div(a, b)
            print("{} / {} = {}".format(a, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
