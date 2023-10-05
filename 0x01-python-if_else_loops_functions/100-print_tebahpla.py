#!/usr/bin/python3
result = ""

for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 1:
        result += chr(i).upper()
    else:
        result += chr(i).lower()

print("{}".format(result), end='')
