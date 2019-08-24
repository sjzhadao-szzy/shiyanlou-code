#!/usr/bin/env python3
amout=float(input("Entor amout:"))
inrate = float(input("Enter Interest rate:"))
period = int(input("Enter period Year:"))
value = 0
year = 1
while year <= period:
    value = amout + (amout * inrate)
    print("Year {} RS .{:.2f} ".format(year,value))
    amout = value
    year += 1

