# 17. Write a program that continues to ask for a number until the correct number is guessed.
num = int(input("Enter a number to Match with existing one: "))
number = 50
while True:
    if num == number:
        print("Wow you guessed the exact number")
        break
    else:
        print("Try again!")
        num = int(input("Enter a number to Match with existing one: "))
