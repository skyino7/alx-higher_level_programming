#!/usr/bin/python3

for i in range(10):
    for j in range(10):
        comb = str(i) + str(j)
        if i == 9 and j == 9:
            print(comb)
        else:
            print(comb + ", ", end="")
