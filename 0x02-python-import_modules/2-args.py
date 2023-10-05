#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of and the list of its arguments."""

    from sys import argv

    args = len(argv)

    print(f"{args} argument:")

    for i in range(1, args):
        print(f"{i}: {argv[i]}")
