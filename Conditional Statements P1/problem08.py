# 8. Create a program that checks if a given string is a palindrome.A string is palindrome when it's reverse is same as string.
string = input("Enter a string: ")
string = string.capitalize()
if string==string[::-1]:
    print(string)
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")