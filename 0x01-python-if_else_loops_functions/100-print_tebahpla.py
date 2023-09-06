#!/usr/bin/python3
for val in range(ord('z'), ord('A') - 1, -1):
    if val % 2 == 0:
        char = chr(val).lower()
    else:
        char = chr(val).upper()
    print(char, end="")
