import sys

try:
    x=int(input("x: "))
    y=int(input("y: "))
except ValueError:
    print("there is a value error")

try:
    result=x/y
except ZeroDivisionError:
    print("can not divide by 0")
    sys.exit(1)



print(result)