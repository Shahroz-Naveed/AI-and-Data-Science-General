# 7. Write a program to find the largest of three numbers.
num1  = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1>num2 and num1>num3:
    print(f"First number {num1} is largest ")
elif num2>num1 and num2>num3:
    print(f"Second number {num2} is largest ")
else:
    print(f"Third number {num3} is largest ")