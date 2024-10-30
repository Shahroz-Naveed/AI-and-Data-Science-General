# 1. Write a program that checks if a given number is positive, negative, or zero.
num = int(input("Enter a number to check either positive, negative or zero ="))
if num == 0:
    print(f" Number {num} is zero.")
elif num > 0:
    print(f" Number {num} is positive ")
else:
    print(f" Number {num} is negative. ")