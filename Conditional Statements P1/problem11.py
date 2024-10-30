# 11. Check if a given number is a multiple of both 3 and 5.
num1 = int(input("Enter a number: "))
if num1 % 3 == 0 and num1 % 5 == 0:
    print(f"{num1} is a multiple of both 3 and 5.")
else:
    print(f"{num1} is not a multiple of both 3 and 5.")
