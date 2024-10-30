# 19. Check if a string input is uppercase, lowercase, or a mix.
string = input("Enter a string: ")

# To check if the string is uppercase

if string.isupper():
    print("The string is uppercase.")
elif string.islower():
    print("The string is lowercase.")
else:
    print("The string is a mix of uppercase and lowercase letters.")