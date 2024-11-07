# 11. Print the reverse of a given number.
num = int(input("Enter a number to reverse it : "))
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
    print("Reversed Number: " + str(reversed_num))