#!/usr/bin/env python3
number = 0
n = 0
while n < 100:
    n += 1
    if n%7 == 0 or n%10 == 7 or n//10 == 7:
        continue
    else:
        print("%5d"%(n),end="  ")
        number += 1
    if number%6 == 0:
        print("\n")


