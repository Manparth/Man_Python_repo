#!/usr/bin/env python3.7

#Python implementation starts here 

a = int(input("enter the number:  "))

if a % 5 == 0  and a % 3 == 0:
    print("fizzbuzz")
elif a % 3 == 0:
    print("Fizz")
elif a % 5 == 0:
        print("buzz")
else:
    print(a)
