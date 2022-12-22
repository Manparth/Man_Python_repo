#!usr/bin/env python3.7

#Python code implementation begins here

Farenheit= float(input("Enter the temperature (farenheit) that you want to see in Celcius? \n "))
celcius = (farenheit - 32) * 5/9

print(Farenheit , "F: is ", round(celcius,2), "C")
