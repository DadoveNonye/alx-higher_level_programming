#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if "a" <= i <= "z":
            upper = chr(ord(i) - 32)
            result += upper
        else:
            result += i
    print("{}".format(result))
        
