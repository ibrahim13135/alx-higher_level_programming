#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    i = 0  # Initialize the counter
    try:
        while i < x:  # Use < instead of is not
            print(my_list[i], end='')
            i += 1
            num += 1
    except IndexError:
        pass
    print()
    return num 
