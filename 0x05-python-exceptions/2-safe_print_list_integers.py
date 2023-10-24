#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    try:
        for item in my_list:
            if printed_count >= x:
                break
            if isinstance(item, int):
                if printed_count > 0:
                    print("", end="")
                print("{:d}".format(item), end="")
                printed_count += 1
    except (TypeError, ValueError):
        pass
    print()
    return printed_count
